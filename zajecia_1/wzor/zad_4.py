##4. Powerset - Napisać kod tworzęcy ze zbioru
##      A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
##	zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A).
##	UWAGA: w python zbiory nie mogą być elementami innych zbiorów,
##      proszę użyć tupli jako zbiorów wewnętrznych

A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
answ = {()} # docelowy zbiór
for x in A: # dla każdego elementu w zbiorze A
    tmp = set() # tworzymy nowy tymczasowy pomocniczy zbiór
    for y in answ: # dla każdego zbioru w zbiorze docelowym
        tmp.add(y + (x, )) # tworzymy nowy podzbiór y rozszerzony o x 
    answ |= tmp # rozszerzamy zbiór docelowy o zbiory w zbiorze tymczasowym
