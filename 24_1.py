f = open('24.txt')
s = f.readline()
lmax = 0
l = 1
for i in range(len(s)-1):
	if s[i] != s[i+1]:
		l+=1
	else: 
		lmax = max(l,lmax)
		l = 1
print(lmax)