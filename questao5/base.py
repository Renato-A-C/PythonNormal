from secundaria import Seconde
import secundaria
import time
print("cadastro de pessoas....")
cont=0 ; reg = "1" ; pessoa=[]
a=0;b=0;o=0;ab=0
while reg != "sair":
    idade = int((input("digite a idade da pessoa: ")))
    if idade <18 and idade >67:
        print("idade inconpativel, deve ser entre 18 e 67")
        continue
    TipoSangue = input("digite o tipo de sangue: ")
    if TipoSangue =="a" or "A":
        a+=1
    elif TipoSangue =="b" or "B":
        b+=1
    elif TipoSangue =="o" or "O":
        o+=1
    elif TipoSangue =="ab" or "AB":
        ab+=1
    else:
        print("os tipos devem ser A, B, O  e AB,")
        continue
    arroz = Seconde(sangue= TipoSangue, idade = idade)
    pessoa.append(cont)
    pessoa[cont]=arroz
    reg = input("digite 'sair' pra sair, ou qualquer outra coisa pra continuar a registrar: ")
    if reg =="sair":
        consult= input("veja quantas pessoas precisam do seu sangue(a/b/o/ab) :")
        if TipoSangue =="a" or "A":
            print("{} pessoas do tipo a".format(a))
        if TipoSangue =="b" or "B":
            print("{} pessoas do tipo b".format(b))
        if TipoSangue =="o" or "O":
            print("{} pessoas do tipo o".format(o))
        if TipoSangue =="ab" or "AB":
            print("{} pessoas do tipo AB".format(ab))