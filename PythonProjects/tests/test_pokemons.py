import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ada0a5622a33d115d34028881a570a2a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '23677'


def test_status_code():
   response = requests.get(F'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
   assert response.status_code == 200 

def test_part_of_response(): 
   response_get = requests.get(F'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
   assert response_get.json()['data'][0]['trainer_id'] == '23677'
