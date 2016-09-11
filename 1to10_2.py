#!/usr/bin/env  python3
# encoding: utf-8
import itertools

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = []
list2 = []


def fun_getall():
	"""
	得到所有成立列表排列组合
	:return:
	"""
	for i in itertools.permutations(v, 10):
		list1.append(i)
	for t in list1:
		a = t[0]+t[1]+t[2]
		b = t[3]+t[4]+t[5]
		c = t[6]+t[7]
		d = t[8]+t[9]
		if a*d == c*b:
			list2.append(t)


def my_print(t):
	print("(%d+%d+%d)/(%d+%d+%d)=(%d+%d)/(%d+%d)" %(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]), end='')


def fun_getid(lsls):
	listrt = []
	for i in range(0, len(lsls)):
		ls = lsls[i]
		a = ls[0]+ls[1]+ls[2]  # 有无都一样
		b = ls[3]+ls[4]+ls[5]  # 有无都一样

		tl = [ls[0]*ls[1]*ls[2], ls[3]*ls[4]*ls[5], ls[6]*ls[7], ls[8]*ls[9]]  # , a, b]
		listrt.append(tl)
	return listrt


def l_eq_l_len_eq(l1, l2):  # 相等
	if not(len(l1) == len(l2)):
		return False
	for i in range(0, len(l1)):
		if l1[i] == l2[i]:
			pass
		else:
			return False
	return True


def get_rt(l_id):
	list_rt = []
	tmp = l_id[0]
	j = 1
	j = 1
	xt = 1
	for i in range(0, len(l_id)):
		f = 1
		new = 0
		tmp = l_id[i]
		for j in range(0, len(l_id)):
			if not(i == j):
				if l_eq_l_len_eq(tmp, l_id[j]):
					xt += 1
					f = 0
					l_id[i].append("1")
					# break  　# 不统计
				else:
					pass

		if f == 1:
			list_rt.append([i, xt])
			xt = 1
	return list_rt


if __name__ == '__main__':
	fun_getall()
	print("1 to 10 in a to j  (a+b+c)/(d+e+f)=(g+h)/(i+j)")
	lid = fun_getid(list2)
	rt = get_rt(lid)
	s = 0
	for i in range(0, len(rt)):
		tt=rt[i]
		myrt=list2[tt[0]]
		my_print(myrt)
		s = s + tt[1]
		print("  相同个数:"+str(tt[1]))

	print(" "*28 + "  相加结果:"+str(s))
	print("重复总数:" + str(len(list2)))
	print("不重复总数:"+str(len(rt)))

	pass
