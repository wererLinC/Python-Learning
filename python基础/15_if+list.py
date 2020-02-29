# if + list 
requested_toppings = ['Green peppers']
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + " into pizzas")
	print("\nFinished your pizza")
else:
	print("are you sure you want a plain pizza")



# using multiple lists

available_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = ['mushrooms', 'olives']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + " into pizza .")
	else:
		print("Sorry we dont have " + requested_topping + ".")

print("\nFinished your pizza .")
