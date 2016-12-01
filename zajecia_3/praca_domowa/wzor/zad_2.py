class MyIter():
    '''symuluje range'''
    def __init__(self, *args):
        if len(args) == 0:
            raise TypeError('Expected at least 1 argument')
        elif len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError('Expected at most 3 arguments')
        self.curr = self.start

    def __iter__(self):
        self.curr = self.start - self.step
        return self

    def __next__(self):
        self.curr += self.step
        if self.step > 0:
            if self.curr < self.stop:
                return self.curr
            else:
                raise StopIteration
        elif self.step < 0:
            if self.curr > self.stop:
                return self.curr
            else:
                raise StopIteration

assert [x for x in MyIter(0, 10)] == list(range(0, 10))
assert [x for x in MyIter(4)] == list(range(4))
assert [x for x in MyIter(2, 30, 5)] == list(range(2, 30, 5))
assert [x for x in MyIter(-50, -1, 7)] == list(range(-50, -1, 7))

# Bonus:
assert [x for x in MyIter(-1, -50, -7)] == list(range(-1, -50, -7))
