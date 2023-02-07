s = open('24-212.txt').readline()
s = s.replace('A', 'g').replace('O', 'g')
s = s.replace('B', 's').replace('C', 's').replace('D', 's')
k = 1
while 'sg'*k in s:
	k+=1
print(k-1) # лишний раз добавляет 1 т.к. используется цикл while