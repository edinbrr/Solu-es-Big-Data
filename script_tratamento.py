import pandas as pd
import numpy as np

# Passo 3 e 4: Leitura do arquivo fornecido com os parâmetros exigidos
# Considerando que o arquivo 'dados.csv' está salvo localmente
df_original = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

print("=== PASSO 5: VERIFICAÇÃO INICIAL ===")
# 5.a - Imprimir informações gerais
print("\nInformações gerais sobre o conjunto de dados:")
print(df_original.info())

# 5.b - Imprimir as primeiras e últimas N linhas (escolhi N=5)
print("\nPrimeiras 5 linhas:")
print(df_original.head(5))
print("\nÚltimas 5 linhas:")
print(df_original.tail(5))

# Passo 6: Criação de uma nova variável com a cópia dos dados
df_tratado = df_original.copy()

print("\n=== PASSO 7: TRATAMENTO DA COLUNA CALORIES ===")
# 7.a - Substituir nulos na coluna Calories por 0
df_tratado['Calories'] = df_tratado['Calories'].fillna(0)
# 7.b - Imprimir para verificar (focando nas linhas 18 e 28 que tinham nulos)
print("\nVerificando Calories (linhas 18 e 28 devem ser 0 agora):")
print(df_tratado.loc[[18, 28], ['ID', 'Calories']])

print("\n=== PASSO 8 e 9: TRATAMENTO DA COLUNA DATE (ERRO INTENCIONAL) ===")
# 8.a - Substituir nulos por '1900/01/01'
df_tratado['Date'] = df_tratado['Date'].fillna('1900/01/01')
print("\nVerificando a inserção de '1900/01/01' (linha 22):")
print(df_tratado.loc[[22], ['ID', 'Date']])

# 9.a - Corrigindo o erro (o formato não é aceito) substituindo por NaN
df_tratado['Date'] = df_tratado['Date'].replace('1900/01/01', np.nan)
print("\nApós substituir '1900/01/01' por NaN (linha 22):")
print(df_tratado.loc[[22], ['ID', 'Date']])

print("\n=== PASSO 10 e 11: TRATAMENTO DA STRING 20201226 E CONVERSÃO ===")
# Primeiro, removendo aspas simples de todas as strings para padronizar o dataframe
df_tratado['Date'] = df_tratado['Date'].str.replace("'", "")

# 10 - Substituindo a string mal formatada
df_tratado['Date'] = df_tratado['Date'].replace("20201226", "2020/12/26")

# 11 - Convertendo finalmente para datetime
df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], format='%Y/%m/%d')
print("\nVerificando as transformações de datetime:")
print(df_tratado.info())

print("\n=== PASSO 12 e 13: LIMPEZA FINAL ===")
# 12 - Remover registros contendo valores nulos (tendo como base a coluna Date, linha 22)
df_tratado = df_tratado.dropna(subset=['Date'])

# 13 - Imprimir o dataframe final
print("\nDataframe final limpo e pronto para análise:")
print(df_tratado)