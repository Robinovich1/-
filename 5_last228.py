for n in range(10000000):
	result = []
	s1 = 0 #chetnie
	s2 = 0 #nechetnie
	n1 = str(n)
	for i in range(len(n1)):
		if int(n1[i])%2 == 0:
			s1 += int(n1[i])
	for z in range(len(n1)):
		if len(n1)%2 == 0:
			if z%2 != 0:
				s2 += int(n1[z])
		else:
			if z%2 == 0:
				s2 += int(n1[z])
	res = abs(s1 - s2)
	if res == 26:
		print(n)


		

