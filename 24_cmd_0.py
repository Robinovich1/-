s = open('k7.txt').readline()
l = 0
maxl = 0
for i in s:
	if i == 'C':
		l+=1
	else:
		maxl = max(maxl, l)
		l = 0
print(maxl)