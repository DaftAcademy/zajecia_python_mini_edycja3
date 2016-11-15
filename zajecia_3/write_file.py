def inf_fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a, b = b, c

with open('fib_100.txt', 'w') as f:
    fib = inf_fib()
    for i in range(100):
        number = next(fib)
        f.write(str(number)) # nie dodaje końców linii
        f.write('\n')
