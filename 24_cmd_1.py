s = open('k8.txt').readline()
symb = ''
l = 1
ans = []
maxl = 0
for i in range(len(s)-1):
	if s[i] == s[i+1]:
		l+=1
	else:
		if l >= maxl:
			ans.append(str(l) + s[i])
			maxl = l
		l = 1
print(ans)