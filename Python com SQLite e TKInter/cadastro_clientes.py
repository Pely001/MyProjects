from tkinter import *
import sqlite3
import pandas as pd
from tkinter import messagebox


##CRIANDO BANCO DE DADOS

conexao = sqlite3.connect("Meu_Banco.db")

##CRIANDO CURSOR

cursor = conexao.cursor()

##CRIANDO A TABELA
try:
    cursor.execute('''CREATE TABLE pessoas
    (nome text NOT NULL,
    sobrenome text NOT NULL,
    telefone text NOT NULL PRIMARY KEY,
    email text
    )''')
except sqlite3.Error as erro:
    print('ERRO: ', erro)



##CONFIRMAR MUDANÇAS E FECHAR BANCO
conexao.commit()
conexao.close()

janela = Tk()
janela.title("Sistema de Cadastro")
janela.geometry("400x400")
janela.resizable(0,0)

try:
    def cadastrar_pessoa():
        conexao = sqlite3.connect("Meu_Banco.db")
        cursor = conexao.cursor()

#INSERINDO DADOS NA TABELA
        cursor.execute("INSERT INTO pessoas VALUES (:nome,:sobrenome,:telefone,:email)",
                   {'nome': entry_nome.get(),
                    'sobrenome': entry_sobrenome.get(),
                    'telefone': entry_telefone.get(),
                    'email': entry_email.get()
                   })
        conexao.commit()
        conexao.close()


        messagebox.showinfo('','Linha Incluida')

#LIMPANDO A TELA
        entry_nome.delete(0,"end")
        entry_sobrenome.delete(0,"end")
        entry_telefone.delete(0,"end")
        entry_email.delete(0,"end")
except:
    messagebox.showerror("ERRO")

#EXPORTANDO DADOS PARA PLANILHA EXCEL
try:
    def exportar_pessoa():
        conexao = sqlite3.connect("Meu_Banco.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT *, oid FROM pessoas")
        pessoas_cadastradas = cursor.fetchall()
        pessoas_cadastradas=pd.DataFrame(pessoas_cadastradas, columns=['nome','sobrenome','telefone','email','Id_banco'])
        pessoas_cadastradas.to_excel('cadastro_pessoas.xlsx')

        conexao.commit()
        conexao.close()
        messagebox.showinfo('','Exportado com sucesso')
except:
    messagebox.showerror("ERRO")    

#DESCRIÇÃO DOS DADOS DE ENTRADA

label_nome = Label(janela, text="Nome")
label_nome.grid(row=2, column=0, padx=10, pady=10)
label_sobrenome = Label(janela, text="Sobrenome")
label_sobrenome.grid(row=3, column=0, padx=10, pady=10)
label_email = Label(janela, text="Email")
label_email.grid(row=4, column=0, padx=10, pady=10)
label_telefone = Label(janela, text="Telefone")
label_telefone.grid(row=5, column=0, padx=10, pady=10)
label_descricao = Label(janela, text="SISTEMA DE CADASTRO")
label_descricao.grid(row=0, column=1, padx=4, pady=4)
label_espaco = Label(janela, text="")
label_espaco.grid(row=1, column=1, padx=4, pady=4)


#CAIXA DE ENTRADA DOS DADOS

entry_nome = Entry(janela, text="Nome")
entry_nome.grid(row=2, column=1, padx=10, pady=10)
entry_sobrenome = Entry(janela, text="Sobrenome")
entry_sobrenome.grid(row=3, column=1, padx=10, pady=10)
entry_email = Entry(janela, text="Email")
entry_email.grid(row=4, column=1, padx=10, pady=10)
entry_telefone = Entry(janela, text="telefone")
entry_telefone.grid(row=5, column=1, padx=10, pady=10)

#BOTÕES

botao_cadastro = Button(janela, text="Cadastrar", command=cadastrar_pessoa)
botao_cadastro.grid(row=6, column=1, padx=10, pady=10)
botao_exportar = Button(janela, text="Exportar Arquivo Excel", command=exportar_pessoa)
botao_exportar.grid(row=7, column=1, padx=10, pady=10)


janela.mainloop()