#! /usr/bin/env python3

class BaseClass():
	def hello(self):
		print('hello')
		
	def hi(self):
		print('hi')
		

# tak zapisujemy dziedziczenie pojedyńcze
class DerivatedClass(BaseClass):
	def allo(self):
		print('allo')
	
	# to dodać w drugiej fazie, jako przykład, że można "nadpisywać" metody
	# klasy bazowej
	def hello(self):
		print('dzień dobry')
		

b = BaseClass()
print(type(b))
b.hello()
b.hi()

d = DerivatedClass()
print(type(d))
d.allo()
d.hello()
d.hi()

# a to w trzeciej fazie jako przykład, że można więcej niż raz dziedziczyć
class EvenMoreDerivatedClass(DerivatedClass):
	def allo(self):
		print('nadpisałem allo')
		
	def hi(self):
		print('nadpisałem hi')
		
e = EvenMoreDerivatedClass()
print(type(e))
e.allo()
e.hello()
e.hi()
