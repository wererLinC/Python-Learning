import json

with open("username.json", "w") as f:
	username = input("input your name :")
	json.dump(username, f)
