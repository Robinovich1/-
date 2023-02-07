s = 49**7 + 7**21 - 7
k = 0
while s>=0:
	if s%7 == 6:
		k += 1 
	s= s//7
print(k)