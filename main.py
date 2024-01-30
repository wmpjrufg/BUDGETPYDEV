import pandas as pd
import streamlit as st
import openpyxl

st.set_page_config(page_title='Custo Referencial de Serviços',
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='auto', )



@st.cache_data
def get_data():
    caminho = 'Custo Referencial de Serviços - T156.xlsx'
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




with st.container():
    st.title('Custo Referencial de Serviços')
    st.write('Calcule o custo referencial de cada item')

    arquivo = st.file_uploader('Selecione o arquivo com os dados', type='csv', accept_multiple_files=False, key='file_uploader')
    temService = False

    if arquivo is not None:
        dados = pd.read_csv(arquivo, sep=';')
        dados = dados.drop(index=0)
        # Check and handle non-numeric values in 'ID GOINFRA' column
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
        
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo
                area = dados['Área']
                #st.write(area)
                #area = dados['Área'].str.replace(',', '.').astype(float)


                for i in range(len(area)):
                    preco_total.append(area[i+1] * p_mo[i])
                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)


            
            elif "CALHA" in service:
                
                preco_total = []
                arquivo_cvs = dados.copy()
                arquivo_cvs['Preço unitário'] = p_mo
            
                comprimento = dados['Comprimento'].str.replace(',', '.').astype(float)
            
                for i in range(len(comprimento)):
                    preco_total.append(float(comprimento[i+1]) * p_mo[0])
            
                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(f'novo_arquivo.csv', sep = ';', index = False)


            elif "FORRO" in servico:
        
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                area = dados['Área'].str.replace(',', '.').astype(float)

                for i in range(len(area)):
                    preco_total.append(float(area[i+1]) * p_mo[i])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)

            elif "ESQUADRIA" in servico:
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                QTD = dados['QTD']

                for i in range(len(QTD)):
                    preco_total.append(float(QTD[i+1]) * p_mo[i])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)

            elif "PORTA" in servico:
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                QTD = dados['QTD']

                for i in range(len(QTD)):
                    preco_total.append(float(QTD[i+1]) * p_mo[i])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)

            elif "PISO" in servico:
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                area = dados['Área'].str.replace(',', '.').astype(float)
                #area = dados['Área']

                for i in range(len(area)):
                    preco_total.append(float(area[i+1]) * p_mo[i-1])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)
        
            elif "TELHA" in servico:
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                area = dados['Área'].str.replace(',', '.').astype(float)
                #area = dados['Área']

                for i in range(len(area)):
                    preco_total.append(float(area[i+1]) * p_mo[i])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)

            elif "ALVENARIAS" in servico:
                preco_total = []
                arquivo_cvs = dados
                arquivo_cvs['Preço unitário'] = p_mo

                area = dados['Área'].str.replace(',', '.').astype(float)
                #area = dados['Área']

                for i in range(len(area)):
                    preco_total.append(float(area[i+1]) * p_mo[i])

                arquivo_cvs['Preço total'] = preco_total
                arquivo_cvs.to_csv(arquivo, sep = ';', index = False)

        st.download_button(label='Baixar arquivo', data=arquivo_cvs.to_csv().encode('utf-8'), file_name='novo_arquivo.csv', mime='text/csv')