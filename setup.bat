@echo off
echo ======================================================
echo   Nairobi Road Encroachment Mapping System
echo   Setup Script for Windows
echo ======================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Ask if user wants to create virtual environment
set /p create_venv="Do you want to create a virtual environment? (recommended) [y/n]: "

if /i "%create_venv%"=="y" (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    
    echo [OK] Virtual environment created
    echo.
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
)

echo.
echo Installing dependencies...
echo This may take a few minutes...
echo.

python -m pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo X Error installing dependencies. Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ======================================================
echo   Setup Complete! [SUCCESS]
echo ======================================================
echo.
echo To run the application:
echo.
if /i "%create_venv%"=="y" (
    echo   1. Activate virtual environment: venv\Scripts\activate
)
echo   2. Run: streamlit run app.py
echo.
echo Your browser will automatically open to http://localhost:8501
echo.
echo For deployment instructions, see DEPLOYMENT.md
echo For quick start guide, see QUICKSTART.md
echo.
pause
