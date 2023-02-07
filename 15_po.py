for a in range(1,1000):
	ok = True 
	for x in range(1,1000):
		if not((x & a != 0) <= ((x & 20 == 0) <= (x & 5 != 0))):
			ok = False 
			break 
	if ok:
		print(a)