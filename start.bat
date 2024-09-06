@echo off

REM Prompt users to read the README.1ST file for detailed instructions.
echo Please make sure you have read the README.1ST file before proceeding.
echo.

REM Check if the virtual environment folder exists
IF NOT EXIST "env" (
    REM Create a virtual environment named "env"
    python -m venv env
    IF %ERRORLEVEL% NEQ 0 (
        echo "Failed to create a virtual environment. Please ensure Python is installed."
        pause
        exit /b
    )
)

REM Activate the virtual environment
CALL env\Scripts\activate

REM Install the required Python packages
pip install -r requirements.txt

REM Run the download_and_parse.py script
python download_and_parse.py

REM Pause the script output
pause

REM Deactivate the virtual environment and exit
CALL env\Scripts\deactivate
exit