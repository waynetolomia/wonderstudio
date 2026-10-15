@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  py -3 serve.py
) else (
  python serve.py
)
if errorlevel 1 (
  echo.
  echo Python 3.10 or later is needed for local preview only.
  echo You may upload index.html to an HTTPS website without installing Python.
)
pause
