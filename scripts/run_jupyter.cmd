@echo off
setlocal

REM Launch Jupyter Notebook using the project virtual environment.
REM This avoids PowerShell execution-policy issues with Activate.ps1.

set VENV_PY=.venv\Scripts\python.exe
if not exist "%VENV_PY%" (
  echo ERROR: "%VENV_PY%" not found.
  echo Create the venv first:
  echo   py -3 -m pip install --user uv
  echo   py -3 -m uv venv
  echo   py -3 -m uv sync
  exit /b 1
)

"%VENV_PY%" -m jupyter notebook
