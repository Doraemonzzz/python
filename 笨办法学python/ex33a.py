# -- coding: utf-8 --
from sys import argv
c,a,b=argv
a=int(a)
b=int(b)
def print_a(a,b):
	i=0
	numbers=[]
	
	while i<a:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i+=b
		print "Numbers now: ",numbers
		print "At the bottom i is %d"%i
print_a(a,b)