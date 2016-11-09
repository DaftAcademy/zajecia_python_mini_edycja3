#! /usr/bin/env python3

def pierwsza_funkcja():
	# a jest w tym miejscu zmienną lokalną - widzialną tylko w obrębie tej funkcji
	a = 1 + 2
	
a = pierwsza_funkcja()
print(a)
print(type(a))

