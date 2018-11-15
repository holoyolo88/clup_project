# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modeep_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 749)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(140, 10, 891, 731))
        self.stackedWidget.setStyleSheet("background-color:transparent")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(160, 90, 441, 71))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.next1 = QtWidgets.QPushButton(self.page)
        self.next1.setGeometry(QtCore.QRect(700, 660, 151, 51))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(16)
        font.setUnderline(True)
        self.next1.setFont(font)
        self.next1.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"border: 2px solid white;\n"
"border-radius :4px;\n"
"color:white;\n"
"")
        self.next1.setObjectName("next1")
        self.load1 = QtWidgets.QPushButton(self.page)
        self.load1.setGeometry(QtCore.QRect(540, 660, 141, 51))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(16)
        font.setUnderline(True)
        self.load1.setFont(font)
        self.load1.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"border: 2px solid white;\n"
"border-radius :4px;\n"
"color:white;\n"
"")
        self.load1.setObjectName("load1")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.page)
        self.graphicsView_3.setGeometry(QtCore.QRect(0, 570, 151, 151))
        self.graphicsView_3.setStyleSheet("border:transparent;\n"
"background:url(:/img/resources/thinking.jpg)")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.view1 = QtWidgets.QLabel(self.page)
        self.view1.setGeometry(QtCore.QRect(10, 220, 841, 421))
        self.view1.setStyleSheet("background-color:white;border:1px solid grey")
        self.view1.setText("")
        self.view1.setObjectName("view1")
        self.label.raise_()
        self.next1.raise_()
        self.load1.raise_()
        self.view1.raise_()
        self.graphicsView_3.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 561, 71))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:black")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.next2 = QtWidgets.QPushButton(self.page_2)
        self.next2.setGeometry(QtCore.QRect(700, 660, 151, 51))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(16)
        font.setUnderline(True)
        self.next2.setFont(font)
        self.next2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"border: 2px solid white;\n"
"border-radius :4px;\n"
"color:white;\n"
"")
        self.next2.setObjectName("next2")
        self.load2 = QtWidgets.QPushButton(self.page_2)
        self.load2.setGeometry(QtCore.QRect(540, 660, 141, 51))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(16)
        font.setUnderline(True)
        self.load2.setFont(font)
        self.load2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"border: 2px solid white;\n"
"border-radius :4px;\n"
"color:white;\n"
"")
        self.load2.setObjectName("load2")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.page_2)
        self.graphicsView_5.setGeometry(QtCore.QRect(670, 100, 101, 21))
        self.graphicsView_5.setStyleSheet("border:transparent;\n"
"background:url(:/img/resources/thug.png)")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 610, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(64)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.view2 = QtWidgets.QLabel(self.page_2)
        self.view2.setGeometry(QtCore.QRect(10, 220, 841, 421))
        self.view2.setStyleSheet("background-color:white;border:1px solid grey")
        self.view2.setText("")
        self.view2.setObjectName("view2")
        self.view2.raise_()
        self.label_2.raise_()
        self.next2.raise_()
        self.load2.raise_()
        self.graphicsView_5.raise_()
        self.label_3.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.time = QtWidgets.QLabel(self.page_3)
        self.time.setGeometry(QtCore.QRect(120, 300, 431, 191))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 ExtraBold")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView_7.setGeometry(QtCore.QRect(90, 70, 501, 611))
        self.graphicsView_7.setStyleSheet("border:transparent;\n"
"background:url(:/img/resources/lines.png)")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView.setGeometry(QtCore.QRect(140, 230, 711, 421))
        self.graphicsView.setStyleSheet("background:url(:/img/resources/brain.jpg);\n"
"border:transparent\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView_8.setGeometry(QtCore.QRect(670, 100, 101, 21))
        self.graphicsView_8.setStyleSheet("border:transparent;\n"
"background:url(:/img/resources/thug.png)")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.page_3)
        self.graphicsView_9.setGeometry(QtCore.QRect(680, 500, 201, 61))
        self.graphicsView_9.setStyleSheet("border:transparent;\n"
"background:url(:/img/resources/thug.png)")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.graphicsView.raise_()
        self.graphicsView_7.raise_()
        self.time.raise_()
        self.graphicsView_8.raise_()
        self.graphicsView_9.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 30, 241, 241))
        self.graphicsView_2.setStyleSheet("background:url(:/img/resources/bonoHI.png);\n"
"border:transparent\n"
"")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(960, 430, 141, 241))
        font = QtGui.QFont()
        font.setFamily("새굴림")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:transparent")
        self.label_4.setObjectName("label_4")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(750, 60, 241, 151))
        self.graphicsView_6.setStyleSheet("background:url(:/img/resources/images.jpeg);\n"
"border:transparent\n"
"")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_6.raise_()
        self.stackedWidget.raise_()
        self.label_4.raise_()
        self.graphicsView_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "*~ 사진선 택 ~*"))
        self.next1.setText(_translate("MainWindow", "다음 단계"))
        self.load1.setText(_translate("MainWindow", "불러 오기"))
        self.label_2.setText(_translate("MainWindow", "*~ 사진선택 ~*"))
        self.next2.setText(_translate("MainWindow", "다음 단계"))
        self.load2.setText(_translate("MainWindow", "불러 오기"))
        self.label_3.setText(_translate("MainWindow", "MoDeep"))
        self.time.setText(_translate("MainWindow", " 1:00"))
        self.label_4.setText(_translate("MainWindow", "⊂_? \n"
"　 ＼＼  Λ＿Λ \n"
"　　 ＼ (\'ㅅ\')  두둠칫 \n"
"　　　 >　⌒? \n"
"　　　/ 　 へ＼ \n"
"　　 /　　/　＼＼ \n"
"　　 ?　ノ　　 ?_つ \n"
"　　/　/ 두둠칫 \n"
"　 /　/| \n"
"　(　(? \n"
"　|　|、＼ \n"
"　| ? ＼ ⌒) \n"
"　| |　　) / \n"
"(`ノ"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

