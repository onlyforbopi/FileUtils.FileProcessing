@echo off



::1st way
SET STARTDIR=C:\Users\p.doulgeridis\Desktop\niarxos\
CD %STARTDIR%
for /R %%f in (*.*) do echo "%%f"
CD ..

pause


::2nd way
::Example directory
set SetupDir=C:\Usersp.doulgeridis\Desktop\niarxos\

::Loop in the folder with "/r" to search in recursive folders, %%f being a loop ::variable 
for /r "%SetupDir%" %%f in (*.*) do set /a counter+=1

echo there are %counter% files in your folder

PAUSE

::3rd way
for /f %%a IN ('dir /b /s "%STARTDIR%*.*"') do echo "%%a"

pause