import beaupy
from datetime import datetime
from src.fileStore import loadData, writeData
from src.validations import inicio, fim, totalDias, calcularDesconto, importIdCar, importIdClient, valorTotal, integerNumber
from src.client import clientList
from src.car import carList

def bookingList():
    return loadData("files/bookingList.json")
  
def printbooking(booking):
    print(f"""
          \033[34mID:\033[0m {booking['id']} \033[34mInício:\033[0m {booking['dataInicio']} \033[34mFim:\033[0m {booking['dataFim']} \033[34mQuantidade de dias:\033[0m {booking['totalDias']} dias
          \033[34mCliente:\033[0m {booking['cliente_id'][0]} - {booking['cliente_id'][1]}
          \033[34mAutomóvel:\033[0m {booking['automovel_id'][0]} - {booking['automovel_id'][1]}({booking['automovel_id'][2]}) Matrícula:{booking['automovel_id'][4]}
          \033[34mValor total:\033[0m {booking['valorTotal']:.2f}€. Nessa reserva você obteve um desconto de: {booking['desconto']}%.
          """)

def printAllBooking():
    print("\nListagem de reservas: \n")
    if len(bookingList()) > 0:
        for booking in bookingList():
            printbooking(booking)
    else:
        print("\nAinda não foram registados reservas!\n") 

def insertBooking():
    print("\nInsira os dados da reserva: \n") 
    count = len(bookingList()) + 999 #Iniciando o id em 1000
    id = count + 1

    newBooking = {}
    newBooking['id'] = id
    newBooking['dataInicio'] = inicio()
    newBooking['dataFim'] = fim()
    newBooking['cliente_id'] = importIdClient() 
    newBooking['automovel_id'] = importIdCar() 
    newBooking['totalDias'] = totalDias(newBooking['dataInicio'], newBooking['dataFim'])
    newBooking['desconto'] = calcularDesconto(newBooking['totalDias'])
    newBooking['valorTotal'] = valorTotal(newBooking['automovel_id'][3], newBooking['totalDias'],  newBooking['desconto'])

    list = bookingList()
    list.append(newBooking)
    writeData(list, 'files/bookingList.json')
    print("Reserva adicionada com sucesso!")


def creatBookingMenu(bookingSearch):
    temp = []
    for booking in bookingSearch:
        temp.append(f"{booking['id']} - {booking['cliente_id']} - {booking['automovel_id']}")
    return temp

def bookingUpdate(booking):
    print(f"\nAtualização da reserva nº: {booking['id']}:\n")
    updateList = ["1 - Data início", "2 - Data fim", "3 - Cliente", "4 - Automóvel", "5 - Voltar"]
    op = beaupy.select(updateList, cursor='=>', cursor_style='blue', return_index=True)+1
    match op:
        case 1:
            booking['dataInicio'] = inicio()
        case 2:
            booking['dataFim'] = fim()
        case 3: 
            booking['cliente_id'] = importIdClient()
        case 4: 
            booking['automovel_id'] = importIdCar()
        case 5:
            print("Voltando...")

    updateField = bookingList()
    for i, c in enumerate(updateField):
        if c['id'] == booking['id']:
            updateField[i] = booking
            break
    writeData(updateField, 'files/bookingList.json')    

def bookingDelete(booking):
    bookingListData = bookingList()
    for i, c in enumerate(bookingListData):
        if c['id'] == booking['id']:
            del bookingListData[i] 
            break
    writeData(bookingListData, 'files/bookingList.json')

def searchBooking():
    bookingSearch = []
    bookingId = integerNumber()
    print(f"\nPesquisa da reserva pelo nº da reserva: {bookingId}. Está correto?\n")
    for booking in bookingList():
        if booking['id'] == bookingId:
            bookingSearch.append(booking)
    else:
        if bookingSearch:
            idSearch = creatBookingMenu(bookingSearch)
            op = beaupy.select(idSearch, cursor='=>', cursor_style='blue', return_index=True)
            printbooking(bookingSearch[op])

            optionsList = ["1 - Atualizar", "2 - Deletar", "3 - Voltar"]
            op1 = beaupy.select(optionsList, cursor='=>', cursor_style='blue', return_index=True)
            if op1 == 0: #Atualizar
                bookingUpdate(bookingSearch[op])
                print("\nCarro atualizado com sucesso!\n")
            elif op1 == 1: #Apagar
                bookingDelete(bookingSearch[op])
                print("\nReserva removida com sucesso!\n")
            else:
                return
        else:
            print("\nNão foram encontrados resultados com o critério definido!\n")

def bookingMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu das reservas:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='blue', return_index=True)+1
        match op:
            case 1:
                printAllBooking()
            case 2:
                insertBooking()
            case 3:
                searchBooking()
            case 4:
                print("Voltando...")
                break
            case _:
                print("\nErro: opção inválida!\n")