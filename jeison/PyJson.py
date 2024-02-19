import json


with open('pythonNormal\jeison\Json.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    
    print(dados)
for i in dados:
    print(f"{i['nome']}, tem {i['idade']} anos de idade")
    
