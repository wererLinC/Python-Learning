responds = {}
polling_active = True
while polling_active:
	name = input("please input your name : ")
	respond = input("write your questionnaire : ")
	responds[name] = respond
	
	repeat = input("would you like to write again ? (YES/NO)")
	if(repeat.lower() == 'no'):
		polling_active = False
		
print("\n print poll results : \n")
print(responds)
