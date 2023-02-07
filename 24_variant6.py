with open( "24-228.txt", "r" ) as F:
  a = F.readline()
a_max=0
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(len(a)-14):
  if a[i]=='S' and a[i+1]=='S' and a[i+2]=='1' and a[i+3]=='2' and a[i+8]=='7'\
  and a[i+9]=='7' and a[i+12]=='9' and a[i+13]=='S' and a[i+14]=='S' and a[i+4]\
  in nums and a[i+5] in nums and a[i+6] in nums and a[i+7] in nums and a[i+10] in nums and a[i+11] in nums:
    b = a[i+2] + a[i+3] + a[i+4] + a[i+5] + a[i+6] + a[i+7] + a[i+8] + a[i+9] + a[i+10] + a[i+11] + a[i+12]
    a_int = int(b)
    a_max = max(a_int,a_max)
print(a_max)