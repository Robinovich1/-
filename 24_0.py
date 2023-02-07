f = open('k7.txt')
s = f.readline()
lmax = 0
l = 0
for i in s:
	if i == 'C':
		l+=1
	else: 
		lmax = max(l,lmax)
		l = 0
print(lmax)