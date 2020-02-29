# print model
def print_model(unprint_model, completed_modes):
	while unprint_model:
		current_designe = unprint_model.pop()
		print("Printing model" + current_designe + " !")
		completed_models.append(current_designe)

# show model
def show_completed_model(completed_models):
	print("follow model has alread printed !!")
	for completed_model in completed_models:
		print(completed_model)
		
# test
unprint_model = ['Audi', 'BMW', 'Benz']
completed_models = []
print_model(unprint_model[:], completed_models)
show_completed_model(completed_models)
print("----------------------------")
print("print unprint_model :")
print(unprint_model)
		
