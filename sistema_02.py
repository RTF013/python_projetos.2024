import streamlit as st
import sqlite3

caminho_db = 'C:\\Users\\USER\\Documents\\banco-de-dados\\banco\\teste.db'

def criar_tabela():
    conexao = sqlite3.connect(caminho_db)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_container (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            container TEXT NOT NULL,
            tara INTEGER,
            lacre TEXT,
            maxgross TEXT,
            armador TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

def salvar_dados(container, tara, lacre, maxgross, armador):
    conexao = sqlite3.connect(caminho_db)
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO dados_container (container, tara, lacre, maxgross, armador) VALUES (?, ?, ?, ?, ?)",
                   (container, tara, lacre, maxgross, armador))

    conexao.commit()
    conexao.close()

def verificar_campos(container, tara, lacre, maxgross, armador):
    return all([container, tara, lacre, maxgross, armador])

marcas = ['Hambur-Sud', 'Maersk', 'One', 'Hapag', 'MSC']

container = st.text_input('Digite o Container')
tara = st.number_input('Digite a tara')
lacre = st.text_input('Digite o lacre')
maxgross = st.text_input('Digite Maxgross')
armador = st.selectbox('Digite o armador', marcas)

criar_tabela()

salvar = st.button('Salvar')

if salvar:
    if verificar_campos(container, tara, lacre, maxgross, armador):
        salvar_dados(container, tara, lacre, maxgross, armador)
        st.success('Dados salvos com sucesso!')
    else:
        st.warning('Digite todos os campos corretamente')
