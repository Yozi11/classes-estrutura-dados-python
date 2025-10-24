import os
os.system("cls")

from dataclasses import dataclass


@dataclass

class Pessoa:
    nome:str
    idade:int
    peso:float
    altura:float
    
    
    
    def mostrar_dados(self):
        print(f"nome:{self.nome},idade:{self.idade},peso:{self.peso},altura:{self.altura}")
        
        
        
lista_de_pessoas = []


for i in range(4):
    dados_da_pessoa = Pessoa(nome=input("digite seu nome: "),idade = input("digite sua idade"),peso = input("digite seu peso:"),altura = input("digite sua altura: "))
    lista_de_pessoas.append(dados_da_pessoa)


for pessoa in lista_de_pessoas:
    pessoa.mostrar_dados()            