#! /usr/bin/env python3

def iloraz(**kwargs):
	print(type(kwargs))
	print(kwargs)
	dzielna = kwargs.pop('dzielna', 0)
	dzielnik = kwargs.pop('dzielnik', 1)	
	return dzielna/dzielnik
	
#print(iloraz(2, 4))
print(iloraz(dzielnik=4, dzielna=2))
print('-' * 80)
print(iloraz(dzielnik=4))
a = {'dzielna': 2, 'dzielnik': 3}
print(iloraz(**a))

