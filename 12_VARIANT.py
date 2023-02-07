cnt = 0

f =[]
for v in range(1000):
	k = 0
	for i in range(2, v // 2+1):
		if (v % i == 0):
			k = k+1
	if (k <= 0):
		f.append(v)
    



for n in range(10,100):
	z = '1' + n*'0'
	while '10' in z:
		if '10' in z:
			z = z.replace('10', '001', 1)
		if '1' in z:
			z = z.replace('1', '01', 1)
	if len(z) in f:
		cnt+=1
print(cnt)

