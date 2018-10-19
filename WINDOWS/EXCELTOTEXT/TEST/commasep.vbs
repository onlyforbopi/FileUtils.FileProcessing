Set objArgs = WScript.Arguments

' Parse cmd arguments
InputName = objArgs(0)
OutputName = objArgs(1)

' Create excel obj
Set objExcel = CreateObject("Excel.application")
objExcel.application.visible=false
objExcel.application.displayalerts=false
set objExcelBook = objExcel.Workbooks.Open(InputName)

' Save with specified format
' REPLACE "-4158" with "23" for comma separated
objExcelBook.SaveAs OutputName, 23
objExcel.Application.Quit
objExcel.Quit