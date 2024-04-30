import beaupy

from src.fileStore import loadData, writeData
from src.validations import validarNome, validarNif, validarDataNascimento, validarTelefone, validarEmail

def clientList():
    return loadData("files/clientList.json")

def printAllClients():
    print("\nListagem de clientes: \n")
    if len(clientList()) > 0:
        for cliente in clientList():
            print(f"id: {cliente['id']} Nome: {cliente['nome']} NIF: {cliente['NIF']} Data de nascimento: {cliente['data de Nascimento']} Telefone: {cliente['telefone']} E-mail: {cliente['email']}")
    else:
        print("\nAinda não foram registados clientes!\n")

def insertClient():
    print("\nInsira os dados do Cliente: \n")

    count = len(clientList()) # Iniciando o id
    id = count + 1
    
    newClient = {}
    newClient['id'] = id
    newClient['nome'] = validarNome()
    newClient['NIF'] = validarNif()
    newClient['data de Nascimento'] = validarDataNascimento() 
    newClient['telefone'] = validarTelefone()
    newClient['email'] = validarEmail()

    list = clientList()
    list.append(newClient)
    writeData(list, 'files/clientList.json')
    print("Cliente adicionado com sucesso!")

def searchClient():
    print("\nPesquisar Cliente: \n")
    nif = input("Insira o NIF do cliente: ")
    for cliente in clientList():
        if cliente['NIF'] == nif:
            print(f"id: {cliente['id']} Nome: {cliente['nome']} NIF: {cliente['NIF']} Data de nascimento: {cliente['data de Nascimento']} Telefone: {cliente['telefone']} E-mail: {cliente['email']}")
#            menu3(cliente)
            break
    else:
        print("Cliente não encontrado!")

def clientMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu dos clientes:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='green', return_index=True)+1
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