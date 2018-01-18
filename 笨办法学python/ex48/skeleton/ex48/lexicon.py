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
		self.list=[]
	
	def scan(self,a):
		self.list=[]
		self.a=a
		self.b=self.a.split()
		for x in self.b:
			if convert_numbers(x) is None:
				if x.lower() in self.a1:
					self.list.append(('direction',x.lower()))
				elif x.lower() in self.a2:
					self.list.append(('verb',x.lower()))
				elif x.lower() in self.a3:
					self.list.append(('stop',x.lower()))
				elif x.lower() in self.a4:
					self.list.append(('noun',x.lower()))
				else:
					self.list.append(('error',x.lower()))
			else:
				self.list.append(('number',int(x)))
		return self.list
lexicon=lexicon()
#b=lexicon()
#lexicon.scan("go kill eat")