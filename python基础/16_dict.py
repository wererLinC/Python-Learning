# dict
alien_0 = {'color': 'green', 'age': 18}
print(alien_0['color'])
print(alien_0['age'])

# insert key-val
alien_0['x_postion'] = 12
alien_0['y_postion'] = 24
print(alien_0['x_postion'])

# edit key-val
alien_0['age'] = 19
print(alien_0['age'])

# del key-val
del alien_0['color']
print(alien_0)

# range for key-val
for key, val in alien_0.items():
	print(str(key) + ":" + str(val))

# range for keys
for keys in alien_0.keys():
	print(keys)

# range for vals
for vals in alien_0.values():
	print(vals)
