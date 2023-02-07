from functools import lru_cache


def moves(h):
	x, cnt = h
	a = []
	if cnt>=1: a.append((x+1, cnt-1))
	if cnt>=2: a.append((x+2, cnt-2))
	if cnt>=x: a.append((x*2, cnt-x))
	return a

@lru_cache(None)
def game(h):
	x, cnt = h
	if x>=41: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P1" or game(i) == "P2" for i in moves(h)): return "B2"
	if any(game(i) == "B2" for i in moves(h)): return "P3" 
	if all(game(i) == "P1" or game(i) == "P2" or game(i) == "P3" for i in moves(h)): return "B3"

for s in range(1, 200):
	h = s, 50 - s            #максимум 50 камней
	if game(h) == 'B3':
		print(s, game(h))

