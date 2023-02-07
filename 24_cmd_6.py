s = open("k7a-6 (1).txt").readline()
s = s.replace("A", '!').replace("E", '!')
l = 0
maxl = 0
for a in s:
	if a != '!':
		l+=1
	else:
		maxl = max(maxl, l)
		l = 0
print(maxl)