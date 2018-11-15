from Modeep_gui import * 
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import shutil
from PyQt5.QtMultimedia import *

# ui 업데이트
class Update(PyQt5.QtCore.QThread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.next1.clicked.connect(lambda x: ui.stackedWidget.setCurrentIndex(1))
        self.ui.next2.clicked.connect(lambda x: ui.stackedWidget.setCurrentIndex(2))
        self.ui.next2.clicked.connect(lambda x: self.timer.start(1000))
        self.ui.load1.clicked.connect(lambda x:self.showImg(view1 = True))
        self.ui.load2.clicked.connect(lambda x: self.showImg(view2 = True))
        self.timer = PyQt5.QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.second = 59
        self.red = 0
        self.start()

    def updateTime(self):
        ui.time.setText('00:'+str(self.second))
        ui.time.setStyleSheet('QLabel{color:rgb('+str(self.red)+',0,0)}')
        self.second = self.second-1
        if self.second<31:
            self.red = (31-self.second)*8
        else:
            self.red = 0
        
    def showImg(self, view1 =False, view2 = False):
        fname = PyQt5.QtWidgets.QFileDialog.getOpenFileName()
        if view1:
            # 이미지 파일 보여주기
            self.ui.view1.setPixmap(PyQt5.QtGui.QPixmap(fname[0]))
            # 이미지 파일 복사
            #shutil.copy(fname[0],"images/target/"+fname[0].split('/')[-1])
            shutil.copy(fname[0], "images/targets/target.png")
        if view2:
            # 이미지 파일 보여주기
            self.ui.view2.setPixmap(PyQt5.QtGui.QPixmap(fname[0]))
            # 이미지 파일 복사
            #shutil.copy(fname[0], "images/style/"+fname[0].split('/')[-1])
            shutil.copy(fname[0], "images/styles/style.png")

# 소리 재생
class Sound:

    def __init__(self, ui ,app):
        self.content = PyQt5.QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("resources/computer1.mp3"))
        self.player = PyQt5.QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        ui.next2.clicked.connect(self.player.play)
        app.lastWindowClosed.connect(self.player.stop)


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    update =Update(ui)
    sound = Sound(ui, app)
    sys.exit(app.exec_())