import os
os.system("cls")

# texto que eu quero salvar.
texto = input("digite seu nome: ")


# definir nome do arquivo para salvar.

nome_arquivo = "exemplo.txt"

#comando para salvar
with open(nome_arquivo, "a")as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("salvo com sucesso!")

