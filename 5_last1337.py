k = 0
for n in range(1000):
	nbin = bin(n)
	nbinSum = 0
	n_str = str(nbin)[2:]
	for i in range(len(n_str)):
		nbinSum+=int(n_str[i])
	nbinbin =bin(nbinSum)

	if n%2 != 0:
		n1 = '1'+ str(n_str) + '00'
	if n%2 == 0:
		n1 = n_str + str(nbinbin)[2:]
	r = int(n1,2)
	if 500<= r <=700:
		k+=1
print(k)

