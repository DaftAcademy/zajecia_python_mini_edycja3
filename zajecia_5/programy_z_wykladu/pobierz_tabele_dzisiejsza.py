import requests

URL = "http://api.nbp.pl/api/exchangerates/tables/{table}?format=json"

TABLE_TYPE = "C"

XML_HEADER = {'Accept': 'application/xml'}
JSON_HEADER = {'Accept': 'application/json'} 

response = requests.get(URL.format(table=TABLE_TYPE), headers=XML_HEADER)
print(response)
print(response.headers)
print(response.text)
#print(response.json())

print(response.request)
print(response.request.headers)
