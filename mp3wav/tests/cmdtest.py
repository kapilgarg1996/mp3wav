import pytest
import os
from mp3wav.converter import Converter
from mp3wav.exceptions.fileexception import FileTypeException
from mp3wav.exceptions.libraryexception import LibraryException
from mp3wav.exceptions.filenotexistexception import FileNotExistException
from mp3wav.exceptions.samefileexception import SameFileException
from mp3wav.exceptions.overwriteexception import OverWriteException

def fileExistTest(tmpdir):
    outfile = tmpdir.mkdir("files").join("demo.wav")
    with pytest.raises(FileNotExistException):
        tester = Converter("any.mp3", str(outfile))
        tester.convert()

def fileTypeTest(tmpdir):
    infile = tmpdir.mkdir("files").join("demo.mp4")
    infile.write("something")
    outfile = tmpdir.join("files", "demo.wav")
    print(infile, outfile)
    with pytest.raises(FileTypeException):
        tester = Converter(str(infile), str(outfile))
        tester.convert()

def overwriteTest(tmpdir):
    infile = tmpdir.mkdir("files").join("demo.mp3")
    infile.write("something")
    outfile = tmpdir.join("files", "demo.wav")
    outfile.write("anything")
    with pytest.raises(OverWriteException):
        tester = Converter(str(infile), str(outfile))
        tester.convert()
