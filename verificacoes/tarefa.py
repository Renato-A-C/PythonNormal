from secundaria import Seconde
import secundaria
import time
print("cadastro de funcionario....")
cont=0 ; reg = "1" ; funcs=[]
while reg == ("1"or"continuar"):
    nome = input("digite o nome do funcionario: ")
    idade = int(input("digite a idade do funcionario: "))
    salario = float(input("digite o salario do funcionario: "))
    arroz = Seconde(nome = nome, idade = idade, salario= salario)
    funcs.append(cont)
    funcs[cont]=arroz
    reg = input("digite 1 ou continuar, para, bem, continuar a registrar: ")
    cont +=1
total = cont ; cont=0 ; idad=0 ; velho = idad ; novo=idad ; nomes= "" ; salario = 0.0
print(total)
for i in range(total):
    idad=funcs[cont]._pegaridade()
    if novo == 0:
        novo=idad
    if velho < idad:
        velho=idad
    if idad < novo:
        novo = idad  
    print("{} {}".format(novo,velho))      
    #print("o mais novo é {}\n o mais velho é {}".format(novo,velho))
    cont+=1
cont=0 ;i=0
for i in range(total):
    if funcs[cont]._pegaridade() ==novo:
        nomes = funcs[cont]._pegarNome()
        salario = funcs[cont]._pegarSalario()
        print("o mais novo é {}, seu salário é {}".format(nomes,salario))
    if funcs[cont]._pegaridade() ==velho:
        nomes = funcs[cont]._pegarNome()
        salario = funcs[cont]._pegarSalario()
        print("o mais velho é {}, seu salário é {}".format(nomes,salario)) 
    cont+=1
    