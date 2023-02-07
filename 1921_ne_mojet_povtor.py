from functools import lru_cache


def moves(h):
	x, last = h
	a = []
	if last != "+1" : a.append((x+1, "+1"))
	if last != "+2" : a.append((x+2, "+2"))
	if last != "*3" : a.append((x*3, "*3")) 
	return a

@lru_cache(None)
def game(h):
	x, last = h
	if x>=140: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2"

for s in range(1, 100):
	h = s, '-1'
	if game(h) == 'B2':
		print(s, game(h))