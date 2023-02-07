#12????77??9
f = open('24-228.txt')
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = [int(x) for x in f]
for i in range(len(a)-15):
	if a[i]=='s' and a[i+1]=='s' and a[i+2]=='1' and a[i+3]=='2' and a[i+8]=='7' and a[i+9]=='7' and a[i+12]=='9' and a[i+13]=='s' and a[i+14]=='s'\
	and a[i+4] in nums and a[i+5] in nums and a[i+6] in nums and a[i+7] in nums and a[i+10] in nums and a[i+11] in nums:
		print(a)
