#f = open('24-213.txt')
#s = f.readline()
#l = 0
#lmax = 0
#s = s.replace('NPO','!')
#s = s.replace('PNO','!')
#for i in s:
#	if i == '!':
#		l+=1
#	else:
#		lmax = max(l, lmax)
#		l = 0
#print(lmax)
f = open('24-213.txt')
s = f.readline()
l = 0
lmax = 0
i = 0
while i < len(s)-2:
	if s[i:i+3] == 'NPO' or s[i:i+3] == 'PNO':
		i+=3
		l+=1
	else:
		lmax = max(l, lmax)
		l = 0
		i +=1
print(lmax)