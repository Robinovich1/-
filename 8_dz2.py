from itertools import product
cnt4 = 0
cnt5 = 0
cnt6 = 0

for i in product("ЧОАНИМЕ", repeat=4):
	a = ''.join(i)
	if a.count("М")==3:
		cnt4+=1

for i in product("ЧОАНИМЕ", repeat=5):
	a = ''.join(i)
	if a.count("М")==3:
		cnt5+=1

for i in product("ЧОАНИМЕ", repeat=6):
	a = ''.join(i)
	if a.count("М")==3:
		cnt6+=1
print(cnt6+cnt5+cnt4)