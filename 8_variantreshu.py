from itertools import product
k = 0
for i in product('ВИШНЯ', repeat=6):
	x=''.join(i)
	if x.count("В")<=1 and x[0]!='Ш' and x[-1]!='И' and x[-1]!='Я': k+=1
print(k)