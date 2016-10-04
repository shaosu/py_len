#!/usr/bin/env  python3
# encoding: utf-8

"""
@version: 0.1
@author: shaosu
@license: Apache Licence 
@contact: https://github.com/shaosu
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: P1.py
@time: 16-10-3 下午1:13

练习：
	窗体，按钮，气泡提示，初识信号/槽，MessageBox

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget


class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initui()

	def initui(self):
		"""
		初始化界面
		:return:
		"""
		self.setGeometry(300, 300, 600, 400)  # (x,y,w,h)
		self.setWindowTitle("My First")
		self.setWindowIcon(QIcon('web.png'))
		self.center()  # 窗口居中

		QToolTip.setFont(QFont('SansSerif',12))
		self.setToolTip('This is a <b>Qwidget</b> widget')
		btn = QPushButton('Button1', self)
		btn.setToolTip('This is a <b>QpushButton</b> widget')
		btn.resize(btn.sizeHint())  # setHint()方法给了按钮一个推荐的大小。
		btn.move(100, 100)
		self.add_exitbtn()  # add quit btn


	def add_exitbtn(self):
		"""
		在PyQt5中，事件处理系统由信号&槽机制建立。如果我们点击了按钮，信号clicked被发送。
		槽可以是Qt内置的槽或Python 的一个方法调用。
		instance()方法给我们返回一个实例化对象.
		QCoreApplication类包含了主事件循环；它处理和转发所有事件
		事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。
		:return:
		"""
		qbtn = QPushButton('Quit', self)

		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(510, 350)

	def closeEvent(self, QCloseEvent):
		"""
		重载关闭事件，只能是右/左上角默认的关闭按钮
		:param QCloseEvent:
		:return:
		"""
		reply = QMessageBox.question(self, 'Message',
									"Are you sure to qiut? ",
									QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())
	pass





