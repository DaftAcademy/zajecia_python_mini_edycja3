import requests

URL = "http://api.nbp.pl/api/exchangerates/tables/{table}"

TABLE_TYPE = "C"

XML_HEADER = {'Accept': 'application/xml'}
JSON_HEADER = {'Accept': 'application/json'} 

response = requests.get(URL.format(table=TABLE_TYPE), headers=XML_HEADER, params={'format': 'json'})
print(response)
print(response.headers)
print(response.text)
#print(response.json())
rjson = response.json()
print(type(response.json()[0]))
print(len(rjson))
print(response.request)
print(response.request.url)
print(response.request.headers)
