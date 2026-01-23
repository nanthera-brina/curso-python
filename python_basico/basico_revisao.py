# TESTANDO VARIÁVEL E PRINT

nome = "Sabrina"

#Usando vírgula
print("Meu nome é:", nome)

#Usando sinal de mais
print("Meu nome é: " + nome)

#Usando f-string
print(f"Meu nome é: {nome}")

# TESTANDO INPUT

nome = input(f"Qual é seu nome: ")

print("Bem-vindo(a), " + nome)

# TESTANDO SOMA SIMPLES

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print("Primeiro exemplo:", num1+num2+num3)

soma = num1 + num2 + num3
print("Segundo exemplo:", soma)

# TESTANDO MAIOR OU MENOR

a = float(input("Coloque o primeiro número: "))
b = float(input("Coloque o segundo número: "))

if a > b:
    print("O primeiro é maior que o segundo.")
elif a < b:
    print("O segundo é maior que o primeiro.")
else:
    print("Mesmo valor.")

# TESTANDO NÚMERO POSITIVO E NEGATIVO

c = int(input("Digite um número: "))

if c > 0:
    print(f"O número {c} é positivo.")
elif c < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#TESTANDO PAR OU ÍMPAR

d = int(input("Digite um número: "))

if d%2 == 0:
    print("O número é par.")
else: 
    print("O número é ímpar.")

# TESTANDO + - * /

e = float(input("Digite o primeiro número: "))
f = float(input("Digite o segundo número: "))

soma = e+f
menos = e-f
vezes = e*f
divisao = e/f

print(f"A soma dos números é {soma:.0f}, a subtração é {menos:.0f}, a multiplicação é {vezes:.2f} e a divisão é {divisao:.2f}.")

# TESTANDO MÉDIA

nota1 = int(input("Digite nota da atividade 1: "))
nota2 = int(input("Digite nota da atividade 2: "))
nota3 = int(input("Digite nota da atividade 3: "))

nota_final = (nota1 + nota2 + nota3) / 3

if nota_final >= 6:
   print(f"Aluno/a aprovado/a com a média de {nota_final}.")
else:
   print(f"Aluno/a reprovado/a com a média de {nota_final}.")

# TESTANDO WHILE PARA CONTAGEM

contador = 1

while contador <= 10:
    print(contador)
    contador += 1 # soma 1 a cada repetição. sem isso, ficaria para sempre
