#! /usr/bin/env python3

def suma(*args):
	total = 0
	for x in args:
		total += x
	return total
	
print(suma(1))
print(suma(1, 2))
print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
a = [1, 2, 3, 4]
print(suma(*a))
print(suma(*range(11)))

