for A in range(1, 1000):
	ok = True
	for x in range(1,1000):
		f = (x%A==0) and ((x%A!=0) <= ((x%36==0)<=(x%15!=0)))
		if not(f):
			ok = False
			break
	if ok:
		print(A)