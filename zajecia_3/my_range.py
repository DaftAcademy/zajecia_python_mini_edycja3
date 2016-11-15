# praca_domowa przerobić my_range tak, żeby wywołanie odpowiadało range

def my_range(start, stop, step=1):
    curr = start
    while curr < stop:
        yield curr
        curr += step


for i in my_range(0, 10, 3):
    print(i)

print(type(my_range))
mr = my_range(0, 4)
print(type(mr))
print(mr.__next__())
print(mr.__next__())
print(mr.__next__())
print(mr.__next__())
print(mr.__next__())

