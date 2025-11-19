import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Usuario:
    nome:str
    data_de_nascimento:str
    rg:str
    cpf:str


def exibir_dados(self):
    print(f"nome: {self.nome} data de nascimento: {self.data_de_nascimento} rg: {self.rg} cpf: {self.cpf} ")

lista_de_usuarios = []
QUANTIDADE_DE_USUARIOS = 5


for i in range(QUANTIDADE_DE_USUARIOS):
    usuario = Usuario(nome = input("digite seu nome: "),data_de_nascimento = input("digite sua data de nascimento: "),rg = input("digite seu rg"),cpf =input("digite seu cpf"))
    lista_de_usuarios.append(usuario)
    print()


nome_do_arquivo = "dados_paciente2.csv"


with open(nome_do_arquivo,"a")as arquivo_usuarios:
    for usuario in lista_de_usuarios:
        arquivo_usuarios.write(f"nome: {usuario.nome}, data de nascimento: {usuario.data_de_nascimento},rg: {usuario.rg}, cpf: {usuario.cpf}")

print()
        
