for A in range(1, 1000):
	ok = True
	for x in range(1,1000):
		f = (A<50) and ((x%A!=0) <= ((x%10==0)<=(x%18!=0)))
		if not(f):
			ok = False
			break
	if ok:
		print(A)