import os
import sys
import pexpect
from mp3wav.exceptions.fileexception import FileTypeException
from mp3wav.exceptions.libraryexception import LibraryException
from mp3wav.exceptions.filenotexistexception import FileNotExistException
from mp3wav.exceptions.samefileexception import SameFileException
from mp3wav.exceptions.overwriteexception import OverWriteException

class Converter(object):
	def __init__(self, infile, outfile, overwrite=False, caller=None):
		super(Converter, self).__init__()
		self.__inputFile = infile
		self.__outputFile = outfile
		self.__overwrite = overwrite
		self.caller = caller
		self.__dir = os.getcwd()

	def __getInputFile(self, fileName):
		return os.path.join(self.__dir, fileName)

	def __getOutputFile(self, fileName):
		return os.path.join(self.__dir, fileName)

	def __setInputFile(self, fileName):
		if not os.path.isabs(fileName):
			self.__inputFile = self.__getInputFile(fileName)

	def __setOutputFile(self, fileName):
		if not os.path.isabs(fileName):
			self.__outputFile = self.__getOutputFile(fileName)

	def __startConversion(self):
		infile = self.__inputFile
		outfile = self.__outputFile
		if not self.caller:
			self.checkValidity()
		args = ""
		if self.__overwrite:
			args = "-y "
		self.__command = "ffmpeg -i "+infile+" "+args+ outfile
		self.run = pexpect.spawn(self.__command)
		if self.caller:
			self.caller.statusUpdate("Converting...")
		else:
			print("Converting...")
		return 1

	def checkValidity(self):
		if not os.path.exists(self.__inputFile) :
			raise FileNotExistException()
		if not self.__inputFile.endswith("mp3"):
			raise FileTypeException(1)
		if not self.__outputFile.endswith("wav"):
			raise FileTypeException(2)
		if os.path.exists(self.__outputFile):
			if not self.__overwrite :
				raise OverWriteException()
	def convert(self):
		output = "Something Went Wrong"
		self.__setInputFile(self.__inputFile)
		self.__setOutputFile(self.__outputFile)
		status = self.__startConversion()

		if status:
			try:
				self.__progress = self.run.compile_pattern_list([pexpect.EOF, "size=\s+([0-9]+)", '(.+)'])
				while True:
					i = self.run.expect_list(self.__progress)
					if i==0:
						if self.caller:
							self.caller.statusUpdate("Completed...")
						else:
							print("Completed..")
						break ;
					elif i==1:
						if self.caller:
							self.caller.statusUpdate("Converting..")
						else:
							print("-+-")
					else:
						pass
			except TIMEOUT:
				raise LibraryException(caller)
		else:
			print(output)

