a = [int(x) for x in open('17-1.txt')]
ans = []
numnorm =[]
midl = []

for i in range(len(a)-1):
	if a[i] > 0 and a[i] % 15 ==0:
		numnorm.append(a[i])
minnum = min(numnorm)



for i in range(len(a)-1):
	if a[i]%2!=0 and a[i+1]%2!=0 and (a[i]+a[i+1])/2 >= minnum:
		ans.append(a[i]+a[i+1])
		midl.append((a[i]+a[i+1])/2)
print(len(ans), min(midl), len(a))