import os
os.system("cls")



from dataclasses import dataclass

@dataclass


class Endereco:
    logradouro: str
    numero: int
    cidade:str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco
    
    
    def mostrar_dados(self):
        print(f"nome:{self.nome},{self.endereco},email:{self.email},")
        
    
        
     
cliente1 = Cliente(nome = input("digite seu nome:"),
                   email = input("digite seu email: "), 
                   endereco=Endereco(
                   logodouro =input("digite seu logodouro: ")),


                   numero =(int(input("digite seu numero: "))))
                

cliente1.mostrar_dados()
print("mostrar dados do cliente.")