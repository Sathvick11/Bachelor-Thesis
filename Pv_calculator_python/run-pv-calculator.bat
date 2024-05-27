@echo off
setlocal

:: Specify the target folder to clean
set "TARGET_FOLDER=%CD%\pv-calculator.opd"

:: Remove all files from the target folder and its subfolders
for /r "%TARGET_FOLDER%" %%i in (*) do (
    echo Deleting file: %%i
    del "%%i"
)

:: Remove all subfolders from the target folder
for /d /r "%TARGET_FOLDER%" %%d in (*) do (
    echo Deleting directory: %%d
    rmdir /s /q "%%d"
)

:: Optional: Remove the target folder itself
:: rmdir /s /q "%TARGET_FOLDER%"


:: Specify the file path
set "FILE_PATH=%CD%\pv-calculator.opf"

:: Check if the file exists and delete it
if exist "%FILE_PATH%" (
    del "%FILE_PATH%"
    echo File deleted: %FILE_PATH%
) else (
    echo File not found: %FILE_PATH%
)
"C:\Program Files\ANSYS Inc\v232\optiSLang\optislang.exe" -b --new pv-calculator.opf --python pv_calculator_optislang.py

echo Done.
endlocal
pause
