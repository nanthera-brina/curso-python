#Usuário precisa colocar número 1 e número 2:

num1 = int(input(f"Coloque o primeiro número: "))
num2 = int(input(f"Coloque o segundo número: "))

if num1 > num2:
    print(f"O primeiro número é maior que o segundo.")
else:
    print(f"O segundo número é maior que o primeiro.")

#Saudação

nome = input("Digite seu nome: ")
print(f"Olá, {nome}")

#Soma

num1 = float(input("Digite número 1: "))
num2 = float(input("Digite número 2: "))

print (num1+num2)

#Ímpar e par

num = int(input("Digite o número: "))

if num %2 == 0:
    print("é par")
else:
    print("é impar")
