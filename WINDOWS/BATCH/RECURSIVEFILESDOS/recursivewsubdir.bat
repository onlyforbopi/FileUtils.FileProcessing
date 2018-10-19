@echo off

::3rd way
SET STARTDIR=C:\Users\p.doulgeridis\Desktop\niarxos\
for /f %%a IN ('dir /b /s "%STARTDIR%*.*"') do echo "%%a"