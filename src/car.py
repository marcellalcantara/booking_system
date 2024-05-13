import beaupy

from datetime import datetime
from src.fileStore import loadData, writeData
from src.validations import matricula, matriculaUpdate, marca, cor, portas, validaPreco, validarCilindradas, validarPotencia
from src.booking import printBooking

#Retorna a lista de carros carregada a partir do arquivo "carList.json"
def carList():
    return loadData("files/carList.json")

#Retona a lista de reservas carregada a partir do arquivo "bookingList.json"
def bookingList():
    return loadData("files/bookingList.json")
#Imprime os detalhes de um carro
def printCar(automovel):
    print(f"""
    \033[34mID:\033[0m {automovel['id']} \033[34mMatrícula:\033[0m {automovel['matricula']} \033[34mMarca:\033[0m {automovel['marca']} \033[34mModelo:\033[0m {automovel['modelo']} 
    \033[34mCor:\033[0m {automovel['cor']} \033[34mPortas:\033[0m {automovel['portas']} \033[34mCilindrada:\033[0m {automovel['cilindrada']}cm3 \033[34mPotência:\033[0m {automovel['cilindrada']}cv
    \033[34mPreço diário:\033[0m {automovel['precoDiario']:.2f}€
    """) 
#Imprime os detalhes de todos os carros cadastrados
def printAllCars():
    print("\nListagem de Automóveis: \n")
    if len(carList()) > 0:
        for automovel in carList():
            printCar(automovel)
    else:
        print("\nAinda não foram registados carros!\n") 

#Imprimir as 5 últimas reservas da matricula em ordem decrescente 
def lastCarBookings(matricula, bookingList):
    carBooking = [booking for booking in bookingList if booking['automovel_id'][4] == matricula]
    carBooking.sort(key=lambda x: (x['id']), reverse=True)
    lastFiveBooking = carBooking[:5]
    print("\nÚltimas 5 reservas para o carro com matrícula", matricula, ":\n")
    if lastFiveBooking:
        for booking in lastFiveBooking:
            printBooking(booking)
    else:
        print("Não há reservas para este carro!\n")
        
#Define ID dos carros
def getCarID():
    listID = [car['id'] for car in carList()]
    return listID[-1] + 1

#Insere carros
def insertCar():
    print("\nInsira os dados do automóvel: \n")

    newCar = {}
    newCar['id'] = getCarID()
    newCar['matricula'] = matricula()
    newCar['marca'] = marca()
    newCar['modelo'] = input ("Modelo: ")
    newCar['cor'] = cor()
    newCar['portas'] = portas()
    newCar['precoDiario'] = validaPreco()
    newCar['cilindrada'] = validarCilindradas()
    newCar['potencia'] = validarPotencia()

    list = carList()
    list.append(newCar)
    writeData(list, 'files/carList.json')
    print("Automóvel adicionado com sucesso!")

#Verificar se o carro escolhido está correto    
def creatCarMenu(carSearch):
    temp = []
    for car in carSearch:
        temp.append(f"{car['matricula']} - {car['marca']}")
    return temp

#Atualizar carro
def carUpdate(car):
    print(f"\nAtualização do carro {car['matricula']}:\n")
    updateList = ["1 - Marca", "2 - Modelo", "3 - Cor", "4 - Portas", "5 - Preço diário", "6 - Cilindradas", "7 - Potência", "8 - Voltar"]
    op = beaupy.select(updateList, cursor='=>', cursor_style='blue', return_index=True)+1
    match op:
        case 1:
            car['marca'] = marca()
        case 2:
            car['modelo'] = input ("Modelo: ")
        case 3: 
            car['cor'] = cor()
        case 4: 
            car['portas'] = portas()
        case 5:
            car['precoDiario'] = validaPreco()
        case 6:
            car['cilindrada'] = validarCilindradas()
        case 7: 
            car['potencia'] = validarPotencia()
        case 8:
            print("Voltando...")

    updateField = carList()
    for i, c in enumerate(updateField):
        if c['id'] == car['id']:
            updateField[i] = car
            break
    writeData(updateField, 'files/carList.json')  

#Deletar carro
def carDelete(car):
    carListData = carList()
    for i, c in enumerate(carListData):
        if c['id'] == car['id']:
            del carListData[i] 
            break
    writeData(carListData, 'files/carList.json')

#Pesquisar pela matricula do carro
def searchCar():
    carSearch = []
    matricula = matriculaUpdate()
    print(f"\nPesquisa do automóvel pela matricula: {matricula}. A marca está correta?\n")
    for car in carList():
        if car['matricula'] == matricula:
            carSearch.append(car)
    else:
        if carSearch:
            matriculaSearch = creatCarMenu(carSearch)
            op = beaupy.select(matriculaSearch, cursor='=>', cursor_style='blue', return_index=True)
            printCar(carSearch[op])
            lastCarBookings(matricula, bookingList())

            optionsList = ["1 - Atualizar", "2 - Deletar", "3 - Voltar"]
            op1 = beaupy.select(optionsList, cursor='=>', cursor_style='blue', return_index=True) +1
            if op1 == 1: #Atualizar
                carUpdate(carSearch[op])
                print("\nCarro atualizado com sucesso!\n")
            elif op1 == 2: #Apagar
                carDelete(carSearch[op])
                print("\nCarro removido com sucesso!\n")
            else:
                return
        else:
            print("\nNão foram encontrados resultados com o critério definido!\n")  
#Menu principal do carro
def carMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu dos automóveis:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='blue', return_index=True)+1
        match op:
            case 1:
                printAllCars()
            case 2:
                insertCar()
            case 3:
                searchCar()
            case 4:
                print("Voltando...")
                break
            case _:
                print("\nErro: opção inválida!\n") 