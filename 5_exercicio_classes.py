import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Pessoa:
    nome: str
    cpf: str
    telefone: str
    
    
    def mostrar_dados(self):
        print(f"nome:{self.nome},cpf:{self.cpf},telefone:{self.telefone}")
    def dados_sms_marketing(self):
        
        print(f"telefone:{self.telefone}")
    
    
lista_de_pessoas = []
    
for i in range(3):
    dados_da_pessoa = Pessoa(nome = input("digite seu nome:"),
                             cpf =input("digite seu cpf: "),
                             telefone = input("digite seu telefone: "))
    lista_de_pessoas.append(dados_da_pessoa)
        
        
        
        
        
for pessoa in lista_de_pessoas:
    pessoa.mostrar_dados()
    