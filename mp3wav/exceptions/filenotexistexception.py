from errordialog import ErrorDialog

class FileNotExistException(Exception):
	def __init__(self, parent=None):
		super(FileNotExistException, self).__init__()
		errorMessage = "The File you selected does not exist"+\
			"\nPlease Choose Appropriate File"
		if parent:
			dialog = ErrorDialog(parent, errorMessage)
			dialog.show()
			dialog.exec_()
		else:
			print(errorMessage)