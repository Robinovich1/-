#   7*729**543 – 6*81**765 – 5*9**987 – 20
#a = 7*729**543 - 6*81**765 - 5*9**987 - 20
#count8 = 0
#while a:
#	if a % 9 == 8 : count8 += 1
#	a //= 9
#print( count8 )


a = 2*7**2 + 3*7**1 + 4
b = (7**80 - 7**4 + a)*5*8
c = b//6
count4 = 0
while c:
	if c % 7 == 4 : count4 += 1
	c //= 7
print( count4 )
