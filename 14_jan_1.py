#273x2 158 + 1x390 158
k = 0
for x in range(158):
	a = 2*158**4 + 7*158**3 + 3*158**2 + x*158 + 2
	b = 1*158**4 + x*158**3 + 3*158**2 + 9*158 + 0
	c = a + b 
	if c%73==0:
		k+=c//73
		print(c//73, x)
print(k)