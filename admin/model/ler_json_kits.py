import json


caminho_arquivo = 'admin/model/KitsSolares.json' 


with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


for kit in dados:
    print("ID do Kit:", kit['id'])
    print("IDs dos Itens:", kit['idItens'])
    print("Quantidade:", kit['quantidade'])
    print("Valor do Kit: R$", kit['valorKit'])
    print("-" * 30)# separador entre kits