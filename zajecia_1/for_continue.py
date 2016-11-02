#! /usr/bin/env python3

# range to generator (będziemy o nich poźniej szczegółowo powiadać)
# w skrócie: da się po nim iterować
# podaje kolejne liczby całkowite od, do, skok
# od - domyślnie 0
# do - trzeba podać, pierwsza liczba której range nie zwróci
# skok - domyślnie 1

for x in range(10):
    if x % 2 != 0:
        continue
    print(x)
