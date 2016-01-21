from mp3wav.exceptions.errordialog import ErrorDialog

class SameFileException(Exception):
	def __init__(self, parent=None):
		super(SameFileException, self).__init__()
		errorMessage = "The Destination File and Source File are same. \
			Select Different Name for destination file"
		if parent:
			dialog = ErrorDialog(parent, errorMessage)
			dialog.show()
			dialog.exec_()
		else:
			print(errorMessage)
