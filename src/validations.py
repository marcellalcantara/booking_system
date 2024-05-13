import re
from datetime import datetime
from src.fileStore import loadData

def clientList():
    return loadData("files/clientList.json")

def carList():
    return loadData("files/carList.json")

def bookingList():
    return loadData("files/bookingList.json")

# Definir funções de Validação Cliente

def validarNome():
    while True:
        nomeInput = input("Nome: ").strip()
        if nomeInput:
            nome = ' '.join([parte.capitalize() for parte in nomeInput.split()])
            return nome
        else: 
            print("Nome inválido. Por favor, insira um nome válido.")

def validarNif():
    while True:
        nif = input("NIF: ")
        if len(nif) == 9 and nif.isdigit():
            if any(cliente['NIF'] == nif for cliente in clientList()):
                print("Este NIF já está registrado. Por favor, insira um NIF diferente.")
                continue
            return nif
        else:
            print("O NIF é inválido. Certifique-se de que contém exatamente 9 dígitos.")

def validarNifUpdate():
    while True:
        nif = input("NIF: ")
        if len(nif) == 9 and nif.isdigit():
            return nif
        else:
            print("O NIF é inválido. Certifique-se de que contém exatamente 9 dígitos.")

def validarDataNascimento():
    while True:
        dataInput = input("Data de nascimento (dd/mm/aaaa): ")
        try:
            dataNascimento = datetime.strptime(dataInput, "%d/%m/%Y")   #Verificar input listagem
            return dataNascimento
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato dd/mm/aaaa.")

def validarTelefone():
    while True:
        telefone = input("Telefone(somente números): ")
        if len(telefone) == 9 and telefone.isdigit():
            if any(cliente['telefone'] == telefone for cliente in clientList()):
                print("Este número de telefone já está registrado. Por favor, insira um número diferente.")
                continue
            return telefone
        else:
            print("O telefone é inválido. Certifique-se de que contém exatamente 9 dígitos.")

def validarEmail():
     while True:
        email = input("E-mail: ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            if any(cliente['email'] == email for cliente in clientList()):
                print("Este e-mail já está registrado. Por favor, insira um e-mail diferente.")
                continue
            return email
        else:
            print("O e-mail é invalido! Insira novamente")

# Definir funções de Validação veiculo

def matricula():
    while True:
        matriculaInput = input("Matrícula(sem traços): ")
        if len(matriculaInput) == 6:
            matricula = '-'.join([matriculaInput[:2], matriculaInput[2:4], matriculaInput[4:]])
            if any(automovel['matricula'] == matricula for automovel in carList()):
                print("Esta matrícula já está registrada. Por favor, insira uma matrícula diferente.")
                continue
            return matricula
        else:
            print ("Matrícula inserida inválida. Deve conter 6 caracteres")

def matriculaUpdate():
    while True:
        matriculaInput = input("Matricula(sem traços):")
        if len(matriculaInput) != 6:
            print ("Matricula inserida inválida. Deve conter 6 caracteres")
        else:
            matricula = '-'.join([matriculaInput[:2], matriculaInput[2:4], matriculaInput[4:]])
            return matricula
         
def validaLetra(letter):
    while True:
        valor = input(letter)
        if valor.replace(" ", "").isalpha():
            return valor
        else: 
            print("Entrada inválida. Insira uma entrada válida.")

def marca():
    return validaLetra("Marca: ")

def cor():
    return validaLetra("Cor: ")
    

def portas(): 
    while True:
        porta = input("Quantidade de portas(3 ou 5): ")
        pattern = r'^[3|5]$'
        if re.match(pattern, porta):
            return porta
        else:
            print("Números de portas inválidos. Nossos carros estão disponíveis em 3 ou 5 portas.")
          
def validaPreco():
        while True:
            numero = input("Valor diário(€): ")
            try:
                numeroFloat = float(numero)
                return numeroFloat
            except ValueError:
                print("Por favor, insira um número float válido.")

def validarCilindradas():
    while True:
        cilindradas = input(f"Cilindradas(cm3): ")
        try:
            cilFloat = float(cilindradas)
            return cilFloat
        except ValueError:
            print("Cilindradas Inválida. Digite apenas números")   

def validarPotencia():
    potencia = input(f"Potência: ")
    if potencia.isdigit():
        return potencia
    else:
        print("Potência Inválida. Digite apenas números")
    return  potencia

#Definir funções de validação booking

def inicio():
    while True:
        inicioInput = input("Início (dd/mm/aaaa): ")
        try:
            inicio = datetime.strptime(inicioInput, "%d/%m/%Y")
            hoje = datetime.now()
            if inicio.date() < hoje.date():
                print("Data inválida. Por favor, insira uma data a partir de hoje.")
            else:
                return inicio
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato dd/mm/aaaa.")

def fim(inicio):
    while True:
        fimInput = input("Fim (dd/mm/aaaa): ")
        try:
            fim = datetime.strptime(fimInput, "%d/%m/%Y")

            if fim <= inicio:
                print("Data inválida. A data de término deve ser pelo menos um dia após a data de início.")
            else: 
                return fim
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato dd/mm/aaaa.")        


def totalDias(fim, inicio):
    dias = (inicio - fim).days 
    return dias

def calcularDesconto(dias):
    if dias <= 4:
        return 0
    elif 5 <= dias <= 8:
        return 0.15
    else:
        return 0.25

def importIdCar():
    while True:
        matriculaInput = input("Matrícula(sem traços): ")
        if len(matriculaInput) == 6:
            matricula = '-'.join([matriculaInput[:2], matriculaInput[2:4], matriculaInput[4:]])
            for car in carList():
                if car['matricula'] == matricula:
                    return (car['id'], car['marca'], car['modelo'], car['precoDiario'], car['matricula'])
            print("Matrícula não encontrada. Tente novamente.")
        else:
            print("Formato de matrícula inválido. Deve ter 6 caracteres.")

def importIdClient():
    while True:
        nifInput = input("NIF do cliente: ")
        if len(nifInput) == 9 and nifInput.isdigit():
            for cliente in clientList():
                if cliente['NIF'] == nifInput:
                    return (cliente['id'], cliente['nome'], cliente['NIF'])
            print("Cliente não encontrado. Tente novamente.")
        else:
            print("Formato do NIF é inválido.Digite novamente.")

def valorTotal(precoDiario, dias, calcularDesconto):  
    valorTotal = precoDiario * dias * (1 - calcularDesconto)
    return valorTotal

def integerNumber():
    bookingId = input(f"ID da reserva: ")
    if bookingId.isdigit():
        return bookingId
    else:
        print("Reserva Inválida. Digite apenas números")
    return bookingId
