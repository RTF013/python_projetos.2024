import tkinter as tk
from tkinter import ttk

class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

def cadastrar_usuario():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    sobrenome = sobrenome_entry.get()
    usuario = Usuario(nome, idade, sobrenome)

    lista_usuario.append(usuario)

    resultado_label.config(text=f'Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}')

    if usuario.idade <= 17:
        resultado_label.config(text=f'{usuario.nome} é adolescente')
    elif usuario.idade >= 18 and usuario.idade <= 50:
        resultado_label.config(text=f'{usuario.nome} é adulto')
    else:
        resultado_label.config(text=f'{usuario.nome} é idoso')

    continuar_var.set(1)

def mostrar_lista_usuarios():
    resultado_label.config(text='Lista de usuários cadastrados:')
    for x in lista_usuario:
        resultado_label.config(text=resultado_label.cget("text") + f'\nNome completo: {x.nome} {x.sobrenome} - idade {x.idade}')

# Criar a janela principal
root = tk.Tk()
