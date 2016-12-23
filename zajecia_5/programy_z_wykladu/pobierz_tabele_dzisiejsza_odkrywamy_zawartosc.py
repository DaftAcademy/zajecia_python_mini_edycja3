import requests

URL = "http://api.nbp.pl/api/exchangerates/tables/{table}"

TABLE_TYPE = "C"


response = requests.get(URL.format(table=TABLE_TYPE), params={'format': 'json'})

rtable = response.json()

table = rtable[0]
print(table)
print('table type: {}'.format(table['table']))
rates = table['rates']
head_rate_template = '| {:^20} | {:^5} | {:^10} | {:^10} |'
row_rate_template = '| {currency:^20} | {code:^5} | {bid:^10} | {ask:^10} |'
table_header = head_rate_template.format('nazwa', 'kod', 'kupno', 'sprzedaż')
print(len(table_header) * '-')
print(table_header)
print(len(table_header) * '-')
rates.sort(key=lambda x: x['code'])
for rate in rates:
    print(row_rate_template.format(**rate))
print(len(table_header) * '-')
