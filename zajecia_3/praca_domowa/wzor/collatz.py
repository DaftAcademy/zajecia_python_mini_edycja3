def collatz_gen(start):
    yield start
    while start != 1:
        if start % 2 == 1:
            start = 3 * start + 1
        else:
            start = int(start / 2)
        yield start
    raise StopIteration

assert list(collatz_gen(1)) == [1]
assert list(collatz_gen(2)) == [2, 1]
assert list(collatz_gen(3)) == [3, 10, 5, 16, 8, 4, 2, 1]
assert list(collatz_gen(12)) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert list(collatz_gen(19)) == [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

