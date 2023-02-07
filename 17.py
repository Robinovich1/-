f = open('17-292.txt')
a = [int(x) for x in f]
ans = []
for i in range(len(a)-1):
	if (a[i]%6 + a[i + 1]%6) == (a[i]%11 + a[i + 1]%11):
		ans.append(a[i] + a[i+1])
print(len(ans), max(ans))