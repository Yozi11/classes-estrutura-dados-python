import os
os.system("cls")


from dataclasses import dataclass

@dataclass

class Autor:
    # Atributo nome: nome do autor (string)
    nome: str
    # Atributo biografia: breve biografia do autor (string)
    biografia:str


@dataclass

class Livro:
    # Atributo titulo: título do livro (string)
    titulo:str
        # Atributo ano: ano de publicação do livro (inteiro)

    ano:int
    # Atributo autor: referência a uma instância da classe Autor
    autor:Autor



    def exibir_detalhes(self):
        # Método para exibir os detalhes do livro e o nome do autor
        print(f"Titulo:{self.titulo}")
        print(f"Ano de publicação:{self.ano}")
        print(f"Autor: {self.autor.nome}")

# Cria uma instância de Autor
autor1 =Autor(nome ="Machado de Assis",biografia="Foi um grande escritor brasileiro.")
# Cria uma instância de Livro associando o autor criado

livro1 =Livro(titulo="Dom casmurro",ano =1899,autor=autor1)

livro1.exibir_detalhes()
