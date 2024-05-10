import beaupy
from src.fileStore import loadData, writeData
from src.validations import matricula, matriculaUpdate, marca, cor, portas, validaPreco, validarCilindradas, validarPotencia, getCarID

def carList():
    return loadData("files/carList.json")

def printCar(automovel):
    print(f"""
          \033[34mID:\033[0m {automovel['id']} \033[34mMatrícula:\033[0m {automovel['matricula']} \033[34mMarca:\033[0m {automovel['marca']} \033[34mModelo:\033[0m {automovel['modelo']} 
          \033[34mCor:\033[0m {automovel['cor']} \033[34mPortas:\033[0m {automovel['portas']} \033[34mCilindrada:\033[0m {automovel['cilindrada']}cm3 \033[34mPotência:\033[0m {automovel['cilindrada']}cv
          \033[34mPreço diário:\033[0m {automovel['precoDiario']:.2f}€
          """) 

def printAllCars():
    print("\nListagem de Automóveis: \n")
    if len(carList()) > 0:
        for automovel in carList():
            printCar(automovel)
    else:
        print("\nAinda não foram registados carros!\n")  

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
    
def creatCarMenu(carSearch):
    temp = []
    for car in carSearch:
        temp.append(f"{car['matricula']} - {car['marca']}")
    return temp

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

def carDelete(car):
    carListData = carList()
    for i, c in enumerate(carListData):
        if c['id'] == car['id']:
            del carListData[i] 
            break
    writeData(carListData, 'files/carList.json')

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

            optionsList = ["1 - Atualizar", "2 - Deletar", "3 - Voltar"]
            op1 = beaupy.select(optionsList, cursor='=>', cursor_style='blue', return_index=True)
            if op1 == 0: #Atualizar
                carUpdate(carSearch[op])
                print("\nCarro atualizado com sucesso!\n")
            elif op1 == 1: #Apagar
                carDelete(carSearch[op])
                print("\nCarro removido com sucesso!\n")
            else:
                return
        else:
            print("\nNão foram encontrados resultados com o critério definido!\n")  

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