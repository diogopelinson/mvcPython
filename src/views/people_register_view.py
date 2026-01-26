import os
from typing import Dict

class PeopleRegisterView:
    #Metodo
    #Pagina inicial da feature
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
    
    #Pagina de sucesso
    def registry_person_sucess(self, message: Dict) -> None:
        os.system('cls||clear')

        sucess_message = f'''
            Usuario Cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos: 
                Nome: { message["attributes"]["name"] }
                Idade: { message["attributes"]["age"] }
        '''
        print(sucess_message)

    #Pagina da falha
    def registry_person_fail(self, error: str) -> None:
        os.system('cls||clear')

        fail_message = f'''
            Falha ao Cadastrar usuario!

            Erro: { error }
        '''
        print(fail_message)