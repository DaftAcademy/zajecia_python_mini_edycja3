#! /usr/bin/env python3

# __init__ jest metodą, która jest uruchamiana zawsze tuż po stworzeniu 
# instancji (przez __new__ <- konstruktor). Ale jeszcze przed zwróceniem 
# instancji.
# Konstruktor (__new__), jest sporadycznie używany
# __init__ jest używany o wiele, wiele częściej.
# Służy do "customizacji" instancji.

class SecondClass():
	def __init__(self):
		print("tworzę nową instancję klasy")
		

a = SecondClass()
print("id(a) = {}".format(id(a)))
b = SecondClass()
print("id(b) = {}".format(id(b)))

# Argumenty podane podczas tworzenia niwej instancji są przekazywane do __init__
# Dzięki temu każda instancja może się różnić (danymi) już na starcie.
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def print_coordinates(self):
		print('x = {}'.format(self.x))
		print('y = {}'.format(self.y))
		
c = Point(1, 2)
c.print_coordinates()
d = Point(5, 10)
d.print_coordinates()
