import requests
from rich.pretty import pprint

# Request Xwing in swapi.dev
response = requests.get("https://swapi.dev/api/starships/12")
pprint(response.json())
