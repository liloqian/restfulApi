import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from client.qt.music.MusicDataManager import getMusicsName
from client.qt.music.MusicListView import MusicListView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MusicListView()
    win.showContent(getMusicsName())
    sys.exit(app.exec_())
    # app = QApplication(sys.argv)
    # player = QMediaPlayer()
    # vw = QVideoWidget()  # 定义视频显示的widget
    # vw.show()
    # player.setVideoOutput(vw)  # 视频播放输出的widget，就是上面定义的
    # player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
    # player.play()  # 播放视频
    # sys.exit(app.exec_())
