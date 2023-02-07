from functools import lru_cache

def moves(h):
	a, b = h
	return (a+2, b), (a*3, b), (a, b+2), (a, b*3)

@lru_cache(None)
def game(h):
	a, b = h
	if 47<=a+b<=59 : return 'W'
	if 59 < a+b    : return 'P1'
	if any(game(m) == 'W' for m in moves(h)): return "P1"
	if all(game(m) == 'P1' for m in moves(h)): return "B1"
	if any(game(m) == 'B1' for m in moves(h)): return "P2"
	if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)): return "B2"

for s in range(1, 42):
	h = 5, s
	if game(h) == 'B2':
		print(s, game(h))