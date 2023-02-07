#7∙5 1984 – 6∙25 777 + 5∙125 333 – 4
a = 7*5**1984 - 6*25**777 + 5*125**333 - 4
res = ''
result = 0
while a:
	res += str(a%5)
	a//=5 
for i in range(len(res)):
	result += int(res[i])
print(result)
