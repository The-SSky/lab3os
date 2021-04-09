import sys
import os
import glob
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from src.lab3 import correct_file_length

# GUI FILE
from ui_mainwindow import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    result_signal = pyqtSignal(int)
    result_sum = list()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(os.getcwd())

        # MOVE WINDOW
        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.titleBar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## MOVE APP EVENT
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ## PUTS SWAP INFO INTO LIST WIDGET
    def infoButton_onclick(self):
        path = self.ui.lineEdit.text()
        path = path.replace('\\', '/', -1)
        if path[-1] == "/":
            path = path + "*/"
        else:
            path = path + "/*/"
        result = glob.glob(path)
        
        for i, name in enumerate(result):
            result[i] = name.replace('\\', '/', -1)
            result[i] = correct_file_length(name) + '/'
        self.ui.textEdit.setText('\n'.join(result))


    def createFileButton_onclick(self):
        path = self.ui.lineEdit.text()
        path = correct_file_length(path)
        if not os.path.exists(path):
            with open(path, 'w'):
                self.ui.textEdit.setText("Файл %s был успешно создан" % path)
        else:
            self.ui.textEdit.setText("Файл %s уже существует" % path)

    def createFolderButton_onclick(self):
        path = self.ui.lineEdit.text()
        path = correct_file_length(path)
        try:
            os.makedirs(path)
        except OSError:
            self.ui.textEdit.setText("Папка %s не была создана" % path)
        else:
            self.ui.textEdit.setText("Папка %s была успешно создана" % path)

    def cmdButton_onclick(self):
        path = os.getcwd()
        path = path + '\\console.py'
        subprocess.Popen(path, shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

    