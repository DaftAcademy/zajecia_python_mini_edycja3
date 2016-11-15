f = open('sample_file', 'r') # otwiera plik w trybie tekstowym do odczytu
print(type(f))

b = f.read()
print(type(b))
print(len(b))
print('b: {}'.format(b))

c = f.read()
print(type(c))
print(len(c)) # 0 bo plik jest już 'przeczytany'
print('c: {}'.format(c))

f.seek(0) # ustawi nam wskaźnik pliku na początek

d = f.read()
print(type(d))
print(len(d))
print('d: {}'.format(d))

# read jest słaby do większych plików - wczytuje cały plik na raz do pamięci

# po skończonej pracy należy plik zamknąć
f.close()

