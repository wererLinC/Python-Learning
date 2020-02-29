'''class method'''
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
		

student1 = Student("weilin", 24)
student1.print_score()
print(student1.__dict__)
