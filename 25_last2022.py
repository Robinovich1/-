
#100000000 9 символов 5 символов 4 символа

for x in range(10000):
	z = str(x)
	numb = "11" + z + "223"
	a = int(numb)
	if a%149 == 0 and a < 10**8:
		print(a, a/149)