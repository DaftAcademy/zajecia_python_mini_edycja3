#! /usr/bin/env python3

class A():
	def aaa(self):
		print('A - aaa')
		
	def hello(self):
		print('A - hello')
	
class B():
	def bbb(self):
		print('B - bbb')
		
	def hello(self):
		print('B - hello')
	
class C():
	def ccc(self):
		print('C - ccc')
		
	def hello(self):
		print('C - hello')

# tak zapisujemy dziedziczenie wielokrotne
class D(A, B, C):
	pass
	
	
d = D()
print(type(d))
# to z której klasy bazowej metoda zostanie wywołana zależy od kolejności
# dziedziczenia
d.hello()
d.aaa()
d.bbb()
d.ccc()
