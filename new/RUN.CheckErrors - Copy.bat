SETLOCAL ENABLEEXTENSIONS
setlocal enabledelayedexpansion
@echo off

:::::::::::::::::::::::::::::::::::::::::::::
:: INTERFACE SPOT : DIMENSION / COLOR / FONT
COLOR 0B
MODE con:cols=110 lines=30
TITLE CHECK ERROR LOG SAP
::::
::


:::::::::::::::::::::::::::::::::::::::::::::
::BASIC VARIABLES
SET me=%0							
SET parent=%~dp0					
SET COUNTER=0
::::
::

:::::::::::::::::::::::::::::::::::::::::::::
::INITIALIZE THE DATE - SYSTEM
FOR /f "delims=" %%a IN ('wmic OS Get localdatetime  ^| find "."') DO SET dt=%%a
SET YYYY=%dt:~0,4%
SET YY=%YYYY:~2,2%
SET MM=%dt:~4,2%
SET DD=%dt:~6,2%
SET HH=%dt:~8,2%
SET Min=%dt:~10,2%
SET Sec=%dt:~12,2%
SET stamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%
::::
::

:::::::::::::::::::::::::::::::::::::::::::::
:: Paths to Script Directory / Control Folder Directory
SET SCRIPTDIR=C:\Users\p.doulgeridis\Desktop\CHECKERRORS\
SET CONTROLDIR=C:\Users\p.doulgeridis\Desktop\CHECKERRORS\ControlFolder\

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: PRINT BASIC SCRIPT PARAMETERS
ECHO ###################################################
ECHO SCRIPT: %me% 
ECHO PARENT DIRECTORY : %parent%


:::::::::::::::::::::::::::::::::::::::::::::
:: PATHS
:: /Interfaces/Payments/ELTA/log
:: /Interfaces/Payments/TAMEIA/log
:: /Interfaces/Payments/AL1/log
:: /Interfaces/Payments/TAMEIAPIS/log
:: /Interfaces/Payments/pPOS/Incoming/log
:: /Interfaces/Payments/ePOS/Incoming/log
:: /Interfaces/Payments/ATM/Incoming/log
:: /Interfaces/Payments/RCFILES/Incoming/log
:: /Interfaces/Payments/RFFILES/Incoming/log

:: Pulling all files in Control Directory
pause
echo launching ftp
::winscp.exe /script=C:\Users\p.doulgeridis\Desktop\CHECKERRORS\ftppull
pause

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Report on contents of directory and wait.
FOR %%i IN (%CONTROLDIR%\*.*) DO echo %%i
ECHO.

REM :choice
REM set /P c=Do you want to scan the files[Y/N]?
REM if /I "%c%" EQU "N" goto :EOF
REM if /I "%c%" EQU "Y" goto :nextstep
REM goto :choice

:: Trigger Prompt
:nextstep

 call :MsgBox "Would you like to scan the files?"  "VBYesNo+VBQuestion" "Click yes to scan"
    if errorlevel 7 (
        echo NO - Terminating.
		exit
    ) else if errorlevel 6 (
        echo YES - Scanning files...
        goto :scanfiles
    )
goto :nextstep

:scanfiles
	
pause


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Launch python scripts
echo Launching Python

:: Iterating over files in Control Directory and Reporting
FOR %%f in (%CONTROLDIR%*) do (
	echo %%f
	::python %SCRIPTDIR%checkerrorlogs.py %%f	
)
::python checkerrorlogs.py C:\Users\p.doulgeridis\Desktop\CHECKERRORS\BN181005_20181008_193708_LOG.001
pause

:: Emptying Control Directory






:MsgBox prompt type title
    setlocal enableextensions
    set "tempFile=%temp%\%~nx0.%random%%random%%random%vbs.tmp"
    >"%tempFile%" echo(WScript.Quit msgBox("%~1",%~2,"%~3") & cscript //nologo //e:vbscript "%tempFile%"
    set "exitCode=%errorlevel%" & del "%tempFile%" >nul 2>nul
    endlocal & exit /b %exitCode%
	
	
	