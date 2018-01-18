# -*- coding: utf-8 -*-
def convert_numbers(x):
		try:
			return int(x)
		except ValueError:
			return None

class lexicon(object):
	def __init__(self):
		self.a1=['north','south','east','west','down','up','left','right','back']
		self.a2=['go','stop','kill','eat']
		self.a3=['the','in','of','from','at','it']
		self.a4=['door','bear','princess','cabinet']
	
	def scan(self,a):
		b=a.split()
		c=[]
		for x in b:
			if convert_numbers(x) is None:
				if x.lower() in self.a1:
					c.append(('direction',x.lower()))
				elif x.lower() in self.a2:
					c.append(('verb',x.lower()))
				elif x.lower() in self.a3:
					c.append(('stop',x.lower()))
				elif x.lower() in self.a4:
					c.append(('noun',x.lower()))
				else:
					c.append(('error',x.lower()))
			else:
				c.append(('number',int(x)))
				
		return c

b=lexicon()		
print b.scan("go kill eat")