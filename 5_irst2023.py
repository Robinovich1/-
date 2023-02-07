res = []
for n in range(40,50):
	ndub = str(bin(n))
	if ndub[-1]=='1':
		ndub = ndub + '0'
	else : ndub = ndub + '1'
	if ndub[-1]=='1':
		ndub = ndub + '0'
	else : ndub = ndub + '1'
	ndub = ndub[2:]
	r = int(ndub, 2)
	print(r, n)
	


		

	
