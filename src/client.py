import beaupy

from src.fileStore import loadData, writeData
from src.validations import validarNome, validarNif, validarNifUpdate, validarDataNascimento, validarTelefone, validarEmail, getClientID

def clientList():
    return loadData("files/clientList.json")

def printClient(client):
    print(f"""
          \033[34mID:\033[0m {client['id']} \033[34mNome:\033[0m {client['nome']} \033[34mNIF:\033[0m {client['NIF']}
          \033[34mData de nascimento:\033[0m {client['dataNascimento'].split()[0]} \033[34mTelefone:\033[0m {client['telefone']}
          \033[34mE-mail:\033[0m {client['email']}
          """)

def printAllClients():
    print("\nListagem de clientes:")
    if len(clientList()) > 0:
        for client in clientList():
            printClient(client)
    else:
        print("\nAinda não foram registados clientes!\n")


def insertClient():
    print("\nInsira os dados do Cliente: \n")
    
    newClient = {}
    newClient['id'] = getClientID()
    newClient['nome'] = validarNome()
    newClient['NIF'] = validarNif()
    newClient['dataNascimento'] = validarDataNascimento() 
    newClient['telefone'] = validarTelefone()
    newClient['email'] = validarEmail()

    list = clientList()
    list.append(newClient)
    writeData(list, 'files/clientList.json')
    print("Cliente adicionado com sucesso!")

def creatClientMenu(clientSearch):
    temp = []
    for client in clientSearch:
        temp.append(f"{client['NIF']} - {client['nome']}")
    return temp

def clientUpdate(client):
    print(f"\nAtualização do cliente {client['nome']}:\n")
    updateList = ["1 - Nome", "2 - Data de nascimento", "3 - Telefone", "4 - E-mail", "5 - Voltar"]
    op = beaupy.select(updateList, cursor='=>', cursor_style='blue', return_index=True)+1
    match op:
        case 1:
            client['nome'] = validarNome()
        case 2:
            client['dataNascimento'] = validarDataNascimento()
        case 3: 
            client['telefone'] = validarTelefone()
        case 4: 
            client['email'] = validarEmail()
        case 5:
            print("Voltando...")

    updateField = clientList()
    for i, c in enumerate(updateField):
        if c['id'] == client['id']:
            updateField[i] = client
            break
    writeData(updateField, 'files/clientList.json')    

def clientDelete(client):
    clientListData = clientList()
    for i, c in enumerate(clientListData):
        if c['id'] == client['id']:
            del clientListData[i] 
            break
    writeData(clientListData, 'files/clientList.json')

def searchClient():
    clientSearch = []
    nif = validarNifUpdate()
    print(f"\nPesquisa de cliente pelo NIF: {nif}. O nome está correto?\n")
    for client in clientList():
        if client['NIF'] == nif:
            clientSearch.append(client)
    else:
        if clientSearch:
            nifSearch = creatClientMenu(clientSearch)
            op = beaupy.select(nifSearch, cursor='=>', cursor_style='blue', return_index=True)
            printClient(clientSearch[op])

            optionsList = ["1 - Atualizar", "2 - Deletar", "3 - Voltar"]
            op1 = beaupy.select(optionsList, cursor='=>', cursor_style='blue', return_index=True)+1
            match op1:
                case 1:
                    clientUpdate(clientSearch[op])
                    print("\nCliente atualizado com sucesso!\n")
                case 2:
                    clientDelete(clientSearch[op])
                    print("\nCliente removido com sucesso!\n")
                case 3:
                    print("Voltando...") 
        else:
            print("\nNão foram encontrados resultados com o critério definido!\n")

def clientMenu():
    while True:
        list = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu dos clientes:\n")  
        op = beaupy.select(list, cursor='=>', cursor_style='blue', return_index=True)+1
        match op:
            case 1:
                printAllClients()
            case 2:                      
                insertClient()
            case 3:
                searchClient()
            case 4:
                print("Voltando...")
                break
            case _:
                print("\nErro: opção inválida!\n")