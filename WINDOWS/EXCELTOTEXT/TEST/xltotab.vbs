Set objArgs = WScript.Arguments

' Instructions : 
'
' Run as tab.vbs <full path of origin file> <full path of output file>
' 
' Function : Converts the excel to tab separated and saves as output
'
' 







' TEST TEST FOR PROMPT
'Set wShell=CreateObject("WScript.Shell")
'Set oExec=wShell.Exec("mshta.exe ""about:<input type=file id=FILE><script>FILE.click();new ActiveXObject('Scripting.FileSystemObject').GetStandardStream(1).WriteLine(FILE.value);close();resizeTo(0,0);</script>""")
'sFileSelected = oExec.StdOut.ReadLine
'wscript.echo sFileSelected


' Parse cmd arguments
InputName = objArgs(0)
OutputName = objArgs(1)


' TEST TEST FOR SETTING PWD
'Set objShell = CreateObject("Wscript.Shell")
'Wscript.Echo objShell.CurrentDirectory
'objShell.CurrentDirectory = "C:\Users\P.Doulgeridis\Desktop"
'Wscript.Echo objShell.CurrentDirectory




' Create excel obj
Set objExcel = CreateObject("Excel.application")
objExcel.application.visible=false
objExcel.application.displayalerts=false
set objExcelBook = objExcel.Workbooks.Open(InputName)

' Save with specified format
' REPLACE "-4158" with "23" for comma separated
objExcelBook.SaveAs OutputName, -4158
objExcel.Application.Quit
objExcel.Quit