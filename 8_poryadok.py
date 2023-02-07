from itertools import product 
cnt = 0
for i in product("АПРСУ", repeat = 5):
	a = ''.join(i)
	cnt+=1
	if a[0]=='У' and "АА" not in a:
		print(cnt)
		break

