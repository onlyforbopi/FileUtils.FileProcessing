Private Sub mybut_Click(sender As Object, e As EventArgs) Handles mybut.Click
MsgBox("Click")
End Sub

Dim oExcel As Object
Dim oBook As Object


   oExcel = CreateObject("Excel.Application")
   oBook = oExcel.Workbooks.Open("C:\Users\aaa.xls")
   oBook.SaveAs("C:\Users\5A5.txt", -4158)

   oBook.Close(False)
   oExcel.Quit()

   
   
   