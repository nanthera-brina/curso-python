# # TESTANDO VARIÁVEL E PRINT

# nome = "Sabrina"

# #Usando vírgula
# print("Meu nome é:", nome)

# #Usando sinal de mais
# print("Meu nome é: " + nome)

# #Usando f-string
# print(f"Meu nome é: {nome}")

# # TESTANDO INPUT

# nome = input(f"Qual é seu nome: ")

# print("Bem-vindo(a), " + nome)

# # TESTANDO SOMA SIMPLES

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))

# print("Primeiro exemplo:", num1+num2+num3)

# soma = num1 + num2 + num3
# print("Segundo exemplo:", soma)

# # TESTANDO MAIOR OU MENOR

# a = float(input("Coloque o primeiro número: "))
# b = float(input("Coloque o segundo número: "))

# if a > b:
#     print("O primeiro é maior que o segundo.")
# elif a < b:
#     print("O segundo é maior que o primeiro.")
# else:
#     print("Mesmo valor.")

# # TESTANDO NÚMERO POSITIVO E NEGATIVO

# c = int(input("Digite um número: "))

# if c > 0:
#     print(f"O número {c} é positivo.")
# elif c < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")

#TESTANDO PAR OU ÍMPAR

d = int(input("Digite um número: "))

if d%2 == 0:
    print("O número é par.")
else: 
    print("O número é ímpar.")