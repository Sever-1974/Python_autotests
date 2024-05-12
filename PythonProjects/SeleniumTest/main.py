import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '82'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Python3",
    "photo": "https://dolnikov.ru/pokemons/albums/041.png"
}

body_rename = {
    "pokemon_id": "26961",
    "name": "Python Rename",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokeball = {
    "pokemon_id": "26961",
}

response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)
print(response_create.status_code)

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''
'''message = response_create.json()['message']
print(message)'''

response_rename = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.text)
