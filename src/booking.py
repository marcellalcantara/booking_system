import beaupy
from datetime import datetime
from src.fileStore import loadData, writeData
from src.validations import inicio, fim, totalDias, calcularDesconto, importIdCar, importIdClient, valorTotal, integerNumber

#Retorna a lista de booking carregada a partir do arquivo "bookingList.json"
def bookingList():
    return loadData("files/bookingList.json")

#Imprimir os dados do cliente  
def printBooking(booking):print(f"""
    \033[34mID:\033[0m {booking['id']} \033[34mInício:\033[0m {booking['dataInicio'].split()[0]} \033[34mFim:\033[0m {booking['dataFim'].split()[0]} \033[34mQuantidade de dias:\033[0m {booking['totalDias']} dias
    \033[34mCliente:\033[0m {booking['cliente_id'][0]} - {booking['cliente_id'][1]}
    \033[34mAutomóvel:\033[0m {booking['automovel_id'][0]} - {booking['automovel_id'][1]}({booking['automovel_id'][2]}) Matrícula:{booking['automovel_id'][4]}
    \033[34mValor total:\033[0m {booking['valorTotal']:.2f}€. Nessa reserva você obteve um desconto de: {booking['desconto']*100}%.
    """)
    
#Imprimir as reservas passadas
def pastBookings():
    currentDate = datetime.now().date()
    print("\nReservas Passadas:\n")
    for booking in bookingList():
        startDate = datetime.strptime(booking['dataInicio'].split()[0], '%Y-%m-%d').date()
        if startDate < currentDate:
            printBooking(booking)
        else:
            print("\nNão existe reserva passada!\n")

#Imprimir as reservas futuras considerando a data de execução
def futureBookings():
    currentDate = datetime.now().date()
    print("\nReservas Futuras:\n")
    for booking in bookingList():
        startDate = datetime.strptime(booking['dataInicio'].split()[0], '%Y-%m-%d').date()
        if startDate >= currentDate:
            printBooking(booking)
        else:
            print("\nNão existe reserva futura!\n")

#Chama a função imprimir
def printAllBooking():
    print("\nListagem de reservas: \n")
    if len(bookingList()) > 0:
        for booking in bookingList():
            listB = ["1 - Reservas Passadas", "2 - Reservas Futuras", "3 - Voltar"]
            op = beaupy.select(listB, cursor='=>', cursor_style='blue', return_index=True)+1
            match op:
                case 1:
                   pastBookings() 
                case 2:
                    futureBookings()
                case 3: 
                    print("Voltando...")
                    return 
    else:
        print("\nAinda não foram registados reservas!\n")

#Define o ID da reserva
def getbookingID():
    listID = [booking['id'] for booking in bookingList()]
    return listID[-1] + 1

#Insere os dados da reserva
def insertBooking():
    print("\nInsira os dados da reserva: \n") 

    newBooking = {}
    newBooking['id'] = getbookingID()
    newBooking['dataInicio'] = inicio()
    newBooking['dataFim'] = fim(newBooking['dataInicio'])
    newBooking['totalDias'] = totalDias(newBooking['dataInicio'], newBooking['dataFim'])
    newBooking['cliente_id'] = importIdClient() 
    newBooking['automovel_id'] = importIdCar() 
    newBooking['desconto'] = calcularDesconto(newBooking['totalDias'])
    newBooking['valorTotal'] = valorTotal(newBooking['automovel_id'][3], newBooking['totalDias'],  newBooking['desconto'])

    if not canBook(newBooking['automovel_id'][0], newBooking['dataInicio'], newBooking['dataFim']):
        print("Não foi possível realizar a reserva. Tente novamente.")
        return

    list = bookingList()
    list.append(newBooking)
    writeData(list, 'files/bookingList.json')
    print("Reserva adicionada com sucesso!")

#Verificar se a reserva escolhida está correta
def createBookingMenu(bookingSearch):
    temp = []
    for booking in bookingSearch:
        temp.append(f"{booking['id']} - {booking['cliente_id'][1]} - {booking['automovel_id'][4]}")
    return temp

#Atualizar cada campo da reserva
def bookingUpdate(booking):
    print(f"\nAtualização da reserva nº: {booking['id']}:\n")
    updateList = ["1 - Data início", "2 - Data fim", "3 - Cliente", "4 - Automóvel", "5 - Voltar"]
    op = beaupy.select(updateList, cursor='=>', cursor_style='blue', return_index=True)+1
    match op:
        case 1:
            booking['dataInicio'] = inicio()
        case 2:
            booking['dataFim'] = fim(booking['dataInicio'])
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

#Deletar reserva
def bookingDelete(booking):
    bookingListData = bookingList()
    for i, c in enumerate(bookingListData):
        if c['id'] == booking['id']:
            del bookingListData[i] 
            break
    writeData(bookingListData, 'files/bookingList.json')

#Pesquisar pelo ID da reserva
def searchBooking():
    bookingSearch = []
    bookingID = integerNumber()
    print(f"\nPesquisa da reserva pelo nº da reserva: {bookingID}. Está correto?\n")
    for booking in bookingList():
        if booking['id'] == int(bookingID):
            bookingSearch.append(booking)
    
    if len(bookingSearch) > 0:
        listSearch = createBookingMenu(bookingSearch)
        op = beaupy.select(listSearch, cursor='=>', cursor_style='blue', return_index=True)
        printBooking(bookingSearch[op])

        optionsList = ["1 - Atualizar", "2 - Deletar", "3 - Voltar"]
        op1 = beaupy.select(optionsList, cursor='=>', cursor_style='blue', return_index=True)+1
        match op1:
            case 1:
                bookingUpdate(bookingSearch[op])
                print("\nReserva atualizada com sucesso!\n")
            case 2:
                bookingDelete(bookingSearch[op])
                print("\nReserva removida com sucesso!\n")
            case 3:
                print("Voltando...")
    else:
        print("\nNão foram encontrados resultados com o critério definido!\n")

#Menu principal da reserva
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

#Comparar ID do automóvel
def bookingsByCar(automovelId):
    return [booking for booking in bookingList() if booking['automovel_id'][0] == automovelId]

#Evitar conflitos de reserva
def canBook(automovelId, dataInicio, dataFim):
    bookings = bookingsByCar(automovelId)
    
    if len(bookings) == 0:
        print("\nEste carro está disponível para a data escolhida.")
        return True
    else:
        for booking in bookings:
            inicio_reserva = datetime.strptime(booking['dataInicio'], '%Y-%m-%d %H:%M:%S')
            fim_reserva = datetime.strptime(booking['dataFim'], '%Y-%m-%d %H:%M:%S')
            
            if (dataInicio >= inicio_reserva and dataInicio <= fim_reserva) or (dataFim >= inicio_reserva and dataFim <= fim_reserva):
                print("\nEste carro já está reservado para essa data. Por favor, escolha outra data.")
                return False
        
        print("\nEste carro está disponível para a data escolhida.")
        return True