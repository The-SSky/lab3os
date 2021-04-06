## ==> GUI FILE
from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    # ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.centralFrame.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.closeButton.clicked.connect(lambda: self.close())

        # # 
        self.ui.infoButton.clicked.connect(self.infoButton_onclick)
        self.ui.createFileButton.clicked.connect(self.createFileButton_onclick)
        self.ui.createFolderButton.clicked.connect(self.createFolderButton_onclick)
        self.ui.cmdButton.clicked.connect(self.cmdButton_onclick)

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
