import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QImage
from PyQt5.QtCore import Qt, QRect


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        for i in range(10000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        # qp.setBrush(QColor(200, 0, 0))
        # qp.drawRect(10, 15, 90, 60)
        # qp.setBrush(QColor(255, 80, 0, 160))
        # qp.drawRect(130, 15, 90, 60)
        # qp.setBrush(QColor(25, 0, 90, 200))
        # qp.drawRect(250, 15, 90, 60)
        qp.drawImage(QRect(0, 0, 300, 300), QImage('./../../../image/anime-girl-3840x2160-4k-5k-19524.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
