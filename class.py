# -*- coding:utf-8 -*-
class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
lily=student('kama',30)
lily.score