r_max = 0
for n in range(10000):
	binar = bin(n)[3:]
	srt = str(binar)
	if srt.count('1')%2==0:
		res = '10' + srt
	else:
		res = '1' + srt + '0'
	r = int(res, 2)
	if r < 450:
		r_max = max(r_max,r)
print(r_max)



