import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp


class StatusBar(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 地步状态栏
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('./../../../image/anime-girl-3840x2160-4k-5k-19524.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        # self.statusBar()
        # # 创建一个菜单栏
        # menubar = self.menuBar()
        # # 添加菜单
        # fileMenu = menubar.addMenu('&File')
        # menubar.setNativeMenuBar(False)
        # # 添加事件
        # fileMenu.addAction(exitAction)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())
