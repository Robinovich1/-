s = open('24.txt').readline()
l = 1
maxl = 0
for i in range(len(s) - 1):
	if ascii(s[i]) < ascii(s[i+1]):
		l+=1
	else:
		maxl = max(maxl, l)
		if l == maxl:
			print(l, i - l + 2)
		l = 1
