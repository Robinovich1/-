k = 0
for n in range(1000, 10000):
	if (str(n)[0] == '4' or str(n)[0] == '8' or str(n)[0] == '9') and str(oct(n))[-1] == '4':
		k+=1
print(k)