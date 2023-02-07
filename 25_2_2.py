#№ 2589
for num_1 in range(2, 300):
	sum_del1 = 0
	for i1 in range(1,300):
		if i1 != num_1 and num_1%i1==0:
			sum_del1+=i1
	for num_2 in range(2, 300):
		sum_del2 = 0
		for i2 in range(1,300):
			if i2 != num_2 and num_2%i2==0:
				sum_del2+=i2
			if sum_del2 ==sum_del1:
				print(num_1, num_2)

