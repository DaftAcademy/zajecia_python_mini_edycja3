Zadanie 1
Stworzyć klasę `NbpTableC(date_from, date_to)`.
date_from - obiekt datetime.date
date_to - obiekt datetime.date
Klasa pobierze kursy walut (tabela C) w podanym przedziale czasu ze strony NBP(przy wykorzystaniu API).

Klasa ma mieć metodę `to_csv(buy_file_name, sell_file_name)`
Zadaniem tej metody będzie zapisanie pobranych kursów walut do plików csv.
date_from włącznie
buy_file_name włącznie
Kursy kupna do buy_file_name
Kursy sprzedaży do sell_file_name

wymagany format plików csv:
* w pierwszej kolumnie symbole walut posortowane alfabetycznie (A-Z),
* poźniej w każdej następnej kolumnie kolejna data z zakresu i kurs kupna/sprzedaży zaokrąglony do 4 miejsc po przecinku,
* separator pól - średnik `;`

Przykład pliku csv z dwoma walutami i zmyślonymi wartościami
```
;21.12.2016;22.12.2016
EUR;3,4567;3,5466
USD;3,5456;3,5345
```

Dodatkowo klasa powinna mieć metody:
* `max_buy(currency)` - zwróci datę najwyższego notowania (kupno) danej waluty (USD, EUR, ...)
* `max_sell(currency)` - zwróci datę najniższego notowania  (kupno)danej waluty (USD, EUR, ...)
* `min_buy(currency)` - zwróci datę najwyższego notowania (sprzedaż) danej waluty (USD, EUR, ...)
* `min_sell(currency)` - zwróci datę najniższego notowania (sprzedaż) danej waluty (USD, EUR, ...)


Bonus: 
Jeśli chcielibyśmy rozszerzać zakres danych (dodatkowe przedziały czasu) to w jaki sposób optymalnie przechowywać już pobrane dane tak aby przy rozszerzaniu wysyłać minimalną ilość zapytań?
Przedziały czasu mogły by się nie stykać, być bardzo długie lub tylko jednodniowe.
Problem nie jest oczywisty.
(do przemyślenia, nie ma potrzeby implementacji)

Zadanie 2
Zadanie jest przekrojowe, trzeba wykorzystać materiały z kilku zajęć.
Proszę zamimplementować dwie klasy:
1. `MyDateTime`
2. `MyTimeDelta`

Na potrzeby zadania proszę założyć:
* dzień ma 24 godziny
* godzina ma 60 minut
* minuta ma 60 sekund

Klasa `MyDateTime` ma reprezentować punkt w czasie (rok, miesiąc, dzień,
 godziny, minuty, sekundy) w kalendarzu gregoriańskim.
Ograniczenia:
* 1 <= rok <= 9999
* 1 <= miesiąc <= 12
* 1 <= dzień <= 28 dla miesiąca 2 w zwykłym roku
* 1 <= dzień <= 29 dla miesiąca 2 w roku przestępnym
* 1 <= dzień <= 30 dla miesięcy nr: 1, 3, 5, 7, 8, 10, 12
* 1 <= dzień <= 31 dla pozostałych miesięcy
* 0 <= godziny <= 23
* 0 <= minuty <= 59
* 0 <= sekundy <= 59
* rok, miesiąc, dzień, godziny, minuty, sekundy muszą być liczbami całkowitymi

Klasa `MyDateTime` powinna obsługiwać:
* `==` - dwa obiekty `MyDateTime` są sobie równe jeśli mają ten sam rok, mesiąc, dzień, godzinę, minutę, sekundę
`Wskazówka: https://docs.python.org/3/library/functions.html#all`
* `+` - dodawanie `MyTimeDelta` powinno stworzyć nowy obiekt `MyDateTime`
* `+=` - zwiększenie wartości obecnego obiektu o `MyTimeDelta`
* `-` - odejmowanie dwóch obiektów `MyDateTime` powinno zwracać obiekt
 `MyTimeDelta` zawierający dokładną różnicę czasu (dni, sekund).
* "udawanie" słownika, po to aby można było pobrać rok, dzień, miesiąc godzinę,
 minutę i sekundy za pomocą operatora `[]`
 a także aby dało się obiekt `MyDateTime` rozpakować za pomocą `**`,
 (w sekcj assertów są przykłady użycia)
```
Wskazówka: `https://docs.python.org/3.5/reference/datamodel.html#object.__getitem__`
Wskazówka: `https://docs.python.org/3.5/library/stdtypes.html#dict.keys`
Wskazówka: `http://stackoverflow.com/questions/8601268/python-class-that-acts-as-mapping-for-unpacking/8601389#8601389`
```
* nadpisana metoda `__str__` powinna zwracać string w formacie `rok-miesiąc-dzień godzina:minuta:sekunda`
na rok są przeznaczone 4 miejsca (w razie potrzeby z lewej strony wypełnione zerami)
na pozostałe wartości 2 miejsca (w razie potrzeby z lewej strony wypełnione zerami)
* nadpisana metoda `__repr__`, powinna działać tak, że jej wynik przekazany do 
funkcji `eval()` stworzy obiekt równy pierwotnemu
Wskazówka: https://docs.python.org/3/library/functions.html#eval

```
a = MyDateTime(2016, 12, 13, 14, 21, 4)
assert '4, 21, 14, 13, 12, 2016' == '{second}, {minute}, {hour}, {day}, {month}, {year}'.format(**a)
assert '2016-12-13 14:21:04' == str(a)
assert 'MyDateTime(year=2016, month=12, day=13, hour=14, minute=21, second=4)' == repr(a)
assert 4 == a['second']
assert 21 == a['minute']
assert 14 == a['hour']
assert 13 == a['day']
assert 12 == a['month']
assert 2016 == a['year']

b = MyDateTime(year=1, month=2, day=3, hour=4, minute=5, second=6)
assert '6, 5, 4, 3, 2, 1' == '{second}, {minute}, {hour}, {day}, {month}, {year}'.format(**b)
assert '0001-02-03 04:05:06' == str(b)
assert 'MyDateTime(year=1, month=2, day=3, hour=4, minute=5, second=6)' == repr(b)
assert 6 == b['second']
assert 5 == b['minute']
assert 4 == b['hour']
assert 3 == b['day']
assert 2 == b['month']
assert 1 == b['year']

c = MyDateTime(year=9999, month=12, day=31)
assert '0, 0, 0, 31, 12, 9999' == '{second}, {minute}, {hour}, {day}, {month}, {year}'.format(**c)
assert '9999-12-31 00:00:00' == str(c)
assert 'MyDateTime(year=9999, month=12, day=31, hour=0, minute=0, second=0)' == repr(c)
assert 0 == c['second']
assert 0 == c['minute']
assert 0 == c['hour']
assert 31 == c['day']
assert 12 == c['month']
assert 9999 == c['year']

d = MyDateTime(year=2016, month=12, day=13, hour=14, minute=21, second=4)
assert a == d
assert d == a
assert a != b
assert a != c

e = eval(repr(a))
assert a == e
assert e == d
```

UWAGA na sposoby przeliczania lat przestępnych!
 
Klasa `MyTimeDelta` ma reprezentować przesunięcie czasu (dni, sekundy).
Tworzenie obiektu `MyTimeDelta` powinno pozwalać na podanie liczby: tygodni, 
dni, godzin, minut, sekund
Ograniczenia:
* tygodnie, dni, godziny, minuty, sekundy powinny być liczbami całkowitymi

wewnętrzna reprezentacja danych powinna normalizować: tygodnie, dni, godziny,
 minuty, sekundy do:
* `0 <= sekundy < 3600*24`
* `-999999999 <= dni <= 999999999`
Wskazówka: https://docs.python.org/3/library/functions.html#divmod

Klasa `MyTimeDelta` powinna obsługiwać
* `+` dodawanie dwóch obiektów `MyTimeDelta` powinno stworzyć nowy obiekt 
`MyTimeDelta`
* `+=` zwiększenie wartości obiektu `MyTimeDelta` o drugi obiekt `MyTimeDelta` 
powinno zmodyfikować pierwszy obiekt
* `-` odejmowanie dwóch obiektów `MyTimeDelta` powinno stworzyć nowy obiekt 
`MyTimeDelta`
* `-=` zmniejszenie wartości obiektu `MyTimeDelta` o drugi obiekt `MyTimeDelta`
 powinno zmodyfikować pierwszy obiekt
* `*` mnożenie obiektu `MyTimeDelta` przez liczbę całkowitą powinno stworzyć 
nowy obiekt `MyTimeDelta`
* `*=` zwiększenie wartości obiektu `MyTimeDelta` o drugą liczbę całkowitą
 powinno zmodyfikować pierwszy obiekt

UWAGA przesunięcia w czasie mogą być ujemne! 

```
ta = MyTimeDelta(seconds=-1)
assert 'MyTimeDelta(days=-1, seconds=86399)' == repr(ta)
        
ta = MyTimeDelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
assert 'MyTimeDelta(days=8, seconds=3661)' == repr(ta)

tb = MyTimeDelta(weeks=7, days=12, hours=23, minutes=59, seconds=1)
assert 'MyTimeDelta(days=61, seconds=86341)' == repr(tb)

tc = ta + tb
assert 'MyTimeDelta(days=70, seconds=3602)' == repr(tc)

td = ta * 2
assert 'MyTimeDelta(days=16, seconds=7322)' == repr(td)

te = tb * 2
assert 'MyTimeDelta(days=123, seconds=86282)' == repr(te)

tf = 2 * ta
assert 'MyTimeDelta(days=16, seconds=7322)' == repr(tf)

tg = 2 * tb
assert 'MyTimeDelta(days=123, seconds=86282)' == repr(tg)

ta *= 2
assert 'MyTimeDelta(days=16, seconds=7322)' == repr(ta)

tb *= 2
assert 'MyTimeDelta(days=123, seconds=86282)' == repr(tb)

ta = MyTimeDelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
tb = MyTimeDelta(weeks=7, days=12, hours=23, minutes=59, seconds=1)
ta += tb
assert 'MyTimeDelta(days=70, seconds=3602)' == repr(ta)

ta = MyTimeDelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
tc = ta - tb
assert 'MyTimeDelta(days=-54, seconds=3720)' == repr(tc)
td = tb - ta
assert 'MyTimeDelta(days=53, seconds=82680)' == repr(td)
```
```
# połączone MyDateTime i MyTimeDelta
a = MyDateTime(2016, 12, 13, 14, 21, 4)
ta = MyTimeDelta(seconds=1)
b = a + ta
c = ta + a
assert a == MyDateTime(2016, 12, 13, 14, 21, 4)
assert b == c
assert MyDateTime(2016, 12, 13, 14, 21, 5) == b

a = MyDateTime(2016, 12, 13, 14, 21, 4)
ta = MyTimeDelta(days=-1, seconds=-1)
b = a + ta
c = ta + a
assert a == MyDateTime(2016, 12, 13, 14, 21, 4)
assert b == c
assert b == MyDateTime(2016, 12, 12, 14, 21, 3)

# Testy z wykorzystaniem datetime i timedelta
import datetime


def compare_datetime(first, second):
    assert first.year == second.year
    assert first.month == second.month
    assert first.day == second.day
    assert first.hour == second.hour
    assert first.minute == second.minute
    assert first.second == second.second

    
def compare_timedelta(first, second):
    assert first.days == second.days
    assert first.seconds == second.seconds

    
def test_datetime_and_timedelta_add(dt_kwargs, td_kwargs):
    a = MyDateTime(**dt_kwargs)
    oa = datetime.datetime(**dt_kwargs)
    ta = MyTimeDelta(**td_kwargs)
    ota = datetime.timedelta(**td_kwargs)
    b = a + ta
    c = ta + a
    ob = oa + ota
    oc = ota + oa
    assert b == c
    assert ob == oc
    compare_datetime(a, oa)
    compare_timedelta(ta, ota)
    compare_datetime(b, ob)
    compare_datetime(c, oc)
    
test_datetime_and_timedelta_add(
    dt_kwargs={'year': 2016, 'month': 12, 'day': 13, 'hour': 14, 'minute': 21, 'second': 4},
    td_kwargs={'days': -13, 'seconds': -(14*3600 + 21*60 +5)}
)

test_datetime_and_timedelta_add(
    dt_kwargs={'year': 2016, 'month': 12, 'day': 13, 'hour': 14, 'minute': 21, 'second': 4},
    td_kwargs={'days': -13, 'seconds': -(30*24*3600 + 14*3600 + 21*60 +5)}
)

test_datetime_and_timedelta_add(
    dt_kwargs={'year': 2016, 'month': 12, 'day': 13, 'hour': 14, 'minute': 21, 'second': 4},
    td_kwargs={'days': -13, 'seconds': -(28*24*3600 + 14*3600 + 21*60 +5)}
)

def test_datetime_and_timedelta_sub(dt_kwargs_a, dt_kwargs_b):
    a = MyDateTime(**dt_kwargs_a)
    oa = datetime.datetime(**dt_kwargs_a)
    b = MyDateTime(**dt_kwargs_b)
    ob = datetime.datetime(**dt_kwargs_b)
    tab = a - b
    tba = b - a
    otab = oa - ob
    otba = ob - oa
    compare_datetime(a, oa)
    compare_datetime(b, ob)
    compare_timedelta(tab, otab)
    compare_timedelta(tba, otba)
    
test_datetime_and_timedelta_sub(
    dt_kwargs_a={'year': 2016, 'month': 12, 'day': 13, 'hour': 14, 'minute': 21, 'second': 4},
    dt_kwargs_b={'year': 2016, 'month': 12, 'day': 13, 'hour': 14, 'minute': 21, 'second': 4}
)
```