import os
os.system("cls")


from dataclasses import dataclass


@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa(nome = input("digite seu nome: "),
                 idade =int(input("digite sua idade: ")),
                 
                 peso = float(input("digite seu peso: ")),
                 altura =float(input("digite sua altura: ")) )




print("exibindo dados da pessoa. ")


print(f"Nome:{pessoa1.nome},idade:{pessoa1.idade} anos ,peso:{pessoa1.peso}kg ,altura:{pessoa1.altura}metros")



