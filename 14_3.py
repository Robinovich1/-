# № 5495
# x23x5 22 – 67y9y 13
for x in range(22):
	for y in range(13):
		a = x*22**4 + 2*22**3 + 3*22**2 + x*22 + 5
		b = 6*13**4 + 7*13**3 + y*13**2 + 9*13 + y
		if (a - b) % 57 ==0:
			print((a - b) / 57, y + x)