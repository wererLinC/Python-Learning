def build_person(first_name, second_name):
	person = {'first' :first_name, 'second': second_name}
	return person
	
person = build_person("chen", "weilin")
print(person)


def greet(names):
	for name in names:
		message = "hello " + name + " !"
		print(message)

users = ['weilin', 'menglong']
greet(users)


