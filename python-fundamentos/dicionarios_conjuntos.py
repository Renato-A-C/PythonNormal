"""
Lista e Tuplas: indexadas
lista = ["Jamilton", "Ana"]
lista: 0->"Jamilton", 1-> "Ana"
"""
# dicionario = {
#     'correr': 'Deslocar-se ou mover-se rapidamente',
#     'ligar': 'Estabelecer uma comunicação',
# }
# print(dicionario['ligar'])

carro = {
    'modelo': 'Fusca',
    'marca': 'volkswagem',
    'ano': 1970,
    'donos': ['Marcos', 'Maria']
}

#print(type(carro))
#print(dir(carro))
#print(carro['modelo'])
#carro['donos'].append("Pedro")
#print(carro['donos'][0])
#carro['km'] = 8500
#carro['ano'] = 1980
#carro.update({'ano': 1980, 'km': 8500})
#del carro['ano']
# valor = carro.pop('ano')
# print(valor)
#print(carro.keys())
#print(carro.values())
#print(carro.items())
#print(carro.get('ano', 'padrao'))
#print(len(carro))
# carro.clear()
# print(carro)

"""
set -> Conjunto
"""
#lista = ["Jamilton", "José", "Ana", "Ana"]
itens = {"Jamilton", "José", "Ana"}
#print(type(itens))
#print(itens)

carros = {"fusca", "gol", "fiat 147"}
#carros2 = {"BMW", "fusca", "passat"}
#novo = carros.union(carros2)
#novo = carros.intersection(carros2)
#carros.add("BMW")
#carros.remove("fusca")
print(carros)
