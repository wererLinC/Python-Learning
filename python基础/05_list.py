# list

bicycles = ['trek', 'look', 'help']
print(bicycles[:1])
print(bicycles[0].title())
print(bicycles[-1])

message = "my first bick is " + bicycles[0].title() + "."
print(message)


# edit
bicycles[0] = 'Treek'
print(bicycles[0])

# append
bicycles.append('myLove')
print(bicycles[-1])

# insert
bicycles.insert(1, 'honda')
print(bicycles[1])

# del
del bicycles[-1]
print(bicycles[-1])

# pop
suzuki = bicycles.pop()
print(suzuki)

# remove
too_expensive = 'look'
bicycles.remove(too_expensive)
print(bicycles)
