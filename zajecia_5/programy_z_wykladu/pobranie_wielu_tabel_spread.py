import requests

URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{startDate}/{endDate}/'

TABLE_TYPE = 'C'
start_date = '2016-12-01'
end_date = '2016-12-12'

XML_HEADER = {'Accept': 'application/xml'}
JSON_HEADER = {'Accept': 'application/json'}

r = requests.get(
    URL.format(table=TABLE_TYPE, startDate=start_date, endDate=end_date),
    params={'format': 'json'},
)
parsed_json = r.json()

head_rate_template = '|{:^20}|{:^5}|{:^10}|{:^10}|{:^10}|'
row_rate_template = '|{currency:^20}|{code:^5}|{bid:^10}|{ask:^10}|{spread:^10.6f}|'
table_header = head_rate_template.format('nazwa', 'kod', 'kupno', 'sprzedaż', 'spread')
th_len = len(table_header)
splitter = th_len * '-'

def code_order(x):
    return x['code']

th_template = 'Tabela nr: {no}, z dnia: {tradingDate}'
th_comp_template = '|{tnt:^{length}}|'

for tabela in parsed_json:
    rates = tabela.get('rates', [])
    tnt = th_template.format(**tabela)
    print(splitter)
    print(th_comp_template.format(length=(th_len -2), tnt=tnt))
    print(splitter)
    print(table_header)
    print(splitter)
    

    rates.sort(key=code_order)
    for rate in rates:
        print(row_rate_template.format(spread=(rate['ask'] - rate['bid']), **rate))
    print(splitter)
