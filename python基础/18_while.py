# while
count = 0
while count < 5:
	print("Hello !")
	count += 1


unconfirm_users = ['kangkang', 'huanhuan', 'wangqian']
confirm_users = []

while unconfirm_users:
	user = unconfirm_users.pop()
	print("Verifying user :  " + user + " !")
	confirm_users.append(user)
	
print("verified users :\n")
for user in confirm_users:
	print(user)
