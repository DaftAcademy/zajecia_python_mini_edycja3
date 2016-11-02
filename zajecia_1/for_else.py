#! /usr/bin/env python3

for x in range(1, 10):
    if x == 10:
        print(x)
        break
else:
    # ten blok kodu wykona się jeśli pętla zakończyła się normalnie
    # (nie za pomocą break)
    print('nie znaleziono')
