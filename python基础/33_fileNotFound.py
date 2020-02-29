# except errorName can free define
try:	
	with open("1.txt") as f:
		contents = f.read()
		print(contents)
except FileNotFoundError:
	message = "Sorry , the 1.txt cant found !!"
	print(message)
	
