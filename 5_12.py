cnt=0
for n in range(10000):
	binx = str(bin(n))[2:]
	if n%2==0:
		res = "1" + binx + '11'
	else:
		res = "11" + binx + '0'
	des = int(res,2)
	if des>=500 and des<=1000:
		cnt+=1
print(cnt)

