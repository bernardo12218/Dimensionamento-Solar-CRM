import json

caminho_arquivo = 'admin/model/Produtos.json'


with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# dados como dict
for produto in dados:
    print("ID:", produto['id'])
    print("Tipo:", produto['tipo'])
    print("Valor:", produto['valor'])
    print("Estoque:", produto['estoque'])
    print("Marca:", produto['marca'])
    print("Potência:", produto['potencia'])
    print("-" * 30)  