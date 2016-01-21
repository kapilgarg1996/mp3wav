import os
import sys
import platform
import converter
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from exceptions.fileexception import FileTypeException
from exceptions.libraryexception import LibraryException
from exceptions.filenotexistexception import FileNotExistException
from exceptions.samefileexception import SameFileException
from exceptions.overwriteexception import OverWriteException

_Mp3WavApp__INFILE = 1
_Mp3WavApp__OUTFILE = 2
_Mp3WavApp__STATUS = 3
_Mp3WavApp__CHANGE = 4

class Mp3WavApp(QDialog):
	def __init__(self, parent=None):
		super(Mp3WavApp, self).__init__(parent)
		#imagePath = os.path.abspath("bengal-tiger-gazzing.jpg")
		#image = QImage(imagePath)
		'''self.changeLabel = QLabel("mp3 to wav")
		self.changeLabel.sid = 1
		self.changeLabel.setAlignment(Qt.AlignCenter)

		self.changeButton = QPushButton("Change")
		self.changeButton.setMinimumSize(50, 10)'''

		self.inputFilePicker = QPushButton("Pick Input File")
		self.inputFileLine = QLineEdit()
		self.inputFileLine.sid = 2
		self.outputFilePicker = QPushButton("Pick Output Directory")
		self.outputFileLine = QLineEdit()
		self.outputFileLineName = QLineEdit()
		self.outputFileLine.sid = 3

		self.overwriteLabel = QLabel("Overwrite Existing File")
		self.overwriteBox = QCheckBox()

		self.conversionButton = QPushButton("Convert")
		self.statusBar = QLabel("Status")
		self.statusBar.sid = 4

		self.appLayout = QGridLayout()
		#self.appLayout.addWidget(self.changeLabel, 0, 0)
		#self.appLayout.addWidget(self.changeButton, 0, 1)
		self.appLayout.addWidget(self.inputFilePicker, 0, 0)
		self.appLayout.addWidget(self.inputFileLine, 0, 1)
		self.appLayout.addWidget(self.outputFilePicker, 1, 0)
		self.appLayout.addWidget(self.outputFileLine, 1, 1)
		self.appLayout.addWidget(self.outputFileLineName, 1, 2)
		self.appLayout.addWidget(self.overwriteLabel, 2, 1)
		self.appLayout.addWidget(self.overwriteBox, 2, 2)
		self.appLayout.addWidget(self.conversionButton, 3, 2)
		self.appLayout.addWidget(self.statusBar, 3, 0)

		self.setLayout(self.appLayout)

		self.connect(self.inputFilePicker, SIGNAL("clicked()"), lambda: self.filePicked(__INFILE))
		self.connect(self.outputFilePicker, SIGNAL("clicked()"), lambda: self.filePicked(__OUTFILE))
		self.connect(self.conversionButton, SIGNAL("clicked()"), lambda: self.startConversion())

	def filePicked(self, sid):
		try:
			if sid ==__INFILE:
				self.inputFileLine.setText(QFileDialog.getOpenFileName())
				self.__infile = str(self.inputFileLine.text())
				self.checkFile(sid)
			elif sid == __OUTFILE:
				self.outputFileLine.setText(QFileDialog.getExistingDirectory())
				self.__outdir = str(self.outputFileLine.text())
		except FileTypeException:
			pass

	def startConversion(self):
		self.__infile = str(self.inputFileLine.text())
		self.__outdir = str(self.outputFileLine.text())
		self.__convert()

	def __convert(self):
		self.__outfilename = os.path.join(self.__outdir, str(self.outputFileLineName.text()))
		if not os.path.exists(self.__infile) :
			raise FileNotExistException(self)

		self.checkFile(__OUTFILE)

		if self.__infile == self.__outfilename:
			raise SameFileException(self)
		if os.path.exists(self.__outfilename):
			if not self.overwriteBox.isChecked() :
				raise OverWriteException(self)

		overwrite = self.overwriteBox.isChecked()
		self.starter = converter.Converter(self.__infile, self.__outfilename, overwrite, self)
		self.starter.convert()
		

	def checkFile(self, fileType):
		if fileType==__INFILE:
			if not self.__infile.endswith("mp3"):
				raise FileTypeException(fileType, self)
		elif fileType == __OUTFILE:
			if not self.__outfilename.endswith("wav"):
				raise FileTypeException(fileType, self)

	def reset(self):
		self.inputFileLine.setText("")
		self.outputFileLine.setText("")
		self.outputFileLineName.setText("")

	def statusUpdate(self, value):
		self.statusBar.setText(value)



