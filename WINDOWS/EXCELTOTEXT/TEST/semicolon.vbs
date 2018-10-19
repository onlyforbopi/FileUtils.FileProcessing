' Instructions : 
'
' Run as tab.vbs <full path of origin file> <full path of output file>
' 
' Function : Converts the excel to semicolon separated and saves as output
'
' 




if WScript.Arguments.Count < 2 Then 
  WScript.Echo "Error! Please specify the source path and the destination. Usage: cvt3.vbs SourcePath.xls Destination.csv" 
  Wscript.Quit 
End If 
Dim oExcel 
Set oExcel = CreateObject("Excel.Application") 
oExcel.DisplayAlerts = FALSE 'to avoid prompts
Dim oBook, local
Set oBook = oExcel.Workbooks.Open(Wscript.Arguments.Item(0))
local = true 
call oBook.SaveAs(WScript.Arguments.Item(1), 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, local) 'this changed
oBook.Close False 
oExcel.Quit 
WScript.Echo "Done" 
