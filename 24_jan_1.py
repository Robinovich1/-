from fnmatch import *

s = open('24-230 (1).txt').readline()
for c in 'QWERTYUIOPLJHGFDSAZXCVBNM':
	s = s.replace(c, ' ')
s = s.split('KK')
s_max = []
for c in s:
	if ' ' not in c and fnmatch(c, '43??78???34'):
		s_max.append(int(c))
z = str(max(s_max))
k = 1
for i in range(len(z)):
			if int(z[i])%2 !=0:
				k*= int(z[i])
print(k)
