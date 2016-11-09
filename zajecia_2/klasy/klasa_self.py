#! /usr/bin/env python3

class MyFirstClass():
	# pierwszy argument jest obowiązkowy, zwyczajowo nazywany self
	def hello(self):
		print("Hello!")
		print(self)
		print(type(self))
		print(id(self))
		
a = MyFirstClass()
a.hello()
# a tu wydarzyło się coś dziwnego, metoda hello przyjmuje jeden argument, nie podaliśmy go.
# A zadziałało, żaden wyjątek nie wyskoczył. Dlaczego?
# https://docs.python.org/3/tutorial/classes.html#method-objects
# pierwszy argument jest przekazywny automatycznie

b = MyFirstClass()
b.hello()

MyFirstClass.hello(a)

print('-' * 80)

print(type(a.hello))
print(type(MyFirstClass.hello))
# pierwszy argument (self) jest konkretną instancją klasy
# When an instance attribute is referenced that isn’t a data attribute, its 
# class is searched. If the name denotes a valid class attribute that is a 
# function object, a method object is created by packing (pointers to) the 
# instance object and the function object just found together in an abstract 
# object: this is the method object. When the method object is called with an 
# argument list, a new argument list is constructed from the instance object 
# and the argument list, and the function object is called with this new 
# argument list.

