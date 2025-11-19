import os
os.system("cls")


from dataclasses import dataclass

@dataclass

class Paciente:
    nome:str
    idade:str

    def exibir_dados(self):
        print(f"nome: {self.nome} \nidade:{self.idade}")

lista_de_pacientes = []
QUANTIDADE_DE_PACIENTES = 2

for i in range (QUANTIDADE_DE_PACIENTES):
    paciente = Paciente( nome= input("digite seu nome: "),
                        idade=int(input("digite sua idade:")))
    
    
    lista_de_pacientes.append(paciente)
    print()


nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome},{paciente.idade}")
        print("dados salvados com sucesso. ") 



print("\nExibindo lista de pacientes: ") 
for paciente in lista_de_pacientes:
    paciente.exibir_dados()
         
