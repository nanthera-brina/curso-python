# ##### FUNÇÕES PARA NÚMEROS

# # VALOR ABSOLUTO

# n1 = abs(int(input("Digite números, positivos ou negativos: "))) # remove o sinal negativo
# print(n1)

# # ARREDONDAR 

# n2 = round(float(input("Digite números decimais: ")))
# print(n2)

# # POTÊNCIA

# n3 = float(input("Digite um número: "))
# n4 = float(input("Digite um número: "))

# n5 = pow(n3, n4)

# print(f"{n5:.0f}")

# #DIVISÃO + RESTO
# #### forma usada: desempacotando

# quociente, resto = divmod(10, 3)  ## divmod(dividendo, divisor)

# print("Quociente:", quociente)
# print("Resto:", resto)

# #### outro exemplo: converter minutos em horas

# minutos = int(input("Digite os minutos: "))

# horas, resto_min = divmod(minutos, 60)

# print(f"{horas} hora(s) e {resto_min} minuto (s).")

# # SOMA

# n6 = float(input("Digite um número: "))
# n7 = float(input("Digite um número: "))
# n8 = float(input("Digite um número: "))

# n9 = sum([n6, n7, n8])

# print(n9)

# # MÍNIMO E MÁXIMO

# n10 = float(input("Digite um número: "))
# n11 = float(input("Digite um número: "))
# n12 = float(input("Digite um número: "))

# minimo = min(n10, n11, n12)

# maximo = max(n10, n11, n12)

# print(f"O número mínimo é {minimo}, o número máximo é {maximo}.")

# ##### BIBLIOTECA MATH

import math

# RAIZ QUADRADA

numero = float(input("Digite um número: "))

n13 = math.sqrt(numero) # raiz quadrada
n14 = math.ceil(numero) # arredonda para cima
n15 = math.floor(numero) # arredonda para baixo
n16 = math.pow(numero, 2) # potência

print(f"A raiz quadrada do número é {n13}, arredondando para cima é {n14}, arredondando para baixo é {n15} e ao quadrado é {n16}.")