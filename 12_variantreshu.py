n = '1' * 99

while '111' in n :
	n =n.replace('11','2',1)
	n =n.replace('22','1',1)
print(n)
	