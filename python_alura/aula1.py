# # # Importar uma biblioteca: pandas -> para fazer isso vá no terminal e digite > pip install pandas

# # import pandas as pd

# # # Agora trazer a base de dados:

# # df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
####### o comando indica que a base de dados vai ser lido usando o pandas; depois é preciso passar o link da base de dados.

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

pd.set_option('display.max_rows', 20)       #### Número máximo de linhas que o pandas mostra antes de resumir com ...
pd.set_option('display.min_rows', 20)       #### Quando a tabela é grande e ele resolve resumir, esse valor diz quantas linhas mínimas ainda devem aparecer
pd.set_option('display.max_columns', None)  #### Mostra todas as colunas, sem esconder nenhuma
pd.set_option('display.width', None)        #### Evita quebrar linhas ou esconder colunas porque “não couberam na tela”

# print(df.head(6)) # TRAZ UMA AMOSTRA DOS DADOS

# print(df.info()) # TRAZ INFORMAÇÕES SOBRE A TIPAGEM DOS DADOS # INFORMAÇÕES GERAIS DAS COLUNAS DA TABELA

# print(df.describe()) # TRAZ INFORMAÇÕES MAIS PROFUNDAS, ANÁLISE ESTATÍSTICA ## APENAS COM OS DADOS NUMÉRICOS 

# print(df.shape) # TRAZ A DIMENSÃO DA TABELA (NÃO USA PARÊNTESES), NÚMEROS DE LINHAS E DE COLUNAS

# linhas, colunas = df.shape[0], df.shape[1]
# print(f"Linhas: {linhas}")
# print(f"Colunas: {colunas}")

print(df.columns) #TRAZ OS NOMES DAS COLUNAS (TAMBÉM NÃO USA PARÊNTESES)

renomear_colunas = {
    'work_year' : 'ano',
    'experience_level' : 'senioridade',
    'employment_type' : 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=renomear_colunas, inplace=True) # Vai renomear as colunas
print(df.columns)

# print(df["senioridade"].value_counts())

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'    
}
df["senioridade"] = df["senioridade"].replace(senioridade)
print(df["senioridade"].value_counts())

# print(df["contrato"].value_counts())

contrato = {
    'FT': 'Tempo integral',
    'PT': 'Tempo parcial',
    'FL': 'Freelancer',
    'CT': 'Contrato'    
}
df["contrato"] = df["contrato"].replace(contrato)
print(df["contrato"].value_counts())

# print(df["remoto"].value_counts())

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
}
df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
print(df["tamanho_empresa"].value_counts())

# print(df["tamanho_empresa"].value_counts())

remoto = {
    0: 'Prensecial',
    50: 'Híbrido',
    100: 'Remoto'
}
df["remoto"] = df["remoto"].replace(remoto)
print(df["remoto"].value_counts())

print(df.head())

print(df.describe(include="object"))
