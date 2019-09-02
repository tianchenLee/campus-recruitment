# 某鹅厂技术类校招笔试20190901，没AC没标准答案 ==!
# desc：有n个数字，每次可以选择并且同时删除任意两个不同的数字，问最后是否能删完；
# input desc：（！！！存疑：在线ide的input应该是测试用例，所以这些约束应该不需要自己去实现？？）
			# 第一行表示数据的组数；
			# 对于每组数据：第一行一个数n（保证是偶数）表示数字个数，2<n<100000；第二行n个数字，每个数字都小于n；
# output desc: 对于每组数据，输出“yes”或者“NO”表示是否可以删除所有的数字

import sys
def delete(alist):
	i=0
	while len(alist)>i+1:
		if alist[i]==alist[i+1] :
			i+=1
		elif(alist[i]!=alist[i+1]):
			print(alist)
			alist.pop(i)				
			alist.pop(i)
			print(alist)
	if (len(alist)==0):print("YES")
	elif (len(alist)==2):
		if(alist[0]==alist[1]):
			print("NO")
		else:print("YES")
	else:print("NO")


if __name__ == '__main__':
	# li = [2,2,2,2,5,6,9,2,4,7,4,1]
	# # li = [2,2,5,6,9,2,4,7,4,1]
	# delete(li)
	# print(li)	

	# 读取第一行的n
	n = int(sys.stdin.readline().strip())

	li=[]
	# 读取每一组的list
	for i in range(n):
		num=int(sys.stdin.readline().strip())
		line=sys.stdin.readline().strip()
		values = list(map(int, line.split()))
		for v in values:
			li.append(v)
		delete(li)
