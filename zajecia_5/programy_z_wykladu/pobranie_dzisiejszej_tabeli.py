import requests

URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}'

TABLE_TYPE = 'C'

XML_HEADER = {'Accept': 'application/xml'}
JSON_HEADER = {'Accept': 'application/json'}

r = requests.get(
    URL.format(table=TABLE_TYPE),
    params={'format': 'json'},
)
parsed_json = r.json()

print(len(parsed_json))
tabela = parsed_json[0]
print(type(tabela))
print(tabela.keys())
print(tabela.get('effectiveDate', ''))
print(tabela.get('table', ''))

head_rate_template = '| {:^20} | {:^5} | {:^10} | {:^10} |'
row_rate_template = '| {currency:^20} | {code:^5} | {bid:^10} | {ask:^10} |'
table_header = head_rate_template.format('nazwa', 'kod', 'kupno', 'sprzedaż')
th_len = len(table_header)
splitter = th_len * '-'
print(splitter)
print(table_header)
print(splitter)
rates = tabela.get('rates', [])

def code_order(x):
    return x['code']

rates.sort(key=code_order)
for rate in rates:
    print(row_rate_template.format(**rate))
print(splitter)
