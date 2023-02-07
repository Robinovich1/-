from itertools import product

k = 0
for x in product('0123456', repeat=7):
	s = ''.join(x)
	if s[0]!='3' and s[0]!='5' and s[0]!='0' and ('44' not in s or '22' not in s):
		k+=1
print(k)