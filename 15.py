for A in range(1, 1000):
	ok = True
	for x in range(1,1000):
		f = ((x%A==0) and (x%21==0)) <= (x%18==0)
		if not(f):
			ok = False
			break
	if ok:
		print(A)