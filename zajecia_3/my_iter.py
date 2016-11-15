class MyIter():
    def __init__(self, start=0, end=10):
        print('__init__ called')
        self.start = start
        self.end = end
        self.curr = self.start

    def __next__(self):
        print('__next__ called')
        self.curr += 1
        if self.curr < self.end:
            return self.curr
        else:
            raise StopIteration

    def __iter__(self):
        print ('__iter__ called')
        self.curr = self.start
        return self


my_iter = MyIter(start=0, end=6)
print(type(my_iter))
for i in my_iter:
    print(i)

