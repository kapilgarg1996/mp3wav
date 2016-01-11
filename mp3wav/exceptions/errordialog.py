from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ErrorDialog(QDialog):
	def __init__(self, parent, msg):
		super(ErrorDialog, self).__init__(parent)
		parent.reset()
		self.errorMessage = QLabel(msg)
		self.layout = QGridLayout()
		self.layout.addWidget(self.errorMessage, 0, 0)
		self.setLayout(self.layout)