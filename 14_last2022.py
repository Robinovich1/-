x = 4*25**2022 - 2*5**2000 + 125**1011 - 3*5**100 - 660

k = 0
while x>0:
	if x%5==4:
		k+=1
	x//=5 
print(k)