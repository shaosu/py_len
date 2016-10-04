#!/usr/bin/env  python3
# encoding: utf-8

"""
@version: 0.1
@author: shaosu
@license: Apache Licence 
@contact: https://github.com/shaosu
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: P2.py
@time: 16-10-3 下午2:30

练习：
	工具栏,菜单栏，状态栏，中心组件

"""
import sys
import PyQt5_len.P1 as p1
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTextEdit


class Exanple(QMainWindow, p1.Example):
	def __init__(self):
		# super(QMainWindow, self).__init__()
		# super(p1.Example, self).__init__() # Not Ok
		super().__init__()  # OK
		self.add_statusbar()
		self.add_menubar()
		self.add_toolbar()
		self.add_textedit()

	def add_statusbar(self):
		"""
		状态栏
		:return:
		"""
		self.statusBar().showMessage('Ready')

	def add_menubar(self):
		"""
		菜单栏
		QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为。
		menuBar()方法创建了一个菜单栏。我们创建一个file菜单，然后将退出动作添加到File菜单中。
		:return:
		"""
		exitAction = QAction(QIcon('web.png'), '退出(&E)', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(qApp.quit)  # triggered:触发器

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('文件(&F)')
		fileMenu.addAction(exitAction)

	def add_toolbar(self):
		exac = QAction(QIcon('web.png'), 'Exit', self)
		exac.setShortcut('Ctrl+Q')
		exac.setStatusTip('Exit Application')
		exac.triggered.connect(qApp.quit)

		self.toobar = self.addToolBar('Exit')
		self.toobar.addAction(exac)

	def add_textedit(self):
		"""
		创建了一个文本编辑框组件。我们将它设置成QMainWindow的中心组件。
		中心组件占据了所有剩下的空间
		:return:
		"""
		textedit = QTextEdit()
		self.setCentralWidget(textedit)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Exanple()
	ex.show()
	sys.exit(app.exec_())
	pass
