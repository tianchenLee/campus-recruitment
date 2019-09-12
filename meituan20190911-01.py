# 将一个正整数N分解成几个正整数相加，可以有多种分解方法，例如7=6+1，7=5+2，7=5+1+1，…。编程求出正整数N的所有整数分解式子。

# 输入格式：

# 每个输入包含一个测试用例，即正整数N (0 < N ≤ 30)。

# 输出格式：

# 按递增顺序输出N的所有整数分解式子。递增顺序是指：对于两个分解序列 N1=n1,n2,⋯ 和 N2=m1,m2,⋯，若存在 i 使得 n1=m1, ⋯ , ni=mi，但是 ni+1<mi+1，则 N1 序列必定在 N2 序列之前输出。每个式子由小到大相加，式子间用分号隔开，且每输出 4 个式子后换行。

# def partition(n, search_start=1, res=[]):


# 	 for i in range(search_start, n + 1):
# 		 if n == i:
# 			 print(*res, n)
# 			 return
# 		 if n < i:
# 			 return


# 		 partition(n - i, search_start=i, res=res + [i])


# partition(9)


# n = 3
# def partition(part_sum=0, search_start=1, res=[]):
# 	count=1
# 	for i in range(search_start, n + 1):
# 		part_sum += i
# 		res.append(i)
# 		if part_sum == n:
# 			print(res)
# 		elif part_sum < n:
# 			# print(res)
# 			partition(part_sum, search_start=i, res=res)
# 	# 如果i进入res之后，列表内元素之和并不等于n，则将该元素弹出
# 		part_sum -= i

# 		# 显然时间复杂度是n2，因为其执行过程是先算n=n个1,然后从队尾pop出1，再加上2，3，4...，依次判断这些不符合再pop出倒数第2个1，再一次加上2，3...所以时间复杂度n2
# 		# print("res变化情况测试   {}".format(res))
# 		res.pop()
		
# partition()




n = 5
def partition(part_sum=0, search_start=1, res=[]):
	count=1
	for i in range(search_start, n + 1):
		part_sum += i
		res.append(i)
		if part_sum == n:
			print(res,end=",\n")
			# print(len(res))
		elif part_sum < n:
			# print(res)
			partition(part_sum, search_start=i, res=res)
	# 如果i进入res之后，列表内元素之和并不等于n，则将该元素弹出
		part_sum -= i
		# 显然时间复杂度是n2，因为其执行过程是先算n=n个1,然后从队尾pop出1，再加上2，3，4...，依次判断这些不符合再pop出倒数第2个1，再一次加上2，3...所以时间复杂度n2
		# print("res变化情况测试   {}".format(res))
		res.pop()
	# print("res变化情况测试   {}".format(res))
		
print(partition())