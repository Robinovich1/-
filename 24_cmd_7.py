s = open('k8-12.txt').readline()
symb = ''
l = 1
maxl = 0
for i in range(len(s) - 1):
	if s[i] == s[i+1]:
		l+=1
	else:
		maxl = max(maxl,l)
		if maxl == l:
			print(s[i], l)
		l =1