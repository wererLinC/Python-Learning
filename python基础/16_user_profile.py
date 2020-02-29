def build_profile(first, last, **user_info):
	profile = {}
	profile['first'] = first
	profile['last'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

person_profile = {}	
person_profile = build_profile("chen", "weilin",
								location = "zhangpu",
								interest = "singing")
print(person_profile)

