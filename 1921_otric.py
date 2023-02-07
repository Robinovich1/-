from functools import lru_cache
k = 0
def moves(h):
	a = []
	if h//3 > 0 : a.append((h//3))
	if h-10 > 0 : a.append((h-10))
	return a


@lru_cache(None)
def game(h):
	if h<=10:return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2" 

for s in range(1, 200):
	if game(s) == 'B2':
		k+=1
print(k)

