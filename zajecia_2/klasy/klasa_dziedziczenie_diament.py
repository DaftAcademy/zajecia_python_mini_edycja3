#! /usr/bin/env python3

class A():
	pass
	
class B(A):
	pass

class C(A):
	pass

# Czy D dziedziczy z A tylko poprzez B, tylko poprzez C, a może z obu?
# w python 3 jest to dobrze zdefiniowane, (patrz - MRO)
# Dziedziczenie diamentowe nie jest wydumanym, akademickim przypadkiem, który 
# nie wystepuje w rzeczywistości. 
# Ponieważ każda klasa tworzona przez "użytkownika" dziedziczy po klasie 
#`object` to znaczy, że każde dziedziczenie wilokrotne jest równocześnie 
# diamentowe.
# Nie będziemy w tym kursie zgłębiać tego tematu.
# Ważne, żebyście pamiętali, że dziedziczenie wielokrotne nie jest takie proste
# i może zaskoczyć osoby bez znajomości MRO
class D(B, C):
	pass
	
