from fnmatch import *

for x in range(0, 10**8):
	if fnmatch(str(x), '12*6789') and x%39 == 0:
		print(x, x//39)
