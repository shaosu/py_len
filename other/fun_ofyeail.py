#!/usr/bin/env  python3
# encoding: utf-8

"""
@version: 0.1
@author: shaosu
@license: Apache Licence 
@contact: https://github.com/shaosu
@site: http://www.baidu.com
@software: PyCharm Community Edition
@file: fun_ofyeail.py.py
@time: 16-9-11 下午10:13
"""


class Fibs:
	def __init__(self, maxval=0xffffffffffff, num=200):
		self.a = 0
		self.b = 1
		self.count = 0
		self.num = num
		self.max = maxval

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.max or self.count > self.num:
			raise StopIteration
		else:
			self.count += 1
			return self.a


def fun1():
	i = 0
	v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	while i < len(v):
		yield v[i]
		i += 1
	raise StopIteration


def g(n):  # 生成器
	for i in range(n):
		try:
			yield i**2
		except StopIteration:
			break


def print_foreach(items, fmat='d'):
	if fmat == 'd':
		for i in items:
			print(i)
	if fmat in ['x', 'X']:
		for i in items:
			print("0x%X,%d" % (i, i))
	if fmat in ['o', 'O']:
		for i in items:
			print("0%o,%d" % (i, i))
	if fmat in ['b', 'B']:
		for i in items:
			print(bin(i) + " ," + str(i))


if __name__ == '__main__':
	rt = g(2)
	try:
		print(next(rt))
		print(next(rt))
		print(next(rt))
		print(next(rt))
	except StopIteration:
		print("End rt")
	rt = fun1()
	next(rt)
	for i in rt:
		print(i)
	e = (i for i in range(100) if i % 10 == 0)
	print(next(e))
	print(next(e))
	print(next(e))

	f = Fibs(1000000, 5)
	print_foreach(f, 'b')
	f2 = lambda x: x*x
	print(f2(f2(2)))
	f3 = list()
	f3.append(22)
	f3.append(33)
	f3.append(44)
	print(f3.pop())
	print(f3.pop())
	qq = [1, 2, 8]
	qq1 = iter(qq)
	print(next(qq1))
	pass
