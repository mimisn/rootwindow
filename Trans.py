# -*- coding: utf-8 -*-
import random
import sys
from PyQt5 import QtCore, QtWidgets
import time

from PyQt5.QtCore import QTimer, QDateTime, Qt, pyqtSignal, pyqtSlot, QRect
from PyQt5.QtGui import QPalette, QFont, QValidator, QIntValidator
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QFormLayout, QLabel, QLineEdit, QDateTimeEdit, QVBoxLayout


class DisplayWindow(QtWidgets.QWidget):
    mySignaldata = pyqtSignal(list, int)

    Countdown = 5
    data = ["没有值", ]
    dataLen = 0
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.hlayout = QVBoxLayout() # 局部布局（4个）：水平、竖直、网格、表单
        self.vlayout = QVBoxLayout()
        self.flayout = QFormLayout()

        self.label12 = QLabel("窗口将在%d秒后自动关闭" % DisplayWindow.Countdown)
        self.label12.setAlignment(Qt.AlignCenter)
        self.flayout.addWidget(self.label12)


        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("没有值")
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)
        self.label.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window, Qt.blue)
        #pe.setColor(QPalette.Background,Qt.blue)
        self.label.setPalette(pe)
        self.label.setFont(QFont("Roman times", 30, QFont.Bold))
        self.vlayout.addWidget(self.label, Qt.AlignJustify)
        self.label.adjustSize()
        self.label.setGeometry(QRect(328,240,329,27*4))
        self.label.setWordWrap(True)


        self.vwg = QtWidgets.QWidget()
        self.fwg = QtWidgets.QWidget()

        self.vwg.setLayout(self.vlayout)
        self.fwg.setLayout(self.flayout)

        self.hlayout.addWidget(self.fwg)
        self.hlayout.addWidget(self.vwg)

        self.setLayout(self.hlayout)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法


        #self.setCentralWidget(self.label)
        self.setWindowOpacity(0.7)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)

    def operate(self):
        DisplayWindow.Countdown -=1
        self.label12.setText("窗口将在%d秒后自动关闭" % DisplayWindow.Countdown)
        if DisplayWindow.Countdown == 0:
            self.timer.stop()
            server = MyWindow.callBcak()
            server.setService()
            self.close()



    def getMySignaldata(self, data, displayTime):
        if not data:
            DisplayWindow.data.append("没有值")
        else:
            DisplayWindow.data = data
        DisplayWindow.dataLen = len(DisplayWindow.data)
        if displayTime == 0 :
            DisplayWindow.Countdown = 5
        else:
            DisplayWindow.Countdown = displayTime
        self.label12.setText("窗口将在%d秒后自动关闭" % DisplayWindow.Countdown)
        index = random.randint(0, DisplayWindow.dataLen-1)
        self.label.setText(DisplayWindow.data[index])
        self.timer.start(1000)
        if not self.isVisible():
            self.showFullScreen()


class MyWindow(QtWidgets.QWidget):
    mySendSignaldata = pyqtSignal(list, int)
    server = ''
    Countdown = 30
    def __init__(self, display, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        MyWindow.server = self
        self.defauTimer =30
        self.defauLockScreenTime = 5
        self.lineEditList = []
        self.setWindowTitle("单词录入窗口")
        self.resize(400, 300)
        self.formLayout = QFormLayout()
        self.anthorWindow = display


        self.lab1 = QLabel("单词1")
        self.lineEdit1 = QLineEdit()
        self.lineEditList.append(self.lineEdit1)

        self.lab2 = QLabel("单词2")
        self.lineEdit2 = QLineEdit()
        self.lineEditList.append(self.lineEdit2)

        self.lab3 = QLabel("单词3")
        self.lineEdit3 = QLineEdit()
        self.lineEditList.append(self.lineEdit3)

        self.lab4 = QLabel("单词4")
        self.lineEdit4 = QLineEdit()
        self.lineEditList.append(self.lineEdit4)

        self.lab5 = QLabel("单词5")
        self.lineEdit5 = QLineEdit()
        self.lineEditList.append(self.lineEdit5)

        self.lab6 = QLabel("单词6")
        self.lineEdit6 = QLineEdit()
        self.lineEditList.append(self.lineEdit6)

        self.lab7 = QLabel("单词7")
        self.lineEdit7 = QLineEdit()
        self.lineEditList.append(self.lineEdit7)

        self.lab8 = QLabel("单词8")
        self.lineEdit8 = QLineEdit()
        self.lineEditList.append(self.lineEdit8)

        self.lab9 = QLabel("单词9")
        self.lineEdit9 = QLineEdit()
        self.lineEditList.append(self.lineEdit9)

        self.lab10 = QLabel("单词10")
        self.lineEdit10 = QLineEdit()
        self.lineEditList.append(self.lineEdit10)

        self.lab11 = QLabel("显示间隔时间")
        self.lineEdit11 = QLineEdit()
        self.lineEdit11.setValidator(QIntValidator())

        self.lab14 = QLabel("锁屏时间")
        self.lineEdit15 = QLineEdit()
        self.lineEdit15.setValidator(QIntValidator())

        self.dispalyTime = self.defauTimer
        self.LockScreenTime = self.defauLockScreenTime

        self.lab12 = QLabel("倒计时")
        self.lab13 = QLabel("下一个单词显示还有%s秒" % str(self.dispalyTime))

        self.button1 = QPushButton("开始")
        self.button2 = QPushButton("停止")
        self.button2.setEnabled(False)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        self.mySendSignaldata.connect(self.anthorWindow.getMySignaldata)



        # 向布局中添加这几个控件
        # 一行两个控件，水平摆放
        self.formLayout.addRow(self.lab1, self.lineEdit1)
        self.formLayout.addRow(self.lab2, self.lineEdit2)
        self.formLayout.addRow(self.lab3, self.lineEdit3)
        self.formLayout.addRow(self.lab4, self.lineEdit4)
        self.formLayout.addRow(self.lab5, self.lineEdit5)
        self.formLayout.addRow(self.lab6, self.lineEdit6)
        self.formLayout.addRow(self.lab7, self.lineEdit7)
        self.formLayout.addRow(self.lab8, self.lineEdit8)
        self.formLayout.addRow(self.lab9, self.lineEdit9)
        self.formLayout.addRow(self.lab10, self.lineEdit10)
        self.formLayout.addRow(self.lab11, self.lineEdit11)
        self.formLayout.addRow(self.lab14, self.lineEdit15)
        self.formLayout.addRow(self.lab12, self.lab13)
        self.formLayout.addRow(self.button1, self.button2)

        self.setLayout(self.formLayout)

    @classmethod
    def callBcak(self):
        return MyWindow.server

    def setService(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)
        self.setDisplayTime()
        self.lab13.setText("下一个单词显示还有%s秒" % str(self.dispalyTime))
        self.timer.start(1000)  # 设置计时间隔并启动


    def setLockScreenTime(self):
        if self.lineEdit15.text() != '' and len(self.lineEdit15.text()) != 0:
            self.LockScreenTime = int(self.lineEdit15.text())
        else:
            self.LockScreenTime = self.defauLockScreenTime

    def setDisplayTime(self):
        if self.lineEdit11.text() != '' and len(self.lineEdit11.text()) != 0:
            self.dispalyTime = int(self.lineEdit11.text())
        else:
            self.dispalyTime = self.defauTimer

    def on_clicked_button1(self):
        self.setDisplayTime()
        self.lab13.setText("下一个单词显示还有%s秒" % str(self.dispalyTime))
        self.timer.start(1000)  # 设置计时间隔并启动
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)
    def on_clicked_button2(self):
        self.setDisplayTime()
        self.lab13.setText("下一个单词显示还有%s秒" % str(self.dispalyTime))
        self.timer.stop()
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def operate(self):
        data = []
        self.dispalyTime -=1
        for i in self.lineEditList:
            if i.text().strip() != '' and len(i.text()) != 0:
                data.append(i.text())
        self.lab13.setText("下一个单词显示还有%s秒" % str(self.dispalyTime))
        if self.dispalyTime == 0:
            self.setDisplayTime()
            self.setLockScreenTime()
            self.timer.stop()
            self.button1.setEnabled(True)
            self.button2.setEnabled(False)
            self.mySendSignaldata.emit(data, self.LockScreenTime)






if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    display = DisplayWindow()
    window = MyWindow(display)
    window.show()
    sys.exit(app.exec_())