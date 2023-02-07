from itertools import permutations

k = 0
for n in range(500, 601):
	a = str(n)
	a_max = 0
	a_min = 1000
	for x in permutations(a, 2):
		l = ''.join(x)
		if l[0]!=0:
			l = int(l)
			a_max = max(a_max,l)
			a_min = min(a_min,l)
	if a_max - a_min == 10:
		k+=1 
print(k)
			
