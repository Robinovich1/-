s = open('24.txt').readline()
l = lmax = 0
for i in s:
	if i!="G" and i!="P" and i!="W":
		l+=1
		lmax = max(l,lmax)
	else:
		l = 0
print(lmax)