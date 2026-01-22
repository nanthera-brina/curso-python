#Criar uma classe, no exemplo: Pessoa

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura}.")

#Criar objetos

p1 = Pessoa("Bruno", 22, 1.75)
p2 = Pessoa("Tamiris", 21, 1.62)
p3 = Pessoa("Dulce", 53, 1.57)
p4 = Pessoa("Luana", 17, 1.70)
p5 = Pessoa("Mateus", 30, 1.82)

#Chamar os atributos dos objetos

print(vars(p1))