import beaupy
from datetime import datetime
from src.fileStore import loadData, writeData

from src.client import clientList
from src.car import carList

def bookingList():
    return loadData("files/bookingList.json")

def bookingMenu():
    while True:
        lista = [
            "1 - Listar",
            "2 - Adicionar",
            "3 - Pesquisar",
            "4 - Sair"
        ]
        print("\nMenu das reservas:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='green', return_index=True)+1
        match op:
            case 1:
                for reserva in bookingList:
                    print(reserva)
            case 2:
                newBooking = {}
                newBooking['data_inicio'] = input("Data de início da reserva (AAAA-MM-DD): ")
                newBooking['data_fim'] = input("Data de fim da reserva (AAAA-MM-DD): ")
                newBooking['cliente_id'] = input("# Pegar JSON id cliente")
                newBooking['automovel_id'] = input("# Pegar JSON id automovel")
                newBooking['precoReserva'] = input(" Pegar JSON precoDiario")
                newBooking['numeroDias'] = input("formula dias") # pegar a data fim menos a data inicio e jogar o resultado

                list = bookingList()
                list.append(newBooking)
                writeData(list, 'files/bookingList.json')
                print("Reserva adicionada com sucesso!")
            case 3:
                searchBooking()
            case 4:
                print("Saindo...")
                break
            case _:
                print("\nErro: opção inválida!\n")



'''
c. Listagem de Bookings futuros no formato: 
Booking data início: XXXX | data fim: YYYYY (XXX dias) \n Cliente: Nome \n Automóvel: Marca 
– Matrícula \n Total: YYY €
d. Pesquisa por automóvel: critério matrícula. Deverá devolver os dados do automóvel bem como 
a listagem dos seus últimos 5 alugueres;
e. Pesquisa por cliente: critério nif. Deverá devolver os dados do cliente bem como a listagem dos 
seus últimos 5 alugueres;

def pesquisar():
    animalSearch = []
    listAnimals = loadTable("SELECT * FROM animal")
    nome = insertStringValue("Nome: ")
    print(f"\nPesquisa de animal com o nome {nome}:\n")
    for animal in listAnimals:
        if animal[1].lower() == nome.lower():
            animalSearch.append(animal)
    else:
        if animalSearch:
            animalSearchString = createAnimalMenu(animalSearch)
            op = beaupy.select(animalSearchString, cursor='->', cursor_style='red', return_index=True)
            #print(f"{animalSearch[op][0]} {animalSearchString[op]}")
            id = animalSearch[op][0]
            print("Animal selecionado:")
            printAnimal(animalSearch[op])
 
            listOptions = ["Atualizar", "Apagar", "Voltar"]
            opGes = beaupy.select(listOptions, cursor='->', cursor_style='red', return_index=True)
            if opGes == 0: # atualizar
                if updateAnimal(animalSearch[op]):
                    print("\nAnimal atualizado com sucesso!\n")
                else:
                    print("\nErro: Animal não foi atualizado!\n")
            elif opGes == 1: # apagar
                if deleteAnimal(id):
                    print("\nAnimal removido com sucesso!\n")
                else:
                    print("\nErro: Animal não foi removido!\n")
            else:
                return            

'''

def calcular_desconto(numero_dias):
    if numero_dias <= 4:
        return 0
    elif 5 <= numero_dias <= 8:
        return 0.15
    else:
        return 0.25
 
def listagemBookings():
    for booking in bookingList:
        inicio = datetime.strptime(booking['data_inicio'], '%Y-%m-%d')
        fim = datetime.strptime(booking['data_fim'], '%Y-%m-%d')
        total_dias = (fim - inicio).days
        cliente = [cliente for cliente in clientList() if cliente['id'] == booking['cliente_id']][0]
        automovel = [automovel for automovel in carList() if automovel['id'] == booking['automovel_id']][0]
        preco_total = booking['precoReserva'] * (1 - calcular_desconto(total_dias))
        print(f"Booking data início: {inicio} | data fim: {fim} ({total_dias} dias)\n"
              f"Cliente: {cliente['nome']}\n"
              f"Automóvel: {automovel['marca']} - {automovel['matricula']}\n"
              f"Total: {preco_total} €\n")

def searchBooking():
    print("\nPesquisar reserva: \n")