import random
import time
print("gerador de senhas")
numtotalga= int(input("digite o número total de algarismos desejados:"))
listaSenha = []
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cont=0
for cont in range(numtotalga):
    listaSenha.append(cont)
    pergunte = int(input("Qual otipo de algarismo desejado?  \n 1 para letras maiusculas \n 2 para minusculas \n 3 para numeros \n 4 para especiais: "))
    if pergunte == 2:
        num1 = random.choice(alfabeto)
        listaSenha[cont]=num1
        cont+=1
    if pergunte == 3:
        num1= random.randint(0, 9)
        listaSenha[cont] = num1
        cont =+1
        
        print(listaSenha)
cont=0
senhaMesmo =""
for cont in range(numtotalga):
    senhaMesmo += str(listaSenha[cont])
    
print(senhaMesmo)