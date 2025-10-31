import os
os.system("cls")

from dataclasses import dataclass

@dataclass

class Livros:
    nome:str
    autor:str
    categoria:str
    preço:str

QUANTIDADE_LIVROS = 3

lista_livros = []

for i in range(QUANTIDADE_LIVROS):
    livros = Livros(nome=(input("digite o nome do livro: ")),
                    autor =input("digite o nome do autor: "),
                    categoria =input("digite a categoria: "),
                    preço = input("digite o preço:R$ "))
    lista_livros.append(livros)



print()

print("salvando dados. ")

arquivo = "dados_livros.txt"

with open(arquivo,"a") as arquivo_livros:
    for livro in lista_livros:
        arquivo_livros.write(f"{livro.nome},{livro.autor},{livro.categoria},{livro.preço}\n")
        print("salvo com sucesso!")


