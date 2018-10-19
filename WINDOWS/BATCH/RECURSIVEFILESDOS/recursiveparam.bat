@ECHO OFF



REM C:\Users\p.doulgeridis\Desktop\niarxos>recursiveparam.bat "C:\Users\p.doulgeridis\Desktop\niarxos\"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\Concepts.pdf"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\datalogiII.pdf"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\recursiveonlyfiles.bat"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\recursiveparam.bat"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\recursivewsubdir.bat"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\testbat.bat"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\NF\v01.FIXED.xls"
REM "C:\Users\p.doulgeridis\Desktop\niarxos\NF\papa\v01.FIXED.xls"
REM Press any key to continue . . .

REM C:\Users\p.doulgeridis\Desktop>



::SET STARTDIR=C:\Users\p.doulgeridis\Desktop\niarxos\
SET STARTDIR=%1

for /f %%f in ('DIR /b /a-d /s "%STARTDIR%*.*"') do echo "%%f"


CD ..

pause