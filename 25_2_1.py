for x in range (2, 10001):
	deli = 0
	k = 0
	for i in range(1, 10001):
		if x!=i and x%i == 0:
			deli+=i
			k+=1
	if x == deli :
		print(x, k)
	

