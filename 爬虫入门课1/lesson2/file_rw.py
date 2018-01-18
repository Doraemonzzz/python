with open('txt.txt') as f:
	for line in f.readlines():
		print line
		
with open('txt.txt') as f:
	print f.read()
	
with open('txt.txt','w') as f:
	f.write('123')