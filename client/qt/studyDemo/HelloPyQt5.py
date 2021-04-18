import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget


class HelloWorld(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("This is a HelloWorld Widget")

        btn = QPushButton("hello_world", self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip("I am a button for hello world")
        btn.resize(btn.sizeHint())

        self.resize(400, 500)
        self.center(self, geometry=QDesktopWidget().availableGeometry())
        self.setWindowTitle("hello world :)")
        self.show()

    # 关闭程序的系统回调方法
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you want to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self, widget, geometry=None):
        geo = widget.frameGeometry()
        center = geometry.center()
        geo.moveCenter(center)
        widget.move(geo.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HelloWorld()
    sys.exit(app.exec_())
