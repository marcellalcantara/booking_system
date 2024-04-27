import json

# Carregar dados dos arquivos JSON
def loadData(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except:
        return []
    else:
        return data

 
# Salvar dados nos arquivos JSON
def writeData(lista, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(lista, f, indent=4, default=str)
    except Exception as e:
        print("\nErro: Não foi possível gravar o ficheiro !\n")
        print(e)
    else:
        print("\nSucesso: o ficheiro foi escrito com sucesso!\n")