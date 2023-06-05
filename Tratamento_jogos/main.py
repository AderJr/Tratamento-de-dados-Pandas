import pandas as pd
from tabulate import tabulate

# lembrando que aqui onde você irá colocar o caminho da Base de Dados
caminhoDataBase = 'DataBase jogos final.csv'
df = pd.read_csv(caminhoDataBase)
# comando para reposicionar o index do código para iniciar com 1
# 'df.index.size' representa o total de registros
df.index = [int(x) for x in range(1, df.index.size + 1)]


def tela_inicial():
    print("============================================================\n")
    print("Bem vindo ao menu de manipulação de dados!")
    print("\n============================================================\n")
    print("1- Mostrar DataBase")
    print("2- Adicionar registro")
    print("3- Deletar registro")
    print("4- Alterar registro")
    print("5- Sair")
    print("\n============================================================\n")
    menu_resp = input("Favor escolher opção: ")
    print("\n============================================================\n")
    return menu_resp


while True:
    resp = tela_inicial()
    match resp:
        case "1":
            while True:
                print("============================================================\n")
                print("Tela de vizualização de DataBase")
                print("\n============================================================\n")
                print("1- Mostrar DataBase completo")
                print("2- Mostrar tamanho do DataBase")
                print("3- Mostrar conjunto de linhas")
                print("4- Transpor colunas para linhas no DataBase")
                print("5- Mostrar duas colunas específicas")
                print("6- Mostrar coluna específica")
                print("7- Mostrar registro específico")
                print("8- Voltar para menu")
                print("\n============================================================\n")
                viz_resp = input("Favor escolher opção: ")
                print("\n============================================================\n")
                match viz_resp:
                    case "1":
                        print("============================================================\n")
                        print("DataBase completo\n", tabulate(df, headers=df.columns, tablefmt="grid", stralign="left"))
                        input("Pressione Enter para continuar...")
                        print("\n============================================================\n")
                    case "2":
                        num_linhas, num_colunas = df.shape
                        print("Número de linhas:", num_linhas)
                        print("Número de colunas:", num_colunas)
                        input("\nPressione Enter para continuar...")
                    case "3":
                        print(tabulate(df.head(int(input("Informe quantas linhas serão exibidas: "))), headers='keys',
                                       tablefmt='psql', stralign='left'))
                        input("\nPressione Enter para continuar...")
                    case "4":
                        print("============================================================\n")
                        print(tabulate(df.T, headers='keys', tablefmt='psql', stralign='left'))
                        input("\nPressione Enter para continuar...")
                    case "5":
                        listaColunas = df.columns.tolist()
                        print("\nTodas as colunas:\n",
                              tabulate([], headers=listaColunas, tablefmt="pipe", stralign="center"), sep="")

                        coluna1 = input("\nDigite o nome da primeira coluna: ")
                        if coluna1 in listaColunas:
                            coluna2 = input("Digite o nome da segunda coluna: ")
                            if coluna2 in listaColunas:
                                colunaEspec = df[[coluna1, coluna2]]
                                print(tabulate(colunaEspec, headers='keys', tablefmt='psql', stralign='left'))
                            else:
                                print(f"\nERRO: '{coluna2}' não é uma coluna da base de dados!\n")
                        else:
                            print(f"\nERRO: '{coluna1}' não é uma coluna da base de dados!\n")

                        input("Pressione Enter para continuar...")
                    case "6":
                        print("============================================================\n")
                        listaColunas = df.columns.tolist()
                        print("\nTodas as colunas:\n",
                              tabulate([], headers=listaColunas, tablefmt="pipe", stralign="center"), sep="")
                        coluna = input("\nInforme a coluna: ")
                        coluna = coluna.lower()
                        print("\n============================================================\n")
                        if coluna in listaColunas:
                            print("\n============================================================\n")
                            print(f"Coluna '{coluna}':\n", tabulate(df[[coluna]], headers='keys', tablefmt='psql'),
                                  sep="")
                        else:
                            print(f"'ERRO: {coluna}' não é uma das colunas!")
                        print("\n============================================================\n")
                        input("Pressione Enter para continuar...")
                    case "7":
                        print("============================================================\n")
                        print("1- Pesquisar registro por index")
                        print("2- Pesquisar registro por nome")
                        print("\n============================================================\n")
                        vR_resp = input("Favor escolher opção: ")
                        if vR_resp == "1":
                            num_rotulos = len(df.index)
                            print("\n============================================================\n")
                            print("\nTotal de index: ", num_rotulos)
                            index = int(input("Informe o index do registro buscado: "))
                            if index > num_rotulos:
                                print(f"\nERRO: '{index}' não é um dos index do dataBase!\n")
                            else:
                                print("\n============================================================\n")
                                print(f"Registro:\n")
                                print(tabulate(df.loc[[index]], headers='keys', tablefmt='psql', stralign="left"))
                            input("Pressione Enter para continuar...")
                        elif vR_resp == "2":
                            print("\n============================================================\n")
                            registro = input("Digite o nome do registro pesquisado: ")
                            print("\n============================================================\n")
                            # A função applymap() é usado para aplicar a função lambda em cada célula do dataframe df.
                            # A função lambda verifica se o valor é uma "string" e, se for, aplica a função lower()
                            # para transformar o valor em minúsculas.
                            df_lower = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
                            if registro.lower() in df_lower['nome'].tolist():
                                print(tabulate(df_lower[df_lower['nome'] == registro.lower()], headers='keys',
                                               tablefmt='psql', stralign="left"))
                            else:
                                print(f"ERRO: '{registro}' não está no dataBase!")
                            print("\n============================================================\n")
                            input("Pressione Enter para continuar...")
                    case "8":
                        break
                    case _:
                        print("Opção inválida!")
                        input("\nPressione Enter para continuar...")
        case "2":
            while True:
                print("\n============================================================\n")
                print("Tela de adição de dados do DataBase")
                print("\n============================================================\n")
                print("1- Adicionar registro no final")
                print("2- Adicionar registro em local especifico")
                print("3- Voltar para menu")
                print("\n============================================================\n")
                add_resp = input("Favor escolher opção: ")
                print("\n============================================================\n")
                match add_resp:
                    case "1":
                        print("\n============================================================\n")
                        listaColunas = df.columns.tolist()
                        print("\nTodas as colunas:\n",
                              tabulate([], headers=listaColunas, tablefmt="pipe", stralign="center"), sep="")
                        nome = input("Nome: ")
                        dtLancamento = input("Data de Lançamento: ")
                        categoria = input("Categoria: ")
                        desenvolvedor = input("Desenvolvedor: ")
                        desc = input("Descrição: ")
                        df.loc[len(df)+1] = [nome, dtLancamento, categoria, desenvolvedor, desc]
                        print("\nRegistro salvo com sucesso!")
                        print("\n============================================================\n")
                        input("Pressione Enter para continuar...")
                    case "2":
                        print("\n============================================================\n")
                        num_rotulos = len(df.index)
                        print("\nTotal de index: ", num_rotulos, end="\n\n")
                        index = int(input("Informe a indexação onde quer adicionar: "))
                        if index > num_rotulos:
                            print(f"\nERRO: '{index}' está além do número de rotulos/index!")
                        else:
                            print("\nTodas as colunas: \n",
                                  tabulate([], headers=df.columns.tolist(), tablefmt='pipe', stralign='left'),
                                  end="\n\n", sep="\n")
                            nome = input("Nome: ")
                            dtLancamento = input("Data de Lançamento: ")
                            categoria = input("Categoria: ")
                            desenvolvedor = input("Desenvolvedor: ")
                            desc = input("Descrição: ")

                            # Dividir o DataFrame em duas partes
                            parte1 = df.iloc[:index]
                            parte2 = df.iloc[index:]

                            # Cria um novo DataFrame para o novo registro
                            novo_registro = pd.DataFrame({'nome': [nome],
                                                          'data lançamento': [dtLancamento],
                                                          'categoria': [categoria],
                                                          'desenvolvedor': [desenvolvedor],
                                                          'descrição': [desc]})

                            # Concatena os 3 DataFrame's no original
                            df = pd.concat([parte1, novo_registro, parte2], ignore_index=True)

                            # Recria a indexação do DataFrame
                            df.index = [int(x) for x in range(1, df.index.size + 1)]

                            print("\n registro salvo com sucesso!")
                        print("\n============================================================\n")
                        input("Pressione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
                        input("Pressione Enter para continuar...")
        case "3":
            while True:
                print("============================================================\n")
                print("Tela de deleção de dados do DataBase")
                print("\n============================================================\n")
                print("1- Deletar registro por index")
                print("2- Deletar registro por nome")
                print("3- Voltar para o menu")
                print("\n============================================================\n")
                del_resp = input("Favor escolher opção: ")
                match del_resp:
                    case "1":
                        num_rotulos = len(df.index)
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(tabulate([df.nome], headers="keys", tablefmt="psql"))
                        print("\nTotal de index: ", num_rotulos)
                        index = int(input("Informe o index do registro que deseja deletar: "))
                        print("\n============================================================\n")
                        if index > num_rotulos:
                            print(f"ERRO: '{index}' está além do número de rotulos/index!\n")
                        else:
                            print(f"registro:\n")
                            print(tabulate([df.loc[index]], headers="keys", tablefmt="psql"))
                            certeza = input("Deseja mesmo deletá-lo? (S/N) ")
                            if certeza.lower() == "s":
                                df = df.drop(index).reset_index(drop=True)
                                df.index = [int(x) for x in range(1, df.index.size + 1)]
                                print("\nRegistro deletado com sucesso!")
                            elif certeza.lower() == "n":
                                print("\nOK")
                            else:
                                print("\nOpção inválida!")
                        input("Pressione Enter para continuar...")
                        print("============================================================\n")
                    case "2":
                        print("\n============================================================\n")
                        print(tabulate([df.nome], headers="keys", tablefmt="grid", stralign="left"))
                        registro = input("\nDigite o nome que deseja deletar: ")
                        print("\n============================================================\n")

                        df_lower = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
                        if registro.lower() in df_lower['nome'].tolist():
                            print("Registro: \n")
                            print(tabulate(df_lower[df_lower['nome'] == registro.lower()], headers='keys',
                                           tablefmt='psql'))
                            certeza = input("Deseja mesmo deletá-lo? (S/N) ")
                            if certeza.lower() == "s":
                                df = df_lower[df_lower['nome'] != registro.lower()].reset_index(drop=True)
                                df.index = [int(x) for x in range(1, df.index.size + 1)]
                                print("\nRegistro deletado com sucesso!")
                            elif certeza.lower() == "n":
                                print("OK\n")
                            else:
                                print("Opção inválida!\n")
                        else:
                            print(f"'{registro}' não está no dataBase!")
                        print("\n============================================================\n")
                        input("Pressione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
                        input("Pressione Enter para continuar...")
        case "4":
            while True:
                print("\n============================================================\n")
                print("Tela de atualização de dados do DataBase")
                print("\n============================================================\n")
                print("1- Alterar registro inteiro;")
                print("2- Alterar célula especifica de um registro;")
                print("3- Voltar para o menu.")
                print("\n============================================================\n")
                upp_resp = input("Favor escolher opção: ")
                match upp_resp:
                    case "1":
                        num_rotulos = len(df.index)
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(tabulate([df.nome], headers="keys", tablefmt="psql"))
                        print("\nTotal de index: ", num_rotulos)
                        index = int(input("Informe o index do registro que deseja alterar: "))
                        print("\n============================================================\n")
                        if index > num_rotulos:
                            print(f"ERRO: '{index}' está além do número de rotulos/index!\n")
                        else:
                            print(f"registro:\n")
                            print(tabulate([df.loc[index]], headers="keys", tablefmt="psql"))
                            print("\n============================================================\n")
                            nome = input("\nNome: ")
                            dtLancamento = input("Data de Lançamento: ")
                            categoria = input("Categoria: ")
                            desenvolvedor = input("Desenvolvedor: ")
                            desc = input("Descrição: ")
                            df.loc[index] = [nome, dtLancamento, categoria, desenvolvedor, desc]
                            print("\nRegistro alterado com sucesso!\n")
                        input("Pressione Enter para continuar...")
                        print("\n============================================================\n")
                    case "2":
                        num_rotulos = len(df.index)
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(tabulate([df.nome], headers="keys", tablefmt="psql"))
                        print("\n============================================================\n")
                        print("Total de index: ", num_rotulos)
                        index = int(input("Informe o index do registro que deseja alterar: "))
                        if index > num_rotulos:
                            print(f"ERRO: '{index}' está além do número de rotulos/index!\n")
                            input("Pressione Enter para continuar...")
                            continue
                        print("\n============================================================\n")
                        dfColuna = df.columns.tolist()
                        print("Colunas: \n", tabulate([], headers=dfColuna, tablefmt="pipe", stralign="center"), sep="")
                        coluna = input("\nInforme a coluna que deseja alterar: ")
                        print("\n============================================================\n")
                        if coluna not in dfColuna:
                            print(f"ERRO: '{coluna}' não é uma das colunas!\n")
                        else:
                            print(f"registro:\n")
                            print(df.at[index, coluna])
                            print("\n============================================================\n")
                            alter = input("Informe a alteração: ")
                            df.at[index, coluna] = alter
                            print("\nRegistro alterado com sucesso!\n")
                        print("\n============================================================\n")
                        input("Pressione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
        case "5":
            print("Adeus!")
            break
        case _:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

df.to_csv(caminhoDataBase, index=False)
