import beaupy
from datetime import datetime
from src.fileStore import loadData, writeData
from src.validations import inicio, fim, totalDias, calcularDesconto, importIdCar, importIdClient, valorTotal
from src.client import clientList
from src.car import carList

def bookingList():
    return loadData("files/bookingList.json")
'''     
def printbooking(booking):
    print(f"""
          |Início: {booking['dataInicio']}| |Fim: {booking['dataFim']}| |Quantidade de dias: {booking['totalDias']}|
          |Cliente: {booking['cliente_id']} Cliente:| 
          |Automóvel: {booking['automovel_id']} Marca:  Matrícula: | 
          |Valor total: {booking['valorTotal']}|   Desconto: {booking['desconto']}
          """)'''
def printbooking(booking):
    print(f"""
          |Início: {booking['dataInicio']}| |Fim: {booking['dataFim']}| |Quantidade de dias: {booking['totalDias']}|
               | Desconto: {booking['desconto']}|   |Preço diário: {booking['precoDiario']}
            |Automóvel: {booking['automovel_id']} Matrícula: |Marca:

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

    newBooking = {}
    newBooking['dataInicio'] = inicio()
    newBooking['dataFim'] = fim()
    newBooking['cliente_id'] = importIdClient() 
    newBooking['automovel_id'] = importIdCar() 
    newBooking['totalDias'] = totalDias(newBooking['dataInicio'], newBooking['dataFim'])
    newBooking['desconto'] = calcularDesconto(newBooking['totalDias'])
    newBooking['valorTotal'] = valorTotal()

    list = bookingList()
    list.append(newBooking)
    writeData(list, 'files/bookingList.json')
    print("Reserva adicionada com sucesso!")


def searchBooking():
    print("\nPesquisar reserva: \n")
#    menu3(cliente)

def bookingMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu das reservas:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='green', return_index=True)+1
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