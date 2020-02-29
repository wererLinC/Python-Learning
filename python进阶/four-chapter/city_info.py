from collections import Iterable, Iterator
import requests

#迭代器
class WeatherIterator(Iterator):
	def __init__(self, caties):
		self.caties = caties
		self.index = 0

	def __next__(self):
		if self.index == len(self.caties):
			raise StopIteration
		city = self.caties[self.index]
		self.index += 1
		return self.get_weather(city)
	
	def get_weather(self, city):
		url = url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
		information = requests.get(url)
		data = information.json()['data']['forecast'][0]
		return city, data['high'], data['low']

#可迭代对象
class WeatherIterable(Iterable):
	
	def __init__(self, cities):
		self.cities = cities
	
	def __iter__(self):
		return WeatherIterator(self.cities)
			

#显示函数
def show(w):
	for x in w:
		print(x)

w = WeatherIterable(['北京', '漳浦', '厦门'] * 10)
show(w)
