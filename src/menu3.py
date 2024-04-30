import beaupy
from src.fileStore import loadData, writeData
import src.client
import src.car
import src.booking

def menu3():
    while True:
        lista = [
            "1 - Atualizar",
            "2 - Deletar",
            "3 - Voltar"
        ]
        print("\nMenu dos automóveis:\n")  
        op = beaupy.select(lista, cursor='=>', cursor_style='green', return_index=True)+1
        match op:
            case 1:
                update()
            case 2:
                delete()
            case 3:
                print("Voltando...")
                break

def update():
    pass

def delete():
    pass