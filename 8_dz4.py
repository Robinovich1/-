
#Андрей составляет шестибуквенные кодовые слова из букв ЕГЭИНФ. Каждую букву можно использовать любое количество раз. При 
#этом слово может начинаться только с буквы Е, а заканчивается либо буквой Э, либо буквой И, а также слово должно содержать 
#xотя бы два сочетания букв ФИ и не содержать сочетания букв ЕГЭ. Сколько таких слов может составить Андрей?
from itertools import product
cnt = 0
for i in product("ЕГЭИНФ", repeat=6):
	a=''.join(i) 
	if a[0]=='Е' and (a[-1]=="Э" or a[-1]=="И") and 'ЕГЭ' not in a and a.count('ФИ')==2:
		cnt+=1
print(cnt)