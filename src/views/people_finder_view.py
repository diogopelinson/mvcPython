import os
from typing import Dict

class PeopleFinderView:
    #Metodo
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar pessoa \n\n')
        name = input('Nome da pessoa: ')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations