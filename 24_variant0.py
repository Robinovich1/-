#12????77??9
f = open('24-228.txt')
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = [str(x) for x in f]
for i in range(len(a)-14):
	if a[i]=='S' and a[i+1]=='S' and a[i+2]=='1' and a[i+3]=='2' and a[i+8]=='7'\
	and a[i+9]=='7' and a[i+12]=='9' and a[i+13]=='S' and a[i+14]=='S' and a[i+4]\
	in nums and a[i+5] in nums and a[i+6] in nums and a[i+7] in nums and a[i+10] in nums and a[i+11] in nums: 
	print(1)
