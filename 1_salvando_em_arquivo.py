import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Paciente:
    nome:str
    idade:str
    peso:str
    altura:str
    cpf:str

    def exibir_dado(self):
        print(f"nome: {self.nome} idade: {self.idade} peso: {self.peso}, altura: {self.altura} cpf:{self.cpf}")





lista_de_pacientes = []
QUANTIDADE_DE_PACIENTE = 2

for i in range(QUANTIDADE_DE_PACIENTE):
    pacinte = Paciente(nome = input("digite seu nome: "),idade = input("digite sua idade: "),peso = input("digite seu peso: "), altura = input("digite sua altura: "),cpf = input("digite seu cpf: "))
    lista_de_pacientes.append(pacinte)
    print()



nome_do_arquivo = "dados_paciente.csv"

with open(nome_do_arquivo, "a")as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"nome: {paciente.nome}, idade: {paciente.idade}, peso: {paciente.peso}, altura:{pacinte.altura} cpf: {pacinte.cpf} ")



print("dados salvados com sucesso") 


print("\nExivindo todos os pacientes: ")
try:
    # "r" -  read - leitura
    with open(nome_do_arquivo,"r",encoding="uft8") as arquivo:
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade = paciente.strip().split(",")
            paciente = Paciente(nome, idade, peso, altura, cpf)

            
            print(f"- {paciente.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado")
