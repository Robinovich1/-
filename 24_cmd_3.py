s = open('k7a-3.txt').readline()
s = s.replace('A', '!').replace('B', '!').replace('E', '!').replace('F', '!')
l    = 0
maxl = 0
for a in s:
	if a == '!':
		l+=1
	else:
		maxl = max(l, maxl)
		l    = 0
print(maxl)