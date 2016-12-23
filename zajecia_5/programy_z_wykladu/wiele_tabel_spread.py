import requests

URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{startDate}/{endDate}'

TABLE_TYPE = "C"
START_DATE = '2016-09-01'
END_DATE = '2016-09-06'


formatted_url = URL.format(table=TABLE_TYPE, startDate=START_DATE, endDate=END_DATE)

response = requests.get(formatted_url, params={'format': 'json'})

tables = response.json()
print(len(tables))

head_rate_template = '|{:^20}|{:^5}|{:^10}|{:^10}|{:^10}|'
row_rate_template = '|{currency:^20}|{code:^5}|{bid:^10.6f}|{ask:^10.6f}|{spread:^10.6f}|'
table_header = head_rate_template.format('nazwa', 'kod', 'kupno', 'sprzedaż', 'spread')
line = len(table_header) * '-'

for table in tables:
    rates = table['rates']
    table_name_text = 'Tabela nr:{no} z dnia: {tradingDate}'.format(**table)
    table_name_complete = '|{tnt:^{length}}|'.format(
        length=(len(table_header) - 2),
        tnt=table_name_text
    )
    print(line)
    print(table_name_complete)
    print(line)
    print(table_header)
    print(line)
    rates.sort(key=lambda x: x['code'])
    for rate in rates:
        print(row_rate_template.format(spread=(rate['ask'] - rate['bid']), **rate))
    print(line)
    print('\n')
