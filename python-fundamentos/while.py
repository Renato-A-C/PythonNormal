""""
while(condicao):
    executa enquanto a condição é verdadeira
"""
# contador = 1
# while contador <= 4:
#     print(f"executou {contador}")
#     contador += 1

postagens = [
    "Hoje passeado pela avenida paulista",#0
    "Fazendo trilha na pedra do Gavião",#1
    "Hoje fiz um curso de criação de Sistemas",#2
    "Na casa da mãe, almoçando todos juntos",#3
]
totalPostagens = len(postagens)# 4

contador = 0
while contador < totalPostagens:
    print(f'{contador} - {postagens[contador]}')
    contador += 1
    if contador == 1:
        continue
    print("+++++++")

    # if contador == 1:
    #     break
    # if contador != totalPostagens:
    #     print("+++++++")
print("fim")