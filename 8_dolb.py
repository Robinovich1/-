from itertools import product

cnt = 0
sht =['11', '22', '33', '44', '55' , '66', '77', '00']
for i in product('01234567', repeat = 4):
	a=''.join(i)
	if  a[0] != '0' and ((a[0]==a[1]and a[2]!=a[3]) or (a[1]==a[2] and a[0]!=a[3]) or (a[2]==a[3]and a[0]!=a[1]))\
	and a.count('0')<=2 and a.count('1')<=2 and a.count('2')<=2 and a.count('3')<=2 and a.count('4')<=2\
	and a.count('5')<=2 and a.count('6')<=2 and a.count('7')<=2:
		cnt += 1
print(cnt)