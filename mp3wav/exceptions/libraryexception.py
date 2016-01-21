from mp3wav.exceptions.errordialog import ErrorDialog

class LibraryException(Exception):
	def __init__(self, parent=None):
		super(LibraryException, self).__init__()
		errorMessage = "There is something wrong with ffmpeg"+\
			"\nMake sure that ffmpeg is installed on your machine"
		if parent:
			dialog = ErrorDialog(parent, errorMessage)
			dialog.show()
			dialog.exec_()
		else:
			print(errorMessage)
