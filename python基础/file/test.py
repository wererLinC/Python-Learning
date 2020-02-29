# read
filename = 'love.txt'
with open(filename, 'r') as f:
	contents = f.readlines()
	
for content in contents:
	print(content)
	
# write
filename1 = 'love1.txt'
with open(filename1, 'w') as f1:
	f1.write("i love C++")

# add
filename1 = 'love1.txt'
with open(filename1, 'a') as f1:
	f1.write("i love C")

