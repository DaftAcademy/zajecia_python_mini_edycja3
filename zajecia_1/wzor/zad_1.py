#1. Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według
#schematu:
#	[[0], [2], ... , [98]]
a = [[x] for x in range(0, 100, 2)]
print(a)
