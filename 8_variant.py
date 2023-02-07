from itertools import product

cnt=0
for x in product('АНТИУОПЯ', repeat=6):
	a=''.join(x)
	cnt+=1
print(cnt*7)
print(1835008)