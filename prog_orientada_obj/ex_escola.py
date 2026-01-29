# Mini mundo: Escola
# Objetos: aluno, professor, direção...

#########################################

# A ESCOLA

## os professores

class Professor:
    def __init__(self, nome, idade, materia):
        self.nome = nome
        self.idade = idade
        self.materia = materia

    def apresentar(self):
        print(f"Olá, sou professor/a, meu nome é {self.nome}, tenho {self.idade} anos e dou aula de {self.materia}.")

### objetos: professores

P1 = Professor("Maria", 45, "história")
P2 = Professor("Juliana", 26, "matemática")
P3 = Professor("Mateus", 50, "português")

## os alunos

class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou na {self.serie} série.")

### objetos: alunos

A1 = Aluno("Enzo", 13, "oitava")
A2 = Aluno("Valentina", 14, "nona")

## a direção

class Direção:
    def __init__(self, nome, idade, funcao):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.funcao}.")

### objetos: direção

D1 = Direção("Creuza", 49, "Diretora")
D2 = Direção("Felipe", 30, "Secretário")

###### Criar objeto com base nas classes

tipo = input("Você quer criar qual pessoa? ").title() #primeiro tem que pedir para o usuário ##TITLE deixa a primeira letra maiúscula

match tipo: 
    case "Professor":
        nome = input("Digite o nome do seu objeto: ")
        idade = int(input("Digite a idade do seu objeto: "))
        materia = input("Digite a matéria que seu objeto lenciona: ")
        P4 = Professor(nome, idade, materia)
        P4.apresentar()

    case "Aluno":
        nome = input("Digite o nome do seu objeto: ")
        idade = int(input("Digite a idade do seu objeto: "))
        serie = input("Digite a série que seu objeto está: ")
        A3 = Aluno(nome, idade, serie)
        A3.apresentar()

    case "Direção" | "Direcao":
        nome = input("Digite o nome do seu objeto: ")
        idade = int(input("Digite a idade do seu objeto: "))
        funcao = input("Digite a função que seu objeto exerce: ")
        D3 = Direção(nome, idade, funcao)
        D3.apresentar()

    case _:  #caso não tenha correspondência
        print("Não tem essa função.")
