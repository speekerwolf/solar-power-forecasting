"""NREL NSRDB API client with caching, timeouts, and retries."""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any

import requests

DEFAULT_BASE = "https://developer.nrel.gov/api/solar/nsrdb/v2"


def _cache_path(cache_dir: Path, payload: dict[str, Any]) -> Path:
    key = json.dumps(payload, sort_keys=True, default=str)
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:24]
    return cache_dir / f"nsrdb_{digest}.json"


def fetch_nsrdb_json(
    *,
    params: dict[str, Any],
    api_key: str | None = None,
    base_url: str | None = None,
    timeout_seconds: float = 120.0,
    max_retries: int = 4,
    cache_dir: Path | None = None,
    use_cache: bool = True,
) -> dict[str, Any]:
    """GET NSRDB (or compatible NREL solar) endpoint and return parsed JSON.

    Parameters
    ----------
    params:
        Query parameters (must include required NSRDB fields for the endpoint you call).
    api_key:
        NREL API key; defaults to ``os.environ[\"NREL_API_KEY\"]``.
    base_url:
        Full URL to GET (without query string). Defaults to NSRDB v2 base; override for
        specific dataset endpoints under NREL developer docs.
    """
    key = api_key or os.environ.get("NREL_API_KEY")
    if not key:
        raise RuntimeError(
            "Missing NREL_API_KEY. Copy .env.example to .env and set your key."
        )

    base = base_url or os.environ.get("NSRDB_BASE_URL", DEFAULT_BASE)
    cache_root = cache_dir or Path(os.environ.get("NSRDB_CACHE_DIR", "cache/nsrdb"))
    cache_root.mkdir(parents=True, exist_ok=True)

    full_params = {"api_key": key, **params}
    if use_cache:
        cached = _cache_path(cache_root, {"base": base, "params": full_params})
        if cached.exists():
            return json.loads(cached.read_text(encoding="utf-8"))

    last_err: Exception | None = None
    for attempt in range(max_retries):
        try:
            response = requests.get(base, params=full_params, timeout=timeout_seconds)
            if response.status_code in (429, 500, 502, 503, 504):
                wait = min(30.0, 2.0**attempt)
                time.sleep(wait)
                continue
            response.raise_for_status()
            data = response.json()
            if use_cache:
                cached = _cache_path(cache_root, {"base": base, "params": full_params})
                cached.write_text(json.dumps(data), encoding="utf-8")
            return data
        except Exception as exc:  # noqa: BLE001 - propagate after retries
            last_err = exc
            time.sleep(min(30.0, 2.0**attempt))
    raise RuntimeError(f"NSRDB request failed after {max_retries} attempts") from last_err
