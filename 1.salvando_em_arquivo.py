import os 
from dataclasses import dataclass

@dataclass

class Aluno:
    nome:str
    idade:int
    email:str
    telefone:str


QUANTIDADE_ALUNOS = 2

lista_alunos = []


print("solicitando dados do aluno.")

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(nome =(input("digite seu nome")),
                  idade=input("digite sua idade:"),
                  email=input("digite seu email: "),
                  telefone=input("digite seu telefone: "))
   
    lista_alunos.append(aluno)


print()
print("salvando dados.")
arquivo = "dados_alunos.txt"
with open(arquivo,"a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome},{aluno.idade},{aluno.email},{aluno.telefone}\n")
        print("salvo com sucesso!")   