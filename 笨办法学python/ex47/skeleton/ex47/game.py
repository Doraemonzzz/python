# -*- coding: utf-8 -*-
class Room(object):
	def __init__(self,name,description):
		self.name=name
		self.description=description
		self.paths={}
		
#获取键对应的值
	def go(self,direction):
		return self.paths.get(direction,None)
		
#update() 函数把字典dict2的键/值对更新到dict里 dict.update(dict2)
	def add_paths(self,paths):
		self.paths.update(paths)