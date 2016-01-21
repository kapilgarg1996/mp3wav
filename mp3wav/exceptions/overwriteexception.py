from errordialog import ErrorDialog

class OverWriteException(Exception):
	def __init__(self, parent=None):
		super(OverWriteException, self).__init__()
		errorMessage = "The Destination File Already Exists"+\
			"\nTo overwrite it, tick the box in the application"
		if parent:
			dialog = ErrorDialog(parent, errorMessage)
			dialog.show()
			dialog.exec_()
		else:
			errorMessage = "The Destination File Already Exists"+\
				"\nTo overwrite it, add -o or --overwrite flag"
			print(errorMessage)
