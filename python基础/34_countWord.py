def count_word_num(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
	except FileNotFoundError:
		mess = "Sorry ," + filename + " not found !!"
		print(mess)
	else:
		words = contents.split()
		word_num = len(words)
		print(word_num)

filenames = ['./file/love.txt', './file/love1.txt']
for filename in filenames:
	count_word_num(filename)

