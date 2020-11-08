from os import walk, remove
from os.path import join
from win32com.client.gencache import EnsureDispatch
root = r'D:\.Desktop\Temp' # rootPath
excel = EnsureDispatch('Excel.Application') # Start Excel Application
for path, dirNames, fileNames in walk(root): # Foreach rootPath
	for fn in fileNames: # Foreach fileNames
		if fn[-4:] == '.xls': # Is XLS workbook
			filePath = join(path, fn) # Join it use '\'
			wb = excel.Workbooks.Open(filePath) # Open the XLS workbook
			wb.SaveAs(filePath + 'x', FileFormat=51) # ['xlsx': 51, 'xls': 56]   Save new file
			wb.Close() # Close old file
			print(filePath, '=>', filePath + 'x') # Print result
			remove(filePath) # Delete old file
excel.Application.Quit() # Close Excel Application