
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FridayGUI(object):
    def setupUi(self, FridayGUI):
        FridayGUI.setObjectName("FridayGUI")
        FridayGUI.resize(909, 607)
        self.centralwidget = QtWidgets.QWidget(FridayGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 911, 601))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("friday_UI/blk.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(760, 510, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.start.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.start.setObjectName("start")
        self.end = QtWidgets.QPushButton(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(760, 540, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(10)
        self.end.setFont(font)
        self.end.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.end.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.end.setObjectName("end")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -30, 381, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("friday_UI/only_ball.gif"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 0, 411, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("friday_UI/UI_02.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 500, 201, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("friday_UI/UI_03.gif"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 140, 211, 301))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("friday_UI/graphs.gif"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 450, 321, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("friday_UI/text.gif"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 440, 141, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("friday_UI/location2.gif"))
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        FridayGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(FridayGUI)
        QtCore.QMetaObject.connectSlotsByName(FridayGUI)

    def retranslateUi(self, FridayGUI):
        _translate = QtCore.QCoreApplication.translate
        FridayGUI.setWindowTitle(_translate("FridayGUI", "MainWindow"))
        self.start.setText(_translate("FridayGUI", "START"))
        self.end.setText(_translate("FridayGUI", "END"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FridayGUI = QtWidgets.QMainWindow()
    ui = Ui_FridayGUI()
    ui.setupUi(FridayGUI)
    FridayGUI.show()
    sys.exit(app.exec_())