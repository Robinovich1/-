def f(x, An, Ak):
	return not(130<=x<=171) or not(150<=x<=185) or (An<=x<=Ak)

min = 1000
for An in range(100, 199):
	for Ak in range(100, 199):
		ok = True
		for x in range(1,1000):
			if not f(x, An, Ak):
				ok = False
				break 
		if ok and Ak - An < min:
			min = Ak - An

print(min)