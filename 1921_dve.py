from functools import lru_cache
def moves(h):
	a, b = h
	return (a+1,b), (a+b,b), (a,b+1),(a,b+a)

@lru_cache(None)
def game(h):
	a, b = h
	if a+b>=81: return 'W'
	if any(game(m) == 'W' for m in moves(h)): return 'P1'
	if all(game(m) == 'P1' for m in moves(h)): return 'B1'
	if any(game(m) == 'B1' for m in moves(h)): return 'P2'
	if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)): return 'B2'

for s in range(1, 74):
	h = 7, s
	if game(h) == "B2":
		print(s, game(h))