print('Starting program...')

import requests

pagina = requests.get("https://catfact.ninja/facts")

feiten = pagina.json()

print(feiten["data"][0]["fact"])