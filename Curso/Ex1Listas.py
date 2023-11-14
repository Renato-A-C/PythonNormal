import random
lista1 = [2,5,9,1]
lista1[2]= 3
lista1.append(7)
lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)
for c, v in enumerate(lista1):
    print(f'na posicao {c} encontrei o valor {v}')
print("AINNNNN")
exit()