# Trabalho Prático - DGT2823 Tecnologias para Soluções de Big Data

**Autor:** Edson Victor Miranda de Oliveira

Este repositório contém a resolução do Trabalho Prático da disciplina **DGT2823 - Tecnologias para desenv. de soluções de big data**[cite: 1]. O projeto consiste na leitura, tratamento e limpeza de um conjunto de dados brutos utilizando Python e a biblioteca Pandas, deixando-o apto para mineração e análise de dados[cite: 8].

## 📁 Estrutura do Repositório

- `dados.csv`: Arquivo de dados bruto fornecido para o projeto, contendo propositalmente valores nulos e dados formatados incorretamente[cite: 4].
- `script_tratamento.py`: Script principal contendo toda a lógica de higienização exigida no roteiro da prática[cite: 8].

## 🚀 Tecnologias Utilizadas

- **Python**[cite: 1]
- **Pandas** (para manipulação e limpeza dos DataFrames)[cite: 1, 8]
- **NumPy**

## ⚙️ Processo de Tratamento de Dados

O script executa o seguinte fluxo de trabalho rigorosamente conforme o roteiro da disciplina[cite: 9, 10]:

1. **Importação:** Leitura do arquivo CSV passando os parâmetros corretos de separador (`;`) e engine (`python`)[cite: 9].
2. **Análise Exploratória:** Exibição das informações gerais (linhas, colunas, tipos) e leitura das primeiras e últimas linhas do dataset[cite: 7, 9].
3. **Tratamento de Nulos (Calories):** Substituição de valores `NaN` na coluna `Calories` por `0`[cite: 9].
4. **Tratamento de Nulos (Date):** Preenchimento inicial dos vazios na data com `1900/01/01`, forçando e em seguida corrigindo o erro de conversão ao substituir por `NaN`[cite: 9].
5. **Correção de Tipagem e Strings:** Tratamento da anomalia da string `20201226` para o formato padrão com barras através do método `replace`[cite: 9, 10].
6. **Conversão Datetime:** Transformação de toda a coluna `Date` para o tipo numérico `datetime` (utilizando `to_datetime`)[cite: 9].
7. **Limpeza Final:** Exclusão definitiva de registros residuais que permaneceram com valores nulos utilizando o método `dropna`[cite: 10].

## 🔧 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/edinbrr/Solu-es-Big-Data.git](https://github.com/edinbrr/Solu-es-Big-Data.git)
