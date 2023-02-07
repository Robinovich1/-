for n in range(100):
	bin_n = bin(n)
	str_n = str(bin_n)
	if n%2 == 0:
		n_2 = str_n + '0'
	else:
		n_2 = str_n + '1'
	number = n_2[0] + n_2[1]
	if n_2.count('1')%3 == 0:
		n_2.replace(number, '11',1)
	else:
		n_2.replace(number, '10',1)
	r =int(n_2,2)
	if r >= 26:
		print(n, r)
