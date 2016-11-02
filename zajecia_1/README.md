1. W pliku notatki.txt jest szczegółowy plan wykładu razem z przykładami z interpretera.
Kolejność programów wg wykładu:
    + ify.py
    + if_else.py
    + if_elif_else.py
    + for.py
    + for_string.py
    + for_continue.py
    + for_break.py
    + for_else.py
    + while.py

2. Na rozwiązania prac domowych czekamy do 06.11.2016 włącznie:
    1. Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według schematu:
	[[0], [2], ... , [98]]


    2. Stworzyć listę 100 list, każda z liczbami od 0 do 100.
Potem dla każdej j-tej z tych list wewnętrznych na jej końcu dodać sumę jej pierwszych j elementów.
spodziewany efekt:
[
	[0, 1, 2, 3, ..., 100, 0],
	[0, 1, 2, 3, ..., 100, 1],
	[0, 1, 2, 3, ..., 100, 3],
	...,
	[0, 1, 2, 3, ..., 100, 5050]
]

    3. Napisać kod transformujący podany słownik:
	{
		1: 'Poniedziałek',
		2: 'Wtorek',
		3: 'Środa',
		4: 'Czwartek',
		5: 'Piątek',
		6: 'Sobota',
		7: 'Niedziela',
	}
	do postaci:
	{
		'Poniedziałek': 1,
		'Środa': 3,
		'Piątek': 5,
		'Niedziela': 7,
	}
	Zamiana klucza z wartością i zostawienie tylko dni nieparzystych
	
    4. Powerset - Napisać kod tworzęcy ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A).
	UWAGA: w python zbiory nie mogą być elementami innych zbiorów, proszę użyć 
	tupli jako zbiorów wewnętrznych
