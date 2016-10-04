#!/usr/bin/env  python3
# encoding: utf-8

"""
@version: 0.1
@author: shaosu
@license: Apache Licence 
@contact: https://github.com/shaosu
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: P4.py
@time: 16-10-3 下午7:30

练习：
	信号,和槽
	输入对话框,


"""

import os
import sys

from PyQt5.QtCore import Qt, QEvent, QBasicTimer
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPalette, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox, QStatusBar, qApp, QMenuBar, QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog, QAction, QTextEdit, QProgressBar
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QPushButton, QColorDialog, QFontDialog
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout


class Communicate(QObject):
	"""
	信号　
	新的信号叫做closeApp。当触发鼠标点击事件时信号会被发射。
	信号连接到了QWidget的close()方法。
	"""
	# noinspection PyArgumentList
	closeApp = pyqtSignal()


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.path = os.getcwd()
		self.lcd = QLCDNumber(self)
		self.lcd.setStyleSheet("color:red")
		self.sld = QSlider(Qt.Horizontal, self)
		self.sld.setMaximum(1000)
		self.btn_dlg = QPushButton("Dialog", self)
		self.btn_color = QPushButton("Color", self)
		self.btn_font = QPushButton('Font', self)
		self.btn_file = QPushButton('File', self)
		self.btn_save = QPushButton('Save', self)
		self.editbox = QLineEdit()
		self.editbox.setStyleSheet("color:green;")
		self.textbox = QTextEdit()
		self.chbox = QCheckBox("QCheckBox", self)
		self.btn_red = QPushButton('Red', self)
		self.btn_red.setCheckable(True)  # 特殊模式
		self.btn_red.setStyleSheet("color:green;")

		self.btn_red.clicked[bool].connect(self.setselfcolor)  # 相当于两个按钮

		self.pbar = QProgressBar(self)
		self.step = 0
		self.timer = QBasicTimer()

		self.bmp = QPixmap('web.png')
		self.pixbox = QLabel(self)
		self.pixbox.setPixmap(self.bmp)

		self.combox = QComboBox(self)
		self.combox.addItem("Ubtntu")
		self.combox.addItem("Lubuntu")
		self.combox.addItem("Xubuntu")
		self.combox.activated[str].connect(self.oncomchaged)

		self.vt = QVBoxLayout()
		self.ht = QHBoxLayout()
		self.vbox = QVBoxLayout()
		self.hbox = QHBoxLayout()
		self.bar_st = QStatusBar()
		self.bar_menu = QMenuBar()
		self.vbox2 = QVBoxLayout()

		self.openAction = QAction(QIcon('web.png'), '&Open', self)
		self.saveAction = QAction(QIcon('web.png'), '&Save', self)
		self.quitAction = QAction(QIcon('web.png'), '&Quit', self)

		self.filemenu = self.bar_menu.addMenu('File(&F)')

		# self.textbox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
		# self.textbox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
		self.setlcdvalue(22)
		self.palette = QPalette()  # 调色版
		self.palette.setColor(QPalette.Text, Qt.red)
		self.textbox.setPalette(self.palette)
		self.c = Communicate()
		self.c.closeApp.connect(self.close)  # 把自定义的closeApp信号连接到QWidget的close()槽上
		self.initui()
		# self.setStyleSheet('''background-color:green;''')
		pass

	def mousePressEvent(self, qmouseevent):
		# button() == QtCore.Qt.LeftButton
		if qmouseevent.button() == Qt.RightButton:
			self.c.closeApp.emit()  # 当我们在窗口上点击一下鼠标,closeApp信号会被发射。

	def initui(self):
		self.hbox.addWidget(self.btn_file, 1)
		self.hbox.addWidget(self.btn_dlg, 1)
		self.hbox.addWidget(self.editbox, 333)
		self.hbox.addWidget(self.btn_color, 1)
		self.hbox.addWidget(self.btn_font, 1)
		# hbox.addWidget(self.btn_save)
		self.vbox.addLayout(self.hbox)
		self.vbox.addWidget(self.textbox, 8)
		self.vbox.addWidget(self.lcd, 1)
		self.vbox.addWidget(self.sld, 1)

		self.vbox2.addWidget(self.btn_save)
		self.vbox2.addStretch(1)
		self.ht.addLayout(self.vbox, 65)
		self.ht.addLayout(self.vbox2, 1)

		self.openAction.setShortcut("Ctrl+O")
		self.saveAction.setShortcut("Ctrl+S")
		self.quitAction.setShortcut("Ctrl+Q")
		self.openAction.setStatusTip("Open an fiel")
		self.saveAction.setStatusTip("Save the fiel")
		self.quitAction.setStatusTip("Exit This PG")
		self.quitAction.triggered.connect(qApp.quit)
		self.openAction.triggered.connect(self.showfiledlg)
		self.saveAction.triggered.connect(self.showsavefiledlg)
		self.openAction.showStatusText(self.bar_st)
		self.chbox.stateChanged.connect(self.changestate)

		self.filemenu.addAction(self.openAction)
		self.filemenu.addAction(self.saveAction)
		self.filemenu.addAction(self.quitAction)
		self.vt.addWidget(self.bar_menu)
		self.vt.addLayout(self.ht)

		self.vbox2.addWidget(self.chbox)
		self.vbox2.addWidget(self.btn_red)
		# self.vbox2.addWidget(self.timer)
		self.vbox2.addWidget(self.pbar)
		self.vbox2.addWidget(self.pixbox)
		self.vbox2.addWidget(self.combox)

		self.vt.addWidget(self.bar_st)
		self.bar_st.showMessage("Good")
		self.setLayout(self.vt)
		self.sld.valueChanged.connect(self.lcd.display)
		self.btn_dlg.clicked.connect(self.showdialog)
		self.btn_color.clicked.connect(self.showcolordlg)
		self.btn_font.clicked.connect(self.showfontdlg)
		self.btn_file.clicked.connect(self.showfiledlg)
		self.btn_save.clicked.connect(self.showsavefiledlg)

		self.setGeometry(200, 200, 800, 500)
		self.setWindowTitle("Singnal & slot Len")

	def timerEvent(self, qtimerevent):
		if self.step >= 100:
			self.timer.stop()
			self.btn_red.setStyleSheet("color:green;")
			self.bar_st.showMessage("Timer Is Stop")
			self.step = 0
			return
		self.step = self.step + 1
		self.pbar.setValue(self.step)

	def oncomchaged(self, text):
		self.bar_st.showMessage(text)

	def doaction(self):
		if self.timer.isActive():
			self.timer.stop()
		else:
			self.timer.start(500, self)  # 500ms

	def changestate(self, state):
		if state == Qt.Checked:
			self.bar_st.showMessage("Chacked")
		else:
			self.bar_st.showMessage("No Chacked")

	def setselfcolor(self, pa):
		sou = self.sender()
		if sou.text() == "Red":
			self.doaction()
			if pa:
				self.btn_red.setStyleSheet("color:red;")
			else:
				self.btn_red.setStyleSheet("color:green;")

	def eventFilter(self, source, event):
		sender = self.sender()
		if event.type() == QEvent.MouseMove:
			if event.buttons() == Qt.NoButton:
				pos = event.pos()
				self.bar_st.showMessage('x:%d, y:%d' % (pos.x(), pos.y()))
			else:
				pass  # do other stuff
		elif event.type() == QEvent.FocusIn:
			# print("int")
			pass
		return QWidget.eventFilter(self, source, event)

	def showdialog(self):
		# noinspection PyCallByClass,PyTypeChecker
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name: ')

		if ok:
			self.editbox.setText(str(text))

	def showcolordlg(self):
		col = QColorDialog.getColor()
		# col = QColor(22, 33, 44)
		print(col.red())
		print(col.green())
		print(col.blue())
		if col.isValid():
			# self.setStyleSheet('''background-color:%s''' % col.name())  # CCS写法
			# self.setStyleSheet('''QWidget{background-color:%s};''' % col.name())
			# self.editbox.setStyleSheet('''background-color:%s''' % col.name())
			self.editbox.setStyleSheet('''color:%s''' % col.name())

	def showfontdlg(self):
		# noinspection PyArgumentList
		font, ok = QFontDialog.getFont()
		assert isinstance(ok, bool)
		# print(ok)
		if ok:
			self.editbox.setFont(font)

	def showfiledlg(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/lei')
		assert isinstance(fname, str)
		if not fname[0] is None:  # fname[0]
			f = open(fname[0], 'r')
			with f:
				data = f.read()
				self.textbox.setText(data)
			f.close()

	def showsavefiledlg(self):
		# noinspection PyTypeChecker
		fname, ok = QFileDialog.getSaveFileName(self, "保存文件", "/home/lei", "Text Files(*.txt);;All File(*)")
		print(self.path)
		# print(fname)  # 文件名
		# print(ok)  # 文件类型
		if fname:
			f = open(fname, 'w')
			# self.textbox.toPlainText() # 无格式文本
			f.write(self.textbox.toPlainText())
			f.close()

	def setlcdvalue(self, n):
		self.lcd.display(n)

	def keyPressEvent(self, qkeyevent):
		if qkeyevent.key() == Qt.Key_Escape:
			self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	app.installEventFilter(ex)
	sys.exit(app.exec_())
	pass
