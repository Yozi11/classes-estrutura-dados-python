import csv
from dataclasses import dataclass, asdict

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

def salvar_funcionarios(funcionarios, filename="Funcionarios.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['nome', 'data_nascimento', 'rg', 'cpf'])
        writer.writeheader()
        for func in funcionarios:
            writer.writerow(asdict(func))

def ler_funcionarios(filename="Funcionarios.csv"):
    funcionarios_lidos = []
    with open(filename, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            funcionarios_lidos.append(Funcionario(**row))
    return funcionarios_lidos

# Programa principal
funcionarios = []
for i in range(5):
    print(f"Digite os dados do funcionário {i+1}:")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    funcionarios.append(Funcionario(nome, data_nascimento, rg, cpf))

salvar_funcionarios(funcionarios)

print("\nFuncionários salvos. Lendo do arquivo Funcionarios.csv:\n")
funcionarios_lidos = ler_funcionarios()
for f in funcionarios_lidos:
    print(f"Nome: {f.nome}, Data de nascimento: {f.data_nascimento}, RG: {f.rg}, CPF: {f.cpf}")