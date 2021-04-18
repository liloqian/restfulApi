import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QTextEdit, QLineEdit


class FixLayout(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Java', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('Kotlin', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Python', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


class LinearLayout(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        # 支持自动伸展
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        okButton2 = QPushButton("OK")
        cancelButton2 = QPushButton("Cancel")
        hbox2 = QHBoxLayout()
        hbox2.addWidget(okButton2)
        hbox2.addWidget(cancelButton2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


class GridLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # grid = QGridLayout()
        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #          '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #          '0', '.', '=', '+']
        # positions = [(i, j) for i in range(5) for j in range(4)]
        # for position, name in zip(positions, names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridLayout()
    sys.exit(app.exec_())
