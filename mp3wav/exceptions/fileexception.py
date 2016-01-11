import os
import sys
from errordialog import ErrorDialog

class FileTypeException(Exception):
	def __init__(self, sid, parent=None):
		super(FileTypeException, self).__init__()
		filetype = "mp3"
		if sid==2:
			filetype = "wav"
		errorMessage = "The Selected file is not "+filetype+\
		"\nSelect the appropriate file"
		if parent:
			dialog = ErrorDialog(parent, errorMessage)
			dialog.show()
			dialog.exec_()
		else:
			print(errorMessage)
