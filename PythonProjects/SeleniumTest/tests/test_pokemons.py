import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '82'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2285'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Python Rename'

def test_status_code_trainer():
    response_trainer = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_trainer.status_code == 200
    assert response_trainer.json()['data'][0]['trainer_name'] == 'Celtus74'

@pytest.mark.parametrize('key, value', [('name','Python Rename'),('trainer_id',TRAINER_ID),('id','27015')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value
