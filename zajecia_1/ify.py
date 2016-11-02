#! /usr/bin/env python3
# to jest linia komentarza
# Python 3 zakłada, że pliki z kodem źródłowym są zapisane w formacie UTF-8
# można wtedy bez problemów używać literałów ze znakami spoza ACII
# nawet zmienne mogą zawierać "ogonki", co nie znaczy, że jest to dobra praktyka
ąę = 3
print('przed ifem')
if ąę == 3:
    # tu jest wcięcie w kodzie, standardowo 4 spacje na poziom zagnieżdżenia
    # nie ma żadnych nawiasów {}, żadnego BEGIN, END
    # tylko obowiązkowe wcięcia
    # dzięki temu sam język wymusza czytelne formatowanie kodu
    # jest to jedna z większych zalet pythona
    print('warunek spełniony!')
print('i już po ifie')
