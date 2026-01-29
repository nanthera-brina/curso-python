# # MUDAR MAIÚSULAS E MINÚSCULAS

# t1 = input("Digite seu nome completo: ").title() # Primeira Letra Maiúscula De Cada Palavra
# print(f"Olá, {t1}.")

# t2 = input("Digite uma frase: ").lower() # tudo fica minúsculo
# print(t2)

# t3 = input("Digite uma frase: ").upper() # TUDO MAIÚSCULO
# print(t3)

# t4 = input("Digite uma frase: ").capitalize() # Só a primeira letra da frase maiúscula
# print(t4)

# # REMOVER ESPAÇOS

# t5 = input("Digite uma frase: ").lstrip() # remove espaços em branco da esquerda
# print(t5)

# t6 = input("Digite uma frase: ").rstrip() # remove espaços em branco da direita
# print(t6)

# t7 = input("Digite seu email: ").strip() # remove espaços em branco do começo e fim
# print(t7)

# PROCURAR TEXTO

t8 = input("Digite uma frase: ").find("eu") # indica a posição da palavra no texto (ou -1 se não achar)
print(t8)

t9 = "Eu estou aprendendo Python" # retorna true ou false
print("Python" in t9)

t10 = input("Digite uma frase: ") # exemplo com input
if "python" in t10.lower():
    print("Você mencionou Python!")
else:
    print("Não falou de Python ainda!")


