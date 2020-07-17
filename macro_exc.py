import os, os.path
import win32com.client
if os.path.exists('D:\загрузки\проги\test.xlsm'): #Your file path
    excel_macro = win32com.client.DispatchEx("Excel.Application") 
    excel_path = os.path.expanduser('D:\загрузки\проги\test.xlsm') #Your file path
    workbook = excel_macro.Workbooks.Open(Filename = excel_path)
    excel_macro.Application.Run("test.xlsm!Module1.sgf") #Your file, module and macros name
    workbook.Save()
    excel_macro.Application.Quit()  
    del excel_macro
