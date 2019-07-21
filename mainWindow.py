# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import time

from PyQt5.QtCore import QTimer


class MyWindow(QtWidgets.QWidget):
    timerc = 0
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("窗口中的时钟")
        self.resize(200, 100)
        self.timer_id = 0
        self.label = QtWidgets.QLabel("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button1 = QtWidgets.QPushButton("开始")
        self.button2 = QtWidgets.QPushButton("停止")
        self.button2.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        self.timer.start(2000)  # 设置计时间隔并启动
        #self.setWindowOpacity(0.5)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def operate(self):
        MyWindow.timerc +=1
        print("1122132323+::: %d" % MyWindow.timerc)
        if MyWindow.timerc == 3:
           self.close()

    def on_clicked_button1(self):
        self.timer_id = self.startTimer(10, timerType = QtCore.Qt.VeryCoarseTimer)
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def on_clicked_button2(self):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = 0
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

    def timerEvent(self, event):
        self.label.setText(time.strftime("%H:%M:%S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())