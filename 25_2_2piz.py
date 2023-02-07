#№ 2589
for num_1 in range(2, 500):
	sum_del1 = 0
	for num_2 in range(2, 500):
		del2 = 0
		for i in range(1, 500):
			if num_1 != i and num_1 % i == 0:
				sum_del1+=i
			if num_2 != i and num_2 % i == 0:
				del2+=i
		if (del2 == num_1 and sum_del1 == num_2) and num_2 > num_1:
			print(num_1, num_2)

