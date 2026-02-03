#Modelo do banco de dados a salvar person

class Person:
    def __init__(self, name: str, age: int, height: float) -> None: #Metodo construtor, definir a classe
        self.name = name
        self.age = age
        self.height = height