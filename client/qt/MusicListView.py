from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel


class MusicListView(QWidget):

    listView = None

    def __init__(self, parent=None):
        super(MusicListView, self).__init__(parent)
        self.setWindowTitle("Music详情页")
        self.resize(400, 600)
        layout = QVBoxLayout()
        self.listView = QListView()
        self.listView.clicked.connect(self.clickedList)
        layout.addWidget(self.listView)
        self.setLayout(layout)

    def showContent(self, music):
        stringListMode = QStringListModel()
        stringListMode.setStringList(music)
        self.listView.setModel(stringListMode)
        self.show()

    def clickedList(self, qModelIndex):
        # QMessageBox.information(self, "QListView", "你选择了: " + self.qList[qModelIndex.row()])
        print("点击的是：" + str(qModelIndex.row()))
