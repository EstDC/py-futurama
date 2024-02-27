import requests
import random

##Parte1

## Ejercicio 1
def characters():
    url= 'https://futurama-dam.web.app/api/characters'
    response = requests.get(url)
    '''character = {
        "name": data["name"],
        "id": data["id"],
        "status": data["status"],
        "gender": data["gender"],
        "species": data["species"],
      } no me funciona de esta manera'''
    if response.ok:
        data = response.json()
        character  = [item['name'] for item in data['hits']]
        return character
    else:
        return []

##Ejercicio 2
def charactersDead():
    charactersdead = characters() 
    dead = [item['name'] for item in charactersdead if item['status'] == 'DEAD']
    return dead

def charactersByGender(gender): 
    characters = characters()
    filtered = [character['name'] for character in characters if character['gender'] == gender]
    return filtered

print(characters())
print(charactersDead())
print(charactersByGender("FEMALE"))

## Parte 2

##Ejercicio 1
class Futurama:
    def __init__(self):
        self.url = "https://futurama-dam.web.app/api"

    def __str__(self):
        return self.name

    def characters(self):
        url= 'https://futurama-dam.web.app/api/characters'
        response = requests.get(self.url)
        if response.ok:
            data = response.json()
            character  = [item['name'] for item in data['hits']]
            return character
        else:
            return []

    def charactersDead(self):
        characters = self.characters() 
        dead = [item['name'] for item in characters if item['status'] == 'DEAD']
        return dead

    def charactersByGender(self, gender): 
        characters = self.characters()
        filtered = [character['name'] for character in characters if character['gender'] == gender]
        return filtered

    ##Ejercicio 2  
    def humans(self):
        characters = self.characters()
        humans = [character['name'] for character in characters if character['species'] == 'HUMAN']
        return humans
    
    ##Ejercicio 3
    
futurama = Futurama()
print(futurama.characters())
print(futurama.charactersByGender("MALE"))
print(futurama.charactersDead())
print(futurama.humans())




