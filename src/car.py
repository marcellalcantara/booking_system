import beaupy
from src.fileStore import loadData, writeData
from src.validations import matricula, marca, cor, portas, validaPreco, validarCilindradas, validarPotencia

def carList():
    return loadData("files/carList.json")

def printCar(automovel):
    print(f"""
          |ID: {automovel['id']}| |Matrícula: {automovel['matricula']}| |Marca: {automovel['marca']}| |Modelo: {automovel['modelo']}| 
          |Cor: {automovel['cor']}| |Portas: {automovel['portas']}| |Cilindrada: {automovel['cilindrada']}cm3| |Potência: {automovel['cilindrada']}cv|
          |Preço diário: {automovel['precoDiario']:.2f}€|
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
    count = len(carList()) # Iniciando o id
    id = count + 1

    newCar = {}
    newCar['id'] = id
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
    
def searchCar():
    print("\nPesquisar Automóvel: \n")
    matrSearch = matricula()
    for automovel in carList():
        if automovel['matricula'] == matrSearch:
            printCar(automovel)
#            menu3(automovel)
            break
    else:
        print("Cliente não encontrado!")

def carMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Voltar"
        ]
        print("\nMenu dos automóveis:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='green', return_index=True)+1
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