import sys
from client.qt.MusicListView import MusicListView
from PyQt5.QtWidgets import QApplication
from client.qt.MusicDataManager import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MusicListView()
    win.showContent(getMusicsName())
    sys.exit(app.exec_())
