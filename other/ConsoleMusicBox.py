#!/usr/bin/python2
# encoding: utf-8

"""
@version: 0.1
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: ConsoleMusicBox.py.py
@time: 16-5-28 上午12:46
"""

import  sys
from pkg_resources import  load_entry_point

class Main():
	def __init__(self):
		pass


if __name__ == '__main__':
	sys.exit(load_entry_point('NetEase-MusicBox==0.2.2.10', 'console_scripts', 'musicbox')()
			 )
	pass