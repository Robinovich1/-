a = [int(x) for x in open("17_22_12_2023.txt")]

ans = []

k = 0

for i in range(len(a)-1):
	if a[i] + a[i+1] == max(a):
		print('228')
		

print(len(a), max(a), min(a))


