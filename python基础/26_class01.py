class Student:
	name = ''
	age = 18
	
	def print_info(self):
		print("name : " + self.name)
		print("age : " +str(self.age))
		
student = Student()
student.print_info()
