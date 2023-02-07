for a in range(500):
	ok = True 
	for x in range(1, 500):
		for y in range(1, 500):
			if not((2*y + 3*x != 135) or (y > a) or (x > a)):
				ok = False
				break 
		if not(ok):
			break
	if ok:
		print(a)
