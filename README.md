Sub teste()

linha = Sheets("Planilha2").Range("A1").End(xlDown).Row + 1


Sheets("Planilha1").Select
Range("A2").Select
Selection.Copy
Sheets("Planilha2").Select
Range("A" & linha).Select
ActiveSheet.Paste


Sheets("Planilha1").Select
Range("B2").Select
Selection.Copy
Sheets("Planilha2").Select
Range("B" & linha).Select
ActiveSheet.Paste


Sheets("Planilha1").Select
Range("C2").Select
Selection.Copy
Sheets("Planilha2").Select
Range("C" & linha).Select
ActiveSheet.Paste

Sheets("Planilha1").Select
Application.CutCopyMode = False

