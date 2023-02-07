from functools import lru_cache


def moves(h):
	return (h+1), (h*2), (h*3)

@lru_cache(None)
def game(h):
	if 36<=h<=60: return "W"
	if h>60: return "P1"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2"

for s in range(1, 100):
	if game(s) == 'B1':
		print(s, game(s))