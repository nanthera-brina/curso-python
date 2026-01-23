# # TESTANDO SENHA BÁSICA

# senha = "1452"
# senha_digitada = input("Digite a senha: ")

# if senha_digitada == senha:
#     print("Acesso liberado!")
# else:
#     print("Senha incorreta")

# # TESTANDO SENHA AVANÇADA

# senha = "1452"
# senha_digitada = ""

# while senha_digitada != senha:   #ENQUANTO a senha digitada for DIFERENTE da senha correta, continue repetindo   ##!= é "diferente de"
#     senha_digitada = input("Digite a senha: ")

#     if senha_digitada != senha:
#         print("Senha incorreta, tente novamente.")

# print("Acesso liberado!")

# # TESTANDO SOMA ATÉ PARAR

# soma = 0  # onde guarda o total

# n = float(input("Digite um número (se 0, interrompe o programa): "))

# while n > 0:
#     soma += n
#     n = float(input("Digite um número (se 0, interrompe o programa): "))

# print(f"A soma total é {soma}.")

# # TESTANDO FOR (1)

# for n1 in range (21):  #usa FOR, IN e RANGE
#     print(n1)

# # TESTANDO FOR (2)

# for n2 in range (0, 21, 2):
#     print(n2)

# # TESTANDO FOR (3)

# for n3 in range (21, 0, -2):
#     print(n3)

# # TESTANDO TABUADA

# n_tab = int(input("Digite um número para sua tabuada: "))

# for nx in range (1,101):
#     resultado = n_tab * nx
#     print(f"{n_tab} X {nx} = {resultado}")

# # TESTANDO SOMA DE APENAS NÚMEROS PARES

# soma = 0

# for numero in range (11):
#     if numero%2 == 0:
#         soma += numero

# print(f"A soma dos números pares é {soma}.")

## TESTE FINAL

num_f = "50"
num_digitado = ""

while num_digitado != num_f:
   num_digitado = input("Digite o número: ")

   if num_digitado != num_f:
      print("Número errado, tente novamente.")

print("Parabéns, você acertou!")
