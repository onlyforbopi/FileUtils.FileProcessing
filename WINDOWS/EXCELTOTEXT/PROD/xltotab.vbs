''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'  Script   : xltotab.vbs
'  Function : Converts the excel to tab separated and saves as output
'  Inputs   : <origin file> <destination file>
'  Outputs  : <destination file> - converted to Text
'  Usage    : xltotab.vbs <origin file> <destination file>
'
'  Notes    : Requires full path to origin/output file
'  Called by: xltotab.bat            	            
'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'Run as xltotab.vbs <full path of origin file> <full path of output file>

Set objArgs = WScript.Arguments

' Parse cmd arguments
InputName = objArgs(0)
OutputName = objArgs(1)

' Create excel obj
Set objExcel = CreateObject("Excel.application")

' Turn off app visibility and alerts
objExcel.application.visible=false
objExcel.application.displayalerts=false

' Open new workbook
set objExcelBook = objExcel.Workbooks.Open(InputName)

' Save with specified format
' REPLACE "-4158" with "23" for comma separated
objExcelBook.SaveAs OutputName, -4158

' Quit Excel application
objExcel.Application.Quit
objExcel.Quit