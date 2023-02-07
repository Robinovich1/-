for a in range(-1000, 1000):
	ok = True 
	for x in range(1000):
		for y in range(1000):
			if not((3*y + x < a) or (y>15) or (x>12)):
				ok = False
				break
		if not(ok):
			break
	if ok:
		print(a)
		break
