#!/usr/bin/env  python3
# encoding: utf-8

"""
@version: 0.1
@author: shaosu
@license: Apache Licence 
@contact: https://github.com/shaosu
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: P3.py
@time: 16-10-3 下午3:44

练习：
	布局管理,简单的计算器

"""

import sys
from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):
	"""
	布局管理
	"""
	def __init__(self):
		super().__init__()
		self.initui()

	def initui(self):
		okbtn = QPushButton("OK")
		cancelbtn = QPushButton("Cancel")

		hbox = QHBoxLayout()
		hbox.addStretch(1)  # 拉伸因子在两个按钮之前增加了一个可伸缩空间。这会将按钮推到窗口的右边。
		hbox.addWidget(okbtn)
		hbox.addWidget(cancelbtn)

		lab1 = QLabel("show something")
		lab1.setFont(QFont('SansSerif', 16))
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addWidget(lab1)
		vbox.addStretch(1)  # 拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle("窗口布局管理")


class Example2(QWidget):

	def __init__(self):
		super().__init__()
		self.text1 = QLineEdit()
		self.text2 = QLineEdit()
		self.btns = []
		self.L = 1
		self.initui()

	def initui(self):
		grid = QGridLayout()
		self.setLayout(grid)
		names = ['Lab1', '', '', 'Lab2',
				'cls', 'Bck', '( )', 'Close',
				'7', '8', '9', '/',
				'4', '5', '6', '*',
				'1', '2', '3', '-',
				'0', '.', '=', '+']
		positions = [(i, j) for i in range(7) for j in range(4)]
		for position, name in zip(positions, names):
			if name == '':
				continue
			elif name == 'Lab1':

				grid.addWidget(self.text1, *position, 1, 3)
			elif name == 'Lab2':

				grid.addWidget(self.text2, *position, 1, 1)
			else:
				btn = QPushButton(name)

				self.btns.append(btn)
				grid.addWidget(self.btns[-1], *position, 1, 1)

		self.move(300, 150)
		self.setWindowTitle("Calculator")
		for i in range(len(self.btns)):  # Not Ok  --改为sender=self.senfer()后OK
			self.btns[i].clicked.connect(lambda: self.text1_addstr(self.btns[i]))
		# self.btns[0].clicked.connect(lambda: self.text1_addstr(self.btns[0]))
		# self.btns[1].clicked.connect(lambda: self.text1_addstr(self.btns[1]))
		# self.btns[2].clicked.connect(lambda: self.text1_addstr(self.btns[2]))
		# self.btns[3].clicked.connect(lambda: self.text1_addstr(self.btns[3]))
		# self.btns[4].clicked.connect(lambda: self.text1_addstr(self.btns[4]))
		# self.btns[5].clicked.connect(lambda: self.text1_addstr(self.btns[5]))
		# self.btns[6].clicked.connect(lambda: self.text1_addstr(self.btns[6]))
		# self.btns[7].clicked.connect(lambda: self.text1_addstr(self.btns[7]))
		# self.btns[8].clicked.connect(lambda: self.text1_addstr(self.btns[8]))
		# self.btns[9].clicked.connect(lambda: self.text1_addstr(self.btns[9]))
		# self.btns[10].clicked.connect(lambda: self.text1_addstr(self.btns[10]))
		# self.btns[11].clicked.connect(lambda: self.text1_addstr(self.btns[11]))
		# self.btns[12].clicked.connect(lambda: self.text1_addstr(self.btns[12]))
		# self.btns[13].clicked.connect(lambda: self.text1_addstr(self.btns[13]))
		# self.btns[14].clicked.connect(lambda: self.text1_addstr(self.btns[14]))
		# self.btns[15].clicked.connect(lambda: self.text1_addstr(self.btns[15]))
		# self.btns[16].clicked.connect(lambda: self.text1_addstr(self.btns[16]))
		# self.btns[17].clicked.connect(lambda: self.text1_addstr(self.btns[17]))
		# self.btns[18].clicked.connect(lambda: self.text1_addstr(self.btns[18]))
		# self.btns[19].clicked.connect(lambda: self.text1_addstr(self.btns[19]))

	strs = ""

	def text1_addstr(self, tmpbtn):
		sender = self.sender()   # 有时需要方便的知道哪一个组件是信号发送者。因此，PyQt5拥有了sender()方法来解决这个问题。
		print(sender.text())

		if sender.text() == "=":
			rt = eval(self.text1.text())
			Example2.strs = self.text1.text()
			if len(str(rt)) >= 13:
				self.tmp = int(rt)
				self.i = 0
				while self.tmp > 10:
					self.tmp = self.tmp / 10
					self.i = self.i + 1
				if self.i > 13:
					rt = round(rt, 1)
				elif rt < 2:
					rt = round(rt, 11)
				else:
					rt = round(rt, 12-self.i)
				print(str(self.i))

			self.text2.setText(str(rt))
		elif sender.text() == "cls":
			Example2.strs = ""
			self.L = 1
			self.text1.setText(Example2.strs)
		elif sender.text() == "Bck":
			if Example2.strs[-1] == ")":
				self.L = 0
			elif Example2.strs[-1] == "(":
				self.L = 1
			Example2.strs = Example2.strs[0:len(Example2.strs)-1]
			self.text1.setText(Example2.strs)
		elif sender.text() == "Close":
			self.close()
		elif sender.text() == "( )":
			if self.L == 1:
				Example2.strs += "("
				self.L = 0
				self.text1.setText(Example2.strs)
			else:
				Example2.strs += ")"
				self.L = 1
				self.text1.setText(Example2.strs)
		else:
			Example2.strs += sender.text()
			self.text1.setText(Example2.strs)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example2()
	ex.show()
	sys.exit(app.exec_())
	pass
