class Car():
	def __init__(self, make, model, year):
		'''initial car '''
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
		'''descript car detail'''
		long_name = self.make + " " + self.model + " " + str(self.year)
		return long_name.title()
		
	def update_year(self, year):
		'''edit year'''
		self.year = year

new_car = Car("Panamera", "4S", 2016)
print(new_car.get_descriptive_name())
print("My favorite !!!")
new_car.update_year(2019)
print(new_car.get_descriptive_name())
print("My favorite too !!!")		
