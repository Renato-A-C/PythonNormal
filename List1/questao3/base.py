from apoio import Seconde
import apoio
import time
print("cadastro de pessoas....")
cont=0 ; reg = "1" ; pessoa=[]
while reg == ("1"or"continuar"):
    nome = input("digite o nome da pessoa: ")
    idade = int(input("digite a idade da pessoa: "))
    sexo = input("digite o gênero BIOLÓGICO (e não algo declarado como helicróptro cromado e blindado) da pessoa: ")
    arroz = Seconde(nome = nome, idade = idade, sexo= sexo)
    pessoa.append(cont)
    pessoa[cont]=arroz
    reg = input("digite 1 ou continuar, para, bem, continuar a registrar: ")
    cont +=1
total = cont 
cont=0 
idad=0 
nomes= "" 
sexo = ""
print(total)
cont=0 
i=0
MaTot=0
MenTot=0
FmenTot=0
for i in range(total):
    if pessoa[cont]._pegaridade() >=18 and (pessoa[cont]._pegarSexo()== "masculino"):
        nomes = pessoa[cont]._pegarNome()
        sexo = "MASCULINO"
        MaTot+=1
        print("A pessoa {} é de maior, e é do gênero {}".format(nomes,sexo))
    if pessoa[cont]._pegaridade() <18:
        MenTot+=1
    if pessoa[cont]._pegaridade() <18 and (pessoa[cont]._pegarSexo()== "feminino"):
        nomes = pessoa[cont]._pegarNome()
        sexo = "FEMININO"
        FmenTot+=1
        print("A pessoa {} é de menor, e é do gênero  {}".format(nomes,sexo))
    cont+=1
print(f"no total, temos {FmenTot} pessoas do sexo feminino menores de idade.\nTambém {MaTot} do sexo masculino maiores de idade\n{MenTot} pessoas menores de idade")