import os
os.system("cls")



from dataclasses import dataclass

@dataclass


class pessoa:
    nome : str
    email : str
    endereco : str


    def mostrar_dado(self):
        print(f"nome:{self.nome},emai:{self.email},endereço:{self.endereco}")
    def mostrar_somente_nome(self):
        print(f"nome:{self.nome}")



pessoa1 = pessoa(nome = input("digite seu nome:"),
                 email = input("digite seu email: "),
                 endereco = input("digite seu endereço: "))

pessoa2 = pessoa(nome = input("digite seu nome:"),
                 email = input("digite seu email: "),
                 endereco = input("digite seu endereço: "))



pessoa1.mostrar_dado()
pessoa1.mostrar_somente_nome()
pessoa2.mostrar_dado()
pessoa2.mostrar_somente_nome()








