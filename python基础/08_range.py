# range [)

for value in range(1, 5):
	print(value)

# range[start, eend, span)

for value in range(1, 6, 2):
	print(value)

# list(range[))

num_list =  list(range(1, 6, 2))
print(num_list)

digits = [0, 5, 7, 8, 9, 34, 5, 23, 5,6, 66]

# min
print(min(digits))

# max
print(max(digits))

# sum
print(sum(digits))

# list analysis
squares = [value ** 2 for value in range(1, 11)]
print(squares)
