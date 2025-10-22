import os
os.system("cls")

from dataclasses import dataclass

#estrutura de dados:classe
@dataclass
class pessoa:
    nome: str
    idade: int
    cpf:str


@dataclass
class pet:
    nome: str
    idade: int
    peso: float

#exemplo de uso da classe
pessoa1 = pessoa(nome="marta",cpf="121342",idade=20)

pet1 = pet(nome="toto",idade="4",peso=2.100)


print("exibindo dados da pessoa. ")

print(f"Nome:{pessoa1.nome}, idade: {pessoa1.idade}cpf:{pessoa1.cpf}")
      
      

print(f"Nome: {pet1.nome}, idade: {pet1.idade}peso:{pet1.peso}")

