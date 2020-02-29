# print

def greet():
	print("hello")

greet()

def greet(name):
	print("hello " + name.title() + " !")
greet("jeese")

print("---------------------------------------------")
def pet_info(pet_host, pet_name):
	print("welcome " + pet_host + " !")
	print("your pet name is " + pet_name + " !")
	
pet_info(pet_name = "pangpang", pet_host = "weilin")
	
