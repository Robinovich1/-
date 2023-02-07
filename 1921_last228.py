from functools import lru_cache

def moves(h):
	a, b = h
	return (a+1, b), (b+2,a ), (a+2, b), (b+1, a)

@lru_cache(None)
def game(h):
	a, b = h
	if a + b==13: return 'W'
	if any(game(m) == 'W' for m in moves(h)): return 'P1'
	if all(game(m) == 'P1' for m in moves(h)): return 'B1'
	if any(game(m) == 'B1' for m in moves(h)): return 'P2'
	if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)): return 'B2'

for s in range(1, 10):
	h = s, 3
	if game(h) == "B1":
		print(s, game(h))