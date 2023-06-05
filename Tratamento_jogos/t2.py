import sqlite3
import tkinter as tk

conexao = sqlite3.connect('Alunos')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (ID INTEGER,  Nome TEXT, idade INTEGER, DTnascimento STR, Telefone STR, Endereco STR, notas STR )")
conexao.close()



def inserir_aluno():
    ID = entry_ID.get()
    Idade = entry_Idade.get()
    Nome = entry_Nome.get()
    DTnascimento = entry_DTnascimento.get()
    Telefone = entry_Telefone.get()
    Endereco = entry_Endereco.get()
    nota_01 = entry_Nota01.get()
    nota_02 = entry_Nota02.get()
    nota_03 = entry_Nota03.get()
    conexao = sqlite3.connect("Alunos")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Alunos (ID, Idade, Nome, DTnascimento, Telefone, Endereco, nota_01, nota_02, nota_03) VALUES (?,?,?,?,?,?,?)",
        (ID, Idade, Nome, DTnascimento, Telefone, Endereco, nota_01, nota_02, nota_03))
    # Confirmar a transação
    conexao.commit()
    conexao.close()
    # Limpar os campos de entrada
    entry_ID.delete(0, tk.END)
    entry_Idade.delete(0, tk.END)
    entry_Nome.delete(0, tk.END)
    entry_DTnascimento.delete(0, tk.END)
    entry_Telefone.delete(0, tk.END)
    entry_Endereco.delete(0, tk.END)

def mostrar_aluno():
    conn = sqlite3.connect('Alunos')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alunos")
    registros = cursor.fetchall()
    conn.close()
    for registro in registros:
        print(registro)

janela = tk.Tk()
janela.title('Inserir aluno')
janela.geometry("330x500")

# label ---> exibir informações estáticas  não permite a edição direta
label_ID = tk.Label(janela, text='id')
label_ID.grid(row=0, column=0, padx=10, pady=10)

label_Nome = tk.Label(janela, text='Idade')
label_Nome.grid(row=1, column=0, padx=10, pady=10)

label_Idade = tk.Label(janela, text='Nome')
label_Idade.grid(row=2, column=0, padx=10, pady=10)

label_DTnascimento = tk.Label(janela, text='DTnascimento')
label_DTnascimento.grid(row=3, column=0, padx=10, pady=10)

label_Telefone = tk.Label(janela, text='Telefone')
label_Telefone.grid(row=4, column=0, padx=10, pady=10)

label_Endereco = tk.Label(janela, text='Endereço')
label_Endereco.grid(row=5, column=0, padx=10, pady=10)

label_Nota01 = tk.Label(janela, text='nota_01')
label_Nota01.grid(row=6, column=0, padx=10, pady=10)

label_Nota02 = tk.Label(janela, text='nota_02')
label_Nota02.grid(row=7, column=0, padx=10, pady=10)

label_Nota03 = tk.Label(janela, text='nota_03')
label_Nota03.grid(row=8, column=0, padx=10, pady=10)

# entry ---> widget interativo inserir dados diretamente

entry_ID = tk.Entry(janela, width=35)
entry_ID.grid(row=0, column=1, padx=10, pady=10)

entry_Nome = tk.Entry(janela, width=35)
entry_Nome.grid(row=1, column=1, padx=10, pady=10)

entry_Idade = tk.Entry(janela, width=35)
entry_Idade.grid(row=2, column=1, padx=10, pady=10)

entry_DTnascimento = tk.Entry(janela, width=35)
entry_DTnascimento.grid(row=3, column=1, padx=10, pady=10)

entry_Telefone = tk.Entry(janela, width=35)
entry_Telefone.grid(row=4, column=1, padx=10, pady=10)

entry_Endereco = tk.Entry(janela, width=35)
entry_Endereco.grid(row=5, column=1, padx=10, pady=10)

entry_Nota01 = tk.Entry(janela, width=35)
entry_Nota01.grid(row=6, column=1, padx=10, pady=10)

entry_Nota02 = tk.Entry(janela, width=35)
entry_Nota02.grid(row=7, column=1, padx=10, pady=10)

entry_Nota03 = tk.Entry(janela, width=35)
entry_Nota03.grid(row=8, column=1, padx=10, pady=10)

# Botão de inserir
botao_inserir = tk.Button(text='Inserir Aluno', command=inserir_aluno)
botao_inserir.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

# Botão de selecionar
botao_mostrar = tk.Button(text='mostrar_aluno', command=mostrar_aluno)
botao_mostrar.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

janela.mainloop()