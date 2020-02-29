class Car():
	'''Car'''
	def __init__(self, model, year):
		self.model = model
		self.year = year
		
	def describe_car(self):
		print("the model is " + self.model + " the product year is " + str(self.year))
		
class Battery():
	'''describe battery'''
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
	def describe_battery(self):
		print("the battery can run is " + str(self.battery_size))
		
class Tesla(Car):
	def __init__(self, model, year):
		super().__init__(model, year)
		self.battery = Battery()
	
