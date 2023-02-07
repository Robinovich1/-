s = open('24-1.txt').readline()
l = 1
maxl = 0
summ = ''
for i in range(len(s) - 1):
	if ascii(s[i]) < ascii(s[i+1]):
		l+=1
		summ += s[i] + s[i+1]
	else:
		maxl = max(maxl, l)
		if l == maxl:
			print(l, summ)
		l = 1
		summ = ''
