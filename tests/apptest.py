#ToDo : Write tests for application interface
import pytest
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mp3wav.application import Mp3WavApp
from mp3wav.exceptions.fileexception import FileTypeException
from mp3wav.exceptions.libraryexception import LibraryException
from mp3wav.exceptions.filenotexistexception import FileNotExistException
from mp3wav.exceptions.samefileexception import SameFileException
from mp3wav.exceptions.overwriteexception import OverWriteException

    
def windowTest(qtbot):
    testapp = Mp3WavApp()
    testapp.show()
    qtbot.addWidget(testapp)
    assert testapp.isVisible()
    assert testapp.close()

def fileTypeTest(qtbot, tmpdir):
    testapp = Mp3WavApp()
    qtbot.addWidget(testapp)
    infile = tmpdir.mkdir("files").join("demo.mp3")
    infile.write("something")
    testapp.inputFileLine.setText(str(tmpdir.join("files", "demo.mp3")))
    testapp.outputFileLine.setText(str(tmpdir.join('files')))
    testapp.outputFileLineName.setText('demo.wave')
    with pytest.raises(FileTypeException):
        qtbot.mouseClick(testapp.conversionButton, Qt.LeftButton)
