### Limpar e Preparar os Dados

from aula1 import df

# print(df.isnull()) # INFORMA SE TEM VALOR NULO COM TRUE OU FALSE

# print(df.isnull().sum()) #SOMA QUANTAS LINHAS TEM VALOR NULO DE TAL COLUNA

# print(df["ano"].unique()) # INFORMA OS VALORES QUE TEM EM UM CAMPO ESPECÍFICO ## "NAN" É A FORMA DO PYTHON DE INFORMAR OS NULOS

# print(df[df.isnull().any(axis=1)]) # MOSTRA QUAIS SÃO AS LINHAS QUE TEM OS NULOS

'''EXEMPLO DE CRIAR DATAFRAME (df)'''

##### PRIMEIRO: MÉDIA E MEDIANA

import pandas as pd
import numpy as np

# df_salarios = pd.DataFrame({
#     'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
#     'salario': [4000, np.nan, 5000, np.nan, 1000000]          # np.nan → cria valores faltantes
# })

# df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))    # .mean() → calcula a média ignorando os NaN 
#                                                                                                         #.round(2) → arredonda para 2 casas
#                                                                                                         #.fillna() → substitui os NaN pela média
# print(df_salarios)

# df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())         # .median() → calcula a mediana ignorando os NaN 

# print(df_salarios)

##### SEGUNDO: PREENCHER COM DADO ANTERIOR OU POSTERIOR

# df_temperaturas = pd.DataFrame({
#     'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
#     'Temperatura': [30, np.nan, np.nan, 28, 27]
# })

# df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()  # ffill significa forward fill, preenche valores vazios usando o valor válido anterior na coluna
# print(df_temperaturas)

# df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()  # ffill significa backward fill, preenche valores vazios usando o próximo valor válido abaixo na coluna
# print(df_temperaturas)

##### TERCEIRO: EM STRING, PREENCHER COM TEXTO PRONTO

# df_cidades = pd.DataFrame({
#     'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
#     'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
# })

# df_cidades['cidade_preenchida'] = df_cidades["cidade"].fillna("Não informado")
# print(df_cidades)

'''VOLTAR PARA O EXERCÍCIO'''

## LIMPAR OS DADOS NULO DO DF ORIGINAL

df_limpo = df.dropna() # dropna() serve para remover valores ausentes
# print(df_limpo.isnull().sum())

## TIRAR DECIMAL DO ANO DO DF ORIGINAL 

# print(df_limpo.info())

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.head())
