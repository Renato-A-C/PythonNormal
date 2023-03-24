from apoio import Seconde
import apoio
import time
print("cadastro de pessoas....")
cont=0 ; reg =0 ; pessoa=[]
while reg >=0:
    salario = float(input("digite o salário da pessoa: "))
    idade = int(input("conte a idade da pessoa: "))
    sexo = input("fale o gênero BIOLÓGICO (e não algo declarado como helicróptro cromado e blindado) da pessoa: ")
    arroz = Seconde(salario = salario, idade = idade, sexo= sexo)
    pessoa.append(cont)
    pessoa[cont]=arroz
    reg = float(input("escreva qualquer numero positivo para continuar, para, bem, continuar a registrar, negativo sai do programa: "))
    cont +=1
total = cont 
cont=0 
idad=0 
salariosM=0.0
sexo = ""
i=0
fems=0
Maidad=0
Menidad=0
MenSalario=0.0
for i in range(total):
    idad= pessoa[cont]._pegaridade()
    if Maidad == 0 and Menidad ==0:
        Maidad = idad
        Menidad = idad

    if Maidad <idad:
        Maidad=idad
    if Menidad > idad:
        Menidad=idad
    salarios= float(pessoa[cont]._pegarSalario())
    if MenSalario==0:
        MenSalario=salarios
    if MenSalario >salarios:
        MenSalario=salarios
    salariosM+=salarios
    cont+=1
print(MenSalario)
salariosM= salariosM/total
i=0 
cont=0
for i in range(total):
    if pessoa[cont]._pegarSalario()==MenSalario:
        print("a pessoa com o menor salario do grupo é a pessoa {}, com um salario de {} reais e é do sexo {}, tem idade {}".format(cont+1,salario,pessoa[cont]._pegarSexo(),idad))
    if pessoa[cont]._pegarSexo() == "feminino":
        fems+=1
    cont+=1
print("{} pessoas\nmaior idade: {}\nmenor idade: {}\n{} do sexo feminino\nsalário médio: {}".format(total,Maidad,Menidad,fems,salariosM))