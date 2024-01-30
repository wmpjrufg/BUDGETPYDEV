import pandas as pd
import streamlit as st
#import openpyxl
from budget import get_data, revestimento, calha, forro, esquadria, porta, piso, telha, alvenaria

st.set_page_config(page_title='Custo Referencial de Serviços',
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='auto', )

with st.container():
    st.title('Custo Referencial de Serviços')
    st.write('Calcule o custo referencial de cada item')

    arquivo = st.file_uploader('Selecione o arquivo com os dados', type='csv', accept_multiple_files=False, key='file_uploader')
    temService = False

    if arquivo is not None:
        dados = pd.read_csv(arquivo, sep=';')
        #dados = dados.drop(index=0)
        codigos = pd.to_numeric(dados['ID GOINFRA'], errors='coerce')

        services = []
        p_mat = []
        p_mo = []
        p_tot = []

        tabela_goinfra = get_data()
        for codigo in codigos:
            df = tabela_goinfra[tabela_goinfra['Código auxiliar'] == codigo]
         
            for I, LINHA in df.iterrows():
                services.append(LINHA['Serviço'])
                p_mat.append(LINHA['Material'])
                p_mo.append(LINHA['Mão-de-obra'])
                p_tot.append(LINHA['Total'])

        temService = True
    
    st.write('---')
         
    if temService:    
        
        for service in services:
            
            if ("REVESTIMENTO" in service) or ("PINTURA" in service):
                arquivo_cvs = revestimento(dados=dados, p_mo=p_mo)
            
            elif "CALHA" in service:
                arquivo_cvs = calha(dados=dados, p_mo=p_mo)

            elif "FORRO" in service:                
                arquivo_cvs = forro(dados=dados, p_mo=p_mo)

            elif "ESQUADRIA" in service:
                arquivo_cvs = esquadria(dados=dados, p_mo=p_mo)

            elif "PORTA" in service:
                arquivo_cvs = porta(dados=dados, p_mo=p_mo)

            elif "PISO" in service:
                arquivo_cvs = piso(dados=dados, p_mo=p_mo)
                
            elif "TELHA" in service:
                arquivo_cvs = telha(dados=dados, p_mo=p_mo)

            elif "ALVENARIAS" in service:
                arquivo_cvs = alvenaria(dados=dados, p_mo=p_mo)
                
        st.download_button(label='Baixar arquivo', data=arquivo_cvs.to_csv(sep=';', index=False).encode('utf-8'), file_name='novo_arquivo.csv', mime='text/csv')