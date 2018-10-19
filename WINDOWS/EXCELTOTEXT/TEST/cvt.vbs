' Instructions : 
'
' Run as tab.vbs <full path of origin file> <full path of output file>
' 
' Function : Converts the excel to comma separated and saves as output
'
' 


Const xlText = -4158

Set objArgs = WScript.Arguments
For I = 0 to objArgs.Count - 1

    FullName = objArgs(I)
    FileName = Left(objArgs(I), InstrRev(objArgs(I), ".") )

    Set objExcel = CreateObject("Excel.application")
    set objExcelBook = objExcel.Workbooks.Open(FullName)

    objExcel.application.visible=false
    objExcel.application.displayalerts=false

    objExcelBook.SaveAs FileName & "txt", xlText

    objExcel.Application.Quit
    objExcel.Quit   

    Set objExcel = Nothing
    set objExcelBook = Nothing

Next