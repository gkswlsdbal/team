import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *

import main_event as ev

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType('ProjectUI.ui')[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    fileCount = 0
    currentData = ''
    newData = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.insertButton.clicked.connect(self.btnClick)
        self.installEventFilter(self)
        self.setAcceptDrops(True)
        self.FileList.itemDoubleClicked.connect(self.fileClick)
        self.actionCellAbsorption.triggered.connect(self.actionCells)
        self.actionFileAbsorption.triggered.connect(self.actionFiles)
        self.menuSave.triggered.connect(self.actionSaves)
        self.actionSave.triggered.connect(self.newSaves)
        self.cellList.itemClicked.connect(self.cellClick)

        # 차트 생성
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.graphLayout.addWidget(self.canvas)
        
        # 차트 폰트 설정
        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)

    # 파일 드레그앤 드랍
    def eventFilter(self, object, event):
        if object is self:
            ev.eventFilter(self, object, event)
        return False

    def btnClick(self):
        ev.btnClick(self)

    def fileClick(self):
        ev.fileClick(self)

    def fileCheck(self, file):
        ev.fileCheck(self, file)

    def actionCells(self):
        ev.CellAbsorption(self)

    def actionFiles(self):
        ev.FileAbsorption(self)

    def actionSaves(self):
        ev.FileSave(self)

    def newSaves(self):
        ev.newSave(self)

    def cellClick(self):
        ev.cellClick(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
