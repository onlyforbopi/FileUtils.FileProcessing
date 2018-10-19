echo off
setlocal ENABLEDELAYEDEXPANSION

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::															::
::	EXCEL TO TAB											::
::															::
::		- CONVERT EXCEL TO TAB								::
::		- EXPAND TAB TO PREDEFINED SPACES					::
::															::		
::	CALL AS : xltotab.bat <file1> <file2> <n>				::
::															::
::			<file1> : Input file (xls, xlsx)				::
::			<file2> : Output file 							::		
::			<n>     : Number of spaces to expand tabs		::	
::															::
::															::
::	Requires : tab.vbs										::
::  Requires : Manual setup of working directory    		::
::															::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




set arg1=%1
set arg2=%2
set arg3=%3



ECHO "#################################################"
ECHO WORKING DIRECTORY: %~dp0
cd %~dp0


set /A tabexpand=%arg3%
ECHO "#################################################"
ECHO EXCEL TO TEXT CONVERTER
ECHO TAB EXPAND SET TO: %tabexpand%
ECHO.

ECHO WORKING DIRECTORY: %root%
set root=c:\Users\P.Doulgeridis\Desktop\
CD %root%

ECHO INPUT FILE: %root%%1
ECHO OUTPUTFILE: %root%%2.final.txt 

wscript tab.vbs %root%%1 %root%%2


more /T!tabexpand! %root%%2 > %root%%2.final.txt

ECHO SCRIPT END.
