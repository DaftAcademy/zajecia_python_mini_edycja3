#! /usr/bin/env python3

def power(a, b):
	print('podniosę {} do potęgi {}'.format(a, b))
	return a**b
	
print(power(2, 3))
print(power(4, 5))

# tu nie ma nawiasów () - i to jest ważne, dzięki temu do cos_innego zapisujemy
# obiekt funkcji a nie jej wynik (wartość zwróconą)
cos_innego = power

print(power(2, 3))

print(type(power))
print(type(cos_innego))
print(power is cos_innego)

kolejka = [power, cos_innego]

print('start pętli')
for x in kolejka:
	print(x(2, 10))
