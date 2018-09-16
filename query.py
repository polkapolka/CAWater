import requests

resource_id = 'f739e3f1-166f-48c7-afe7-9e69a4e9363d'

#  https://data.ca.gov/api/action/datastore/search.json?resource_id=f739e3f1-166f-48c7-afe7-9e69a4e9363d&limit=5

api_endpoint = 'https://data.ca.gov/api/action/datastore/search.json'
params = {'resource_id':resource_id,'limit':5}

response = requests.get(api_endpoint, params)

df = response.json()

#headers = df['result']['fields']
#data = df['result']['records']