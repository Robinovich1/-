s = open('24.txt').readline()
l = 1
maxl = 0
for a in range(len(s)-1):
	if s[a] != s[a+1]:
		l+=1
	else:
		maxl = max(l,maxl)
		l = 1
print(maxl)