from itertools import permutations
cnt = 0
for x in permutations('СПОРТЛОТО'):
	n=''.join(x)
	cnt+=1
print(cnt)
