a = [int(x) for x in open("17-328.txt")]

k = 0
ans = []
knt = 0
summar = 0
for i in range(len(a)):
	if a[i]%2!=0:
		knt+=1
		summar+=a[i]
sr_ar = summar/knt


for z in range(len(a)-2):
	summ = (a[z] + a[z+1] + a[z+2])
	octsum = str(oct(summ))
	if octsum.count("7") == 0 and (summ)< sr_ar:
		k+=1
		ans.append(summ)
print(k, max(ans))

