




from dataclasses import dataclass

@dataclass
class pessoa:
    nome :str
    email : str
    telefone : str
    endereço : str

    def mostrar_dados(self):
        print(f"nome:{pessoa1.nome} email:{pessoa1.email} telefone:{pessoa1.telefone} endereço: {pessoa1.endereço} ")


    



pessoa1 =pessoa(nome =input("digite seu nome"),
                email =input("digite seu e-mail: "),
                telefone = input("digite seu telefone"),
                endereço =input("digite seu endereço"))


pessoa1.mostrar_dados()