#9 12 + 3 8 − 3
n = 9**12 + 3**8 - 3
k = 0
while n > 0:
	if n%3 == 2:
		k+=1
	n//=3
print(k)