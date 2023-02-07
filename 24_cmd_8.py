s = open("k8-10.txt").readline()
l = 1
maxl = 0
for i in range(len(s) - 1):
	if s[i] != s[i+1]:
		l+=1
	else:
		maxl = max(l, maxl)
		l = 1
print(maxl)