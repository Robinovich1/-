#1ЧНЧНЧН
chet = ['2', '4', '6', '8', '0']
nech = ['1', '3', '5', '7', '9']
for s in range(1000000, 2000000):
	i = str(s)
	if  i[0] == '1' and i[1] in chet and i[3] in chet and i[5] in chet and i[2] in nech and i[4] in nech and i[6] in nech and s%4023==0:
		print(i, s/4023)