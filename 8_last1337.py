from itertools import permutations

res = []
k = 0
for x in permutations('СПОРТЛОТО'):
	a = ''.join(x)
	res.append(a)
print(len(res))
for i in range(len(res)):
	res2 = []
	nobuk = []
	