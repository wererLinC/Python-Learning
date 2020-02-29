student = ['lilei', 'kangkang', 'xiaozhi']
print(student[:2])


student = ['lilei', 'kangkang', 'xiaozhi']
print(student[1:])


students = ['lilei', 'kangkang', 'xiaozhi']
for student in students:
	print(student)

# assign
my_food = ['pork', 'beef', 'chicken']
my_favorite_food = my_food

my_food.append('duck')
print(my_favorite_food)

# copy
my_food = ['pork', 'beef', 'chicken']
my_favorite_food = my_food[:]

my_food.append('duck')
print(my_favorite_food)
