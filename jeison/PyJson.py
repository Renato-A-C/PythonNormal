import json

"""
Listas são como arrays em Javascript
Mutável e dinâmica, heterogênea e indexada
"""
#lista = ["Jamilton", "Pedro", "Ana", "João", "Maria"]
#print(type(lista))
#print( dir(lista) )
#print( lista[0] )
#print( lista[-1] )
#print( lista[0:2] )
#print( lista[2:5] )
#print( lista[::2] )

lista = ["Jamilton", "Pedro", "Ana", "João", "Maria"]

lista[3] = "Alterado"
lista.append("Novo")
#lista.remove("Pedro")
#del lista[1]
#print( lista[0:2] )
#del lista[0:2]
#print( len(lista) )
#print(lista.count("Jamilton"))
#print( lista.index("Pedro") )
#lista.clear()
#lista.reverse()
#lista.sort()

#print( "Jamilton" in lista )
# print("Marcio" not in lista)

# print(f"quero ver o espaço {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]},  da lista")
"""
valor = 1
print(type(valor))
valor = "a"
print(type(valor))
valor = 1.2
print(type(valor))
valor = True 
print(type(valor))
valor = 4
"""
altura = float(input('digite sua altura '))
peso = float(input('digite seu peso '))
imc =  peso/ (altura**2) 
imc = round(imc,2)

print(f"o imc é {imc} , a altura é {altura} e o peso é {peso}")    

if imc >=0 and imc< 18.5:
    print("O cara é mais magro que um palito de dente")
elif imc >=18.5 and imc< 25:
    print("na media")
elif imc >=25 and imc < 30:
    print("pesado")
elif imc >=30:
    print("thaisplodindo")
else:
    print("ta errado")
    
    
"""
tupla = ()
lista = []
dicionario = {
    'nome1': "jamilto",
    'nome2': "xedo",
    'nome3': "chopp",
}
print(f"Quero ver o espaço {dicionario['nome1']}{dicionario['nome2']}")
"""
