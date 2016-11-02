#! /usr/bin/env python3

# proste wyznaczanie liczb pierwszych (niezbyt wydajne)
limit = 100
# skok = 2 <- omijamy liczby parzyste, które i tak nie są pierwsze
for n in range(3, limit, 2):
    sqrt_n = int(n**0.5) + 1
    q = 2
    while q <= sqrt_n:
        if n % q == 0:
            break
        q += 1
    else:
        print(n, ' jest liczbą pierwszą')
