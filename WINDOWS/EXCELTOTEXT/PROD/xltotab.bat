@echo off
setlocal ENABLEDELAYEDEXPANSION

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::	EXCEL TO TAB
::	
::	Description:
::    - Convert Excel To Tab
::		- Expand Tab To Predefined Spaces
::
::	Call As:
::    xltotab.bat  <file1>  <file2>  <n>
::
::	Parameters:
::    <file1> : Input file (xls, xlsx)
::		<file2> : Output file
::		<n>     : Number of spaces to expand tabs
::															
:: Calls:
::	   xltotab.vbs
::	   replace.vbs
::    replace_quotes.vbs
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Parse command line parameters
set arg1=%1
set arg2=%2
set arg3=%3

:: Set tab expand variable to 3rd argument
set /A tabexpand=%arg3%

:: Report on Script parameters
ECHO "#################################################"
ECHO EXCEL TO TEXT CONVERTER
ECHO TAB EXPAND SET TO: %tabexpand%
ECHO.

ECHO WORKING DIRECTORY: %~dp0
ECHO CHANGING TO WORKING DIRECTORY
set root=%~dp0
CD %root%

ECHO INPUT FILE: %root%%1
ECHO OUTPUTFILE: %root%%2.final.txt 

:: Call vbscript to convert xl to text
wscript xltotab.vbs %root%%1 %root%%2.temp

:: Replace specific characters
cscript replace.vbs %root%%2.temp "," ""
cscript replace.vbs %root%%2.temp "." ""
cscript replace_quotes.vbs %root%%2.temp

:: Call "more" command with delayed expansion to expand tabs
more /T!tabexpand! %root%%2.temp > %root%%2

:: Clean trash files
ECHO CLEANUP
DEL %root%%2.temp

:: Script end
ECHO SCRIPT END.
