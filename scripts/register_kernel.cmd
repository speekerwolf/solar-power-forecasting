@echo off
setlocal

REM Register the project venv as a Jupyter kernel (so notebooks don't use system Python).

set VENV_PY=.venv\Scripts\python.exe
if not exist "%VENV_PY%" (
  echo ERROR: "%VENV_PY%" not found.
  echo Create the venv first:
  echo   py -3 -m pip install --user uv
  echo   py -3 -m uv venv
  echo   py -3 -m uv sync
  exit /b 1
)

"%VENV_PY%" -m ipykernel install --user --name solar-venv --display-name "Solar Forecasting (.venv)"
echo Done. In Jupyter: Kernel ^> Change Kernel ^> "Solar Forecasting (.venv)"
