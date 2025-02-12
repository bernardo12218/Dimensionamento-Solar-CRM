import json


caminho_arquivo = 'admin/model/Itens.json'  


with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


for item in dados:
    print("ID do Item:", item['id'])
    print("ID do Produto:", item['id_Produto'])
    print("ID do Kit Solar:", item['id_KitSolar'])
    print("Quantidade:", item['quantidade'])
    print("-" * 30)  # separador entre itens