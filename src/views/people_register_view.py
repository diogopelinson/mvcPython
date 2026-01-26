import os
from typing import Dict

class PeopleRegisterView:
    #Metodo
    def registry_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Cadastrar Nova Pessoa \n\n')

        name = input('Determine o nome: ')
        age = input('Determine a idade: ')
        height = input('Determine a altura: ')

        new_person_informations = {
            "name": name,
            "age": age,
            "height": height
        }

        return new_person_informations