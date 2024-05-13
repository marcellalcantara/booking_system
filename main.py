#Marcella Pereira 
#Romulo Sousa
#Thais Almeida

import beaupy

from src.client import clientMenu
from src.car import carMenu
from src.booking import bookingMenu

# Menu principal
def menu():
    while True:
        lista = [
            "1 - Clientes",
            "2 - Automóveis",
            "3 - Reservas",
            "4 - Sair"
        ]
        print("\nVocê está no rent-a-car Fundão, o que deseja gerenciar?\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='blue', return_index=True)+1
        match op:
            case 1:
                clientMenu()
            case 2:
                carMenu()
            case 3:
                bookingMenu()
            case 4:
                print("Saindo...")
                break
            case _:
                print("\nErro: opção inválida!\n")

# Inicialização do programa
menu() 