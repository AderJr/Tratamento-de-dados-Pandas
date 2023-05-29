import pandas as pd

#lembrando que aqui onde você irá colocar o caminho do DataBase
caminhoDataBase = 'DataBase jogos - Página1_2.csv'
df = pd.read_csv(caminhoDataBase)

def telaInicial():
    print("\n============================================================\n")
    print("Bem vido ao menu de manipulação de dados!")
    print("\n============================================================\n")
    print("1- Mostrar DataBase;")
    print("2- Adicionar registro;")
    print("3- Deletar registro;")
    print("4- Alterar registro;")
    print("5- Sair.")
    print("\n============================================================\n")
    resp = input("Favor escolher opção: ")
    print("\n============================================================\n")
    return resp

while True:
    resp = telaInicial()
    match resp:
        case "1":
            while True:
                print("\n============================================================\n")
                print("Tela de vizualização de DataBase")
                print("\n============================================================\n")
                print("1- Mostrar DataBase completo;")
                print("2- Pesquisar coluna;")
                print("3- Pesguisar registro;")
                print("4- Voltar para menu.")
                print("\n============================================================\n")
                viz_resp = input("Favor escolher opção: ")
                print("\n============================================================\n")
                match viz_resp:
                    case "1":
                        print("\n============================================================\n")
                        print("DataBase completo")
                        print(df)
                        input("Precione Enter para continuar...")
                        print("\n============================================================\n")
                    case "2":
                        print("\n============================================================\n")
                        listaColunas = df.columns.tolist()
                        print("\nTodas as colunas: ", listaColunas)
                        coluna = input("\nInforme a coluna: ")
                        coluna = coluna.lower()
                        print("\n============================================================\n")
                        if coluna in listaColunas:
                            print("\n============================================================\n")
                            print(f"Coluna '{coluna}':\n")
                            print(df[coluna])
                        else:
                            print("{} não é uma das colunas!")
                        print("\n============================================================\n")
                        input("Precione Enter para continuar...")
                    case "3":
                        print("\n============================================================\n")
                        print("1- Pesquisar registro por index;")
                        print("2- Pesquisar registro por nome.")
                        print("\n============================================================\n")
                        vR_resp = input("Favor escolher opção: ")
                        if vR_resp == "1":
                            num_rotulos = len(df.index) - 1
                            print("\n============================================================\n")
                            print("\nTotal de index: ", num_rotulos)
                            index = int(input("Informe o index do registro buscado: "))
                            if index > num_rotulos:
                                print(f"\n'{index}' não é um dos index do dataBase!\n")
                            else:
                                print("\n============================================================\n")
                                print(f"registro:\n")
                                print(df.loc[index])
                            input("Precione Enter para continuar...")
                            print("\n============================================================\n")
                        elif vR_resp == "2":
                            print("\n============================================================\n")
                            registro = input("Digite o resgistro pesquisado: ")
                            print("\n============================================================\n")
                            if registro in df.nome.tolist():
                                print(df[df.nome == registro])
                            else:
                                print(f"'{registro}' não está no dataBase!")
                            print("\n============================================================\n")
                            input("Precione Enter para continuar...")
                    case "4":
                        break
                    case _:
                        print("Opção inválida!")
                        input("\nPrecione Enter para continuar...")
        case "2":
            while True:
                print("\n============================================================\n")
                print("Tela de adição de dados do DataBase")
                print("\n============================================================\n")
                print("1- Adicionar registro no final;")
                print("2- Adicionar registro em local especifico;")
                print("3- Voltar para menu.")
                print("\n============================================================\n")
                add_resp = input("Favor escolher opção: ")
                print("\n============================================================\n")
                match add_resp:
                    case "1":
                        print("\n============================================================\n")
                        print("\nTodas as colunas: ", df.columns.tolist(), end="\n\n")
                        nome = input("Nome: ")
                        dtLancamento = input("Data de Lançamento: ")
                        categoria = input("Categoria: ")
                        desenvolvedor = input("Desenvolvedor: ")
                        desc = input("Descrição: ")
                        df.loc[len(df)] = [nome, dtLancamento, categoria, desenvolvedor, desc]
                        print("\n registro salvo com sucesso!")
                        print("\n============================================================\n")
                        input("Precione Enter para continuar...")
                    case "2":
                        print("\n============================================================\n")
                        num_rotulos = len(df.index) -1
                        print("\nTotal de index: ", num_rotulos, end="\n\n")
                        index = int(input("Informe a indexação onde quer adicionar: "))
                        if index > num_rotulos:
                            print(f"\n{index} está além do número de rotulos/index!")
                        else:
                            print("\nTodas as colunas: ", df.columns.tolist(), end="\n\n")
                            nome = input("Nome: ")
                            dtLancamento = input("Data de Lançamento: ")
                            categoria = input("Categoria: ")
                            desenvolvedor = input("Desenvolvedor: ")
                            desc = input("Descrição: ")
                            df.loc[index] = [nome, dtLancamento, categoria, desenvolvedor, desc]
                            print("\n registro salvo com sucesso!")
                        print("\n============================================================\n")
                        input("Precione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
                        input("Precione Enter para continuar...")
        case "3":
            while True:
                print("\n============================================================\n")
                print("Tela de deleção de dados do DataBase")
                print("\n============================================================\n")
                print("1- Deletar registro por index;")
                print("2- Deletar registro por nome;")
                print("3- Voltar para o menu.")
                print("\n============================================================\n")
                del_resp = input("Favor escolher opção: ")
                match del_resp:
                    case "1":
                        num_rotulos = len(df.index)
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(df.nome)
                        print("\nTotal de index: ", num_rotulos - 1)
                        index = int(input("Informe o index do registro que deseja deletar: "))
                        print("\n============================================================\n")
                        if index > num_rotulos:
                            print(f"{index} está além do número de rotulos/index!\n")
                        else:
                            print(f"registro:\n")
                            print(df.loc[index])
                            certeza = input("Deseja mesmo deletá-lo? (s/n) ")
                            if certeza.lower() == "s":
                                df = df.drop(index)
                                print("\nRegistro deletado com sucesso!")
                            elif certeza.lower() == "n":
                                print("\nOK")
                            else:
                                print("\nOpção inválida!")
                        input("Precione Enter para continuar...")
                        print("\n============================================================\n")
                    case "2":
                        print("\n============================================================\n")
                        print(df.nome)
                        registro = input("\nDigite o nome que deseja deletar: ")
                        print("\n============================================================\n")
                        if registro in df.nome.tolist():
                            print("registro: \n")
                            print(df[df.nome == registro])
                            certeza = input("Deseja mesmo deletá-lo? (s/n) ")
                            if certeza.lower() == "s":
                                df = df[df.nome == registro]
                                print("Registro deletado com sucesso!\n")
                            elif certeza.lower() == "n":
                                print("OK\n")
                            else:
                                print("Opção inválida!\n")
                        else:
                            print(f"'{registro}' não está no dataBase!")
                        print("\n============================================================\n")
                        input("Precione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
                        input("Precione Enter para continuar...")
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
                        num_rotulos = len(df.index) -1
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(df.nome)
                        print("\nTotal de index: ", num_rotulos)
                        index = int(input("Informe o index do registro que deseja alterar: "))
                        print("\n============================================================\n")
                        if index > num_rotulos:
                            print(f"{index} está além do número de rotulos/index!\n")
                        else:
                            print(f"registro:\n")
                            print(df.loc[index])
                            print("\n============================================================\n")
                            nome = input("\nNome: ")
                            dtLancamento = input("Data de Lançamento: ")
                            categoria = input("Categoria: ")
                            desenvolvedor = input("Desenvolvedor: ")
                            desc = input("Descrição: ")
                            df.loc[index] = [nome, dtLancamento, categoria, desenvolvedor, desc]
                            print("\nRegistro alterado com sucesso!\n")
                        input("Precione Enter para continuar...")
                        print("\n============================================================\n")
                    case "2":
                        num_rotulos = len(df.index) - 1
                        print("\n============================================================\n")
                        print("Todos os registros por index e nome: \n")
                        print(df.nome)
                        print("\n============================================================\n")
                        print("Total de index: ", num_rotulos)
                        index = int(input("Informe o index do registro que deseja alterar: "))
                        if index > num_rotulos:
                            print(f"{index} está além do número de rotulos/index!\n")
                            input("Precione Enter para continuar...")
                            continue
                        print("\n============================================================\n")
                        dfColuna = df.columns.tolist()
                        print("Colunas: ", dfColuna)
                        coluna = input("\nInforme a coluna que deseja alterar: ")
                        print("\n============================================================\n")
                        if coluna not in dfColuna:
                            print(f"{coluna} não é uma das colunas!\n")
                        else:
                            print(f"registro:\n")
                            print(df.at[index, coluna])
                            print("\n============================================================\n")
                            alter = input("Informe a alteração: ")
                            df.at[index, coluna] = alter
                            print("\nRegistro alterado com sucesso!\n")
                        print("\n============================================================\n")
                        input("Precione Enter para continuar...")
                    case "3":
                        break
                    case _:
                        print("Opção inválida!")
        case "5":
            print("Adeus!")
            break
        case _:
            print("Opção inválida!")
            input("Precione Enter para continuar...")

df.to_csv(caminhoDataBase, index=False)