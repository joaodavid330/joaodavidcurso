import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import random
from datetime import datetime, timedelta

def gera_dados_fictcios(num_registros = 600):
   """
   Gera um DataFrame do Pandas com dados de vendas fictícios.
   """
   print(f"\nIniciando geração de {num_registros} registros de vendas...")

   produtos = {
      'Celular': {'Categoria': 'Eletrônicos', 'Preço': 5500.00},
      'Notebook': {'Categoria': 'Eletrônicos', 'Preço': 3500.00},
      'Tablet': {'Categoria': 'Eletrônicos', 'Preço': 2500.00},
      'Camiseta': {'Categoria': 'Vestuário', 'Preço': 50.00},
      'Calça': {'Categoria': 'Vestuário', 'Preço': 120.00},
      'Tênis': {'Categoria': 'Vestuário', 'Preço': 300.00},
      'Livro': {'Categoria': 'Livros', 'Preço': 40.00},
      'Caderno': {'Categoria': 'Papelaria', 'Preço': 15.00},
      'Caneta': {'Categoria': 'Papelaria', 'Preço': 5.00},
   }

   lista_produtos = list(produtos.keys())

   cidades_estados = {
      'São Paulo': 'SP',
      'Rio de Janeiro': 'RJ',
      'Belo Horizonte': 'MG',
      'Brasília': 'DF',
      'Salvador': 'BA'
   }

   lista_cidades = list(cidades_estados.keys())

   dados_vendas = []

   data_inicial = datetime(2026, 5, 25)

   for i in range(num_registros):
        produto = random.choice(lista_produtos)
        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1, 10)
        data_pedido = data_inicial + timedelta( days= int(i/5), hours = random.randint(0, 23))

        if produto_nome in ['Celular', 'Notebook', 'Tablet']:
            preco_unitario = produtos[produto_nome]['Preço'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['Preço']

        dados_vendas.append({
            'Id_Pedido': 1000 + 1,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria_Produto': produtos[produto_nome]['Categoria'],
            'Preço_Unitário': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'Id_Cliente': np.random.randint(1000, 2000),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

        print("Geração de dados concluída com sucesso!\n")
        return pd.DataFrame(dados_vendas)

df_vendas = gera_dados_fictcios(500)
type(df_vendas)
df_vendas.shape
df_vendas.head()
df_vendas.tail()
df_vendas.info()
df_vendas.describe()
df_vendas.dtypes
