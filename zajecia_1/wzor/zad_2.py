#2. Stworzyć listę 100 list, każda z liczbami od 0 do 100.
#Potem dla każdej j-tej z tych list wewnętrznych na jej końcu dodać sumę jej
#pierwszych j elementów.
#spodziewany efekt:
#[
#	[0, 1, 2, 3, ..., 100, 0],
#	[0, 1, 2, 3, ..., 100, 1],
#	[0, 1, 2, 3, ..., 100, 3],
#	...,
#	[0, 1, 2, 3, ..., 100, 5050] # <- tu był błąd powinno być 4950
#]
zero_sto = list(range(101)) # stworzenie listy liczb całkowitych od 0 do 100 włącznie
total = 0
answ = [None] * 100 # stworzenie listy o długości 100
for i in range(100):
    a = zero_sto[:] # skopiownie (shallow) listy zero_sto
    total += i
    a.append(total) # dodanie sumy do listy wewnętrznej
    answ[i] = a # zapisanie listy wewnętrznej pod odpowiednim indeksem
print(answ)
