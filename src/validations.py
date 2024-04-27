from datetime import datetime
import re

# Definir funções de Validação Cliente
def validarNome():
    while True:
        nome = input("Nome: ")
        if nome.replace(" ", "").isalpha():
            return nome
        else: 
            print("Nome inválido. Por favor, insira um nome válido.")

def validarNif():
    while True:
        nif = input("NIF: ")
        if len(nif) == 9 and nif.isdigit():
            return nif
        else:
            print("O NIF é inválido. Certifique-se de que contém exatamente 9 dígitos.")

def validarDataNascimento():
    while True:
        data_input = input("Data de nascimento (dd/mm/aaaa): ")
        try:
            data_nascimento = datetime.strptime(data_input, "%d/%m/%Y")   #Verificar input listagem
            return data_nascimento
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato dd/mm/aaaa.")

def validarTelefone():
    while True:
        telefone = input("Telefone(somente números): ")
        if len(telefone) == 9 and telefone.isdigit():
            return telefone
        else:
            print("O telefone é inválido. Certifique-se de que contém exatamente 9 dígitos.")

def validarEmail():
     while True:
        email = input("E-mail: ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            print("O e-mail é invalido! Insira novamente")

# Definir funções de Validação veiculo
def matricula():
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
        pattern = r'^[3]$' and r'^[5]$'
        if re.match(pattern, porta):
            return porta
        else:
            print("Números de portas inválidos. Nossos carros estão disponíveis em 3 ou 5 portas.")
          
def validaPreco():
        while True:
            numero = input("Valor diário: ")
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
        return potencia + "cv"
    else:
        print("Potência Inválida. Digite apenas números")
    return  potencia
    