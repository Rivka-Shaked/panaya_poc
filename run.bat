@echo off
setlocal

REM Check if argument (JSON string) is provided
if "%~1"=="" (
    echo Usage: update-settings.bat "{json_string}"
    exit /b 1
)

REM Store the JSON argument
set "json=%~1"

REM Set the path to the settings file
set "settingsFile=C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json"

REM Create the config folder if it doesn't exist
if not exist "C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config" (
    mkdir "C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config"
)

REM Use PowerShell to write the JSON to the file
powershell -Command "Set-Content -Path '%settingsFile%' -Value '%json%' -Encoding UTF8"

REM Start the Agent process
start "" "C:\Program Files\Panaya\Agent\Agent.exe"

