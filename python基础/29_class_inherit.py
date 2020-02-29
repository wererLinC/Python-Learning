# parent
class Student():
	sum = 0
	
	def __init__(self, name, age):
		'''__init__()'''
		self.name = name
		self.age = age
		self.__score = 0
		
	def __score_make(self):
		'''make score'''
		self.__score = 98
	
	def print_score(self):
		'''print score'''
		self.__score_make()
		print(self.__score)
	
	@classmethod
	def plus_sum(cls):
		cls.sum += 1
		print(cls.sum)
		
class xiaoming(Student):
	'''student_01'''
	def __init__(self, name, age):
		super().__init__(name, age)
		
	def get_parent(self):
		print("daming")
		
class xiaohong(Student):
	'''student_01'''
	def __init__(self, name, age):
		super().__init__(name, age)
		
	def get_parent(self):
		print("dahong")
		
xiaoming = xiaoming("xiaoming", 18)
xiaoming.print_score()
xiaoming.get_parent()

xiaohong = xiaohong("xiaohong", 18)
xiaohong.print_score()
xiaohong.get_parent()
