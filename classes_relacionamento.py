import os 
from dataclasses import dataclass

os.system("cls")


@dataclass

class Endereco:
    logradouro: str
    numero: int
    
    
    
    
@dataclass
class Cliente:
    nome: str
    endereco: Endereco
        

cliente1 = Cliente(nome ="Marta",
                  endereco=Endereco
                  (logradouro="Rua A",
                   numero=23))

print(f"nome:{cliente1.nome},endereço:{cliente1.endereco.logradouro},numero:{cliente1.endereco.numero}")

    