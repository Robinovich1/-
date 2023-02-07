for n in range(2000):
	n2 = n
	r_1 = ''
	while n2>0:
		r_1+=str(n2%3)
		n2//=3
	r2 = r_1[::-1]
	r2+=str(n%3)
	r = int(r2, 3)
	if r > 999:
		print(r)