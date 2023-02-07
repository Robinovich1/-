def moves(h):
	a = []
	if h%2!= 0 : a.append((h*3))
	if (h+1)%2 != 0 :a.append((h+1))
	if (h+3)%2 != 0 :a.append((h+3))
	return a
	


def game(h):
	if h>=51: return "W"
	if any(game(i) == "W" for i in moves(h)): return "P1"  #i принимает два значения: H+2 или H*2
	if all(game(i) == "P1" for i in moves(h)): return "B1" 
	if any(game(i) == "B1" for i in moves(h)): return "P2" 
	if all(game(i) == "P2" for i in moves(h)): return "B2" 

for s in range(1, 51):
	if game(s) == 'B2':
		print(s, game(s))
#7 12 14
