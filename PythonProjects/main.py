import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ada0a5622a33d115d34028881a570a2a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Anita",
    "photo_id": 115
}

body_put = {
    "pokemon_id": "267973",
    "name": "New Name",
    "photo_id": 115
}

"""response_create = requests.post(F'{URL}/pokemons', headers = HEADER,  json = body_create)
print(response_create.text)"""
'''message = response_create.json()['message']
print(message)'''

response_put = requests.put(F'{URL}/pokemons', headers = HEADER,  json = body_put)
print(response_put.json)