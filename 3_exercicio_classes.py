import os
os.system("cls")



from dataclasses import dataclass

@dataclass

class pessoa:
    nome : str
    email: str
    endereco: str


    def dados_entrega(self):
        print(f"nome:{self.nome},endereço:{self.endereco}")



    def dados_email_mariketing(self):
        print(f"nome:{self.nome},email:{self.email}")


pessoa1 = pessoa(nome =input("digite seu nome"),
                 email = input("digite seu email"),
                               endereco =input("digite seu endereço"))



pessoa1.dados_entrega()
pessoa1.dados_email_mariketing()







