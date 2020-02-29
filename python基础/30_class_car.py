# Car
class Car():
	'''Car'''
	def __init__(self, model, year):
		'''initial car'''
		self.model = model
		self.year = year
		
	def get_descript_car(self):
		print("the model is " + self.model + " product year is " + str(self.year))
		
class Battery():
	'''battery'''
	def __init__(self, battery_size = 70):
		'''initial battery'''
		self.battery_size = battery_size
	def describe_battery(self):
		print("the car will run " + str(self.battery_size) + " KM")
		
class Tesla(Car):
	'''my tesla'''
	def __init__(self, model, year):
		super().__init__(model, year)
		self.battery = Battery()
		

my_tesla = Tesla('panemala 4s', 2016)
my_tesla.get_descript_car()
my_tesla.battery.describe_battery()
	
		
