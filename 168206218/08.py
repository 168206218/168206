def find_thief(alist):
	# 遍历每个人
	for each in alist:
		# 每次假设一个人是小偷
		thief = each

		# A说真话的情况
		A = (thief != alist[0])

		# B说真话的情况
		B = (thief == alist[3])

		# C说真话的情况
		C = (thief == alist[1])

		# D说真话的情况
		D = (thief != alist[3])

		truth = A+B+C+D
		# 四个人中只有一个人说真话的情况
		if truth == 1:
			if A:
				print("A说的是真话")
			elif B:
				print("B说的是真话")
			elif C:
				print("C说的是真话")
			elif D:
				print("D说的是真话")

			print(each+"是小偷！")


# 四个人的列表
alist = ['A', 'B', 'C', 'D']
find_thief(alist)