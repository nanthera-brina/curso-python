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

# # PROCURAR TEXTO

# t8 = input("Digite uma frase: ").find("eu") # indica a posição da palavra no texto (ou -1 se não achar)
# print(t8)

# t9 = "Eu estou aprendendo Python" # retorna true ou false
# print("Python" in t9)

# t10 = input("Digite uma frase: ") # exemplo com input
# if "python" in t10.lower():
#     print("Você mencionou Python!")
# else:
#     print("Não falou de Python ainda!")

# # SUBSTITUIR PARTES DO TEXTO

# t11 = input("Digite uma frase: ").replace("a", "@") #("qual a letra", "substitui por")
# print(t11)

# t12 = input("Digite uma frase: ").lower().replace("triste", "feliz") # verifique a ordem
# print(t12)

# # SEPARAR TEXTOS

# t13 = input("Digite uma frase: ").split()  # quebra texto em lista
# print(t13)

# # JUNTAR TEXTOS

# lista = ["Eu", "amo", "Python"]

# t14 = " ".join(lista)  # junta lista em texto
# print(t14)

# # TAMANHO DO TEXTO

# t15 = len(input("Digite uma frase: ")) # len é função, ela conta caracteres
# print(t15)

# ##### contar caracteres sem espaço #####
# frase = input("Digite uma frase: ")
# t16 = len(frase.replace(" ", ""))
# print(t16)

# VERIFICAÇÕES: LETRAS, NÚMEROS E ESPAÇOS

t17 = input("Digite senha: ").isalpha() # verifica só letras ## retorna True ou False
print(t17)

t18 = input("Digite senha: ").isdigit() # verifica só números ## retorna True ou False
print(t18)

t19 = input("Digite senha: ").isalnum() # verifica letras ou números ## retorna True ou False
print(t19)

t20 = input("Digite senha: ").isspace() # verifica espaços em branco ## retorna True ou False
print(t20)