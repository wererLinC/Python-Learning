class Dog():
	"""dog class"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		'''sit function'''
		print(self.name.title() + " is now sitting !!")
		
	def roll_over(self):
		'''roll !!!'''
		print(self.name.title() + " is now rolling !!")
		
	def __repr__(self):
		""" now doging !!!"""
	
	
dog = Dog("pangpang", 25)
print(dog.name)
dog.sit()
dog.roll_over()
		
