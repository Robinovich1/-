s = open('k7a-5.txt').readline()
l = 0
maxl = 0
for a in s:
	if a != "C" and a != "F":
		l+=1
	else:
		maxl = max(maxl, l)
		l = 0
print(maxl)