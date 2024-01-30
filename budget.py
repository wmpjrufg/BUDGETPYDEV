import streamlit as st
import pandas as pd

@st.cache_data
def get_data():
    caminho = './Custo Referencial de Serviços - T156.xlsx'
    tabela_goinfra = pd.read_excel(caminho)
    tabela_goinfra.drop([0,1,2,3,4], axis = 0, inplace = True)

    tabela_goinfra.columns = list(tabela_goinfra.iloc[0])
    tabela_goinfra = tabela_goinfra.reset_index()
    tabela_goinfra.drop([0], axis = 0, inplace = True)

    tabela_goinfra = tabela_goinfra[['Código auxiliar', 'Serviço', 'Unidade', 'Material', 'Mão-de-obra', 'Total']].copy()
    tabela_goinfra = tabela_goinfra.iloc[:-2]
    tabela_goinfra = tabela_goinfra.dropna()

    tabela_goinfra['Código auxiliar'] = tabela_goinfra['Código auxiliar'].astype(int)
    tabela_goinfra['Serviço'] = tabela_goinfra['Serviço'].astype(str)
    tabela_goinfra['Unidade'] = tabela_goinfra['Unidade'].astype(str)
    tabela_goinfra['Unidade'] = tabela_goinfra['Unidade'].astype(str)
    tabela_goinfra['Material'] = tabela_goinfra['Material'].astype(float)
    tabela_goinfra['Mão-de-obra'] = tabela_goinfra['Mão-de-obra'].astype(float)
    tabela_goinfra['Total'] = tabela_goinfra['Total'].astype(float)

    return tabela_goinfra

def revestimento(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    area = dados['Área']
    area = dados['Área'].str.replace(',', '.').astype(float)

    for i in range(len(area)):
        preco_total.append(area[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo
             
def calha(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    comprimento = dados['Comprimento'].str.replace(',', '.').astype(float)

    for i in range(len(comprimento)):
        preco_total.append(comprimento[i] * p_mo[0])
    arquivo['Preço total'] = preco_total
    
    return arquivo

def forro(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    area = dados['Área'].str.replace(',', '.').astype(float)

    for i in range(len(area)):
        preco_total.append(area[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo


def esquadria(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    QTD = dados['QTD']

    for i in range(len(QTD)):
        preco_total.append(QTD[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo

def porta(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    QTD = dados['QTD']

    for i in range(len(QTD)):
        preco_total.append(QTD[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo

def piso(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    area = dados['Área'].str.replace(',', '.').astype(float)

    for i in range(len(area)):
        preco_total.append(area[i] * p_mo[i-1])
    arquivo['Preço total'] = preco_total
    
    return arquivo

def telha(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    area = dados['Área'].str.replace(',', '.').astype(float)

    for i in range(len(area)):
        preco_total.append(area[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo

def alvenaria(dados, p_mo):
    preco_total = []
    arquivo = dados
    arquivo['Preço unitário'] = p_mo
    area = dados['Área'].str.replace(',', '.').astype(float)

    for i in range(len(area)):
        preco_total.append(area[i] * p_mo[i])
    arquivo['Preço total'] = preco_total
    
    return arquivo
