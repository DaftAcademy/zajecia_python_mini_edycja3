#! /usr/bin/env python3

def wszystko(a, b, c=0, d=1, *args, **kwargs):
	print(a)
	print(b)
	print(c)
	print(d)
	print(args)
	print(kwargs)

print(wszystko(1, 2))
print('-' * 80)

print(wszystko(1, 2, 3, 4))
print('-' * 80)

print(wszystko(1, 2, dzielnik=4, dzielna=2))
print('-' * 80)

#TypeError: wszystko() got multiple values for argument 'c'
#print(wszystko(1, 2, 3, 4, 5, c='c', d='d', dzielnik=4, dzielna=2))
print('-' * 80)
