#ZaYX55 –  2XaY55
for a in range(55):
	b_1 = int("Z", 36)
	b_2 = int("Y", 36)
	b_3 = int("X", 36)
	zx = b_1*55*3 + a*55**2 + b_2*55 + b_3
	zy = 2*55*3 + b_3*55**2 + a*55 + b_2
	if (zx - zy) % 29 == 0:
		print(zx - zy)