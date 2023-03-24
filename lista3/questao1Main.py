# temo que perguntar o setor de morada
# temo q perguntar idade
# temo q perguntar nível de escolaridade 
import questao1Sec
from questao1Sec import base
cadast = []
reg = "1"
cont=0 
while reg!= "sair":
    arroz = base(val1=0, val2="", setor="")
    cadast.append(cont)
    cadast[cont] = arroz
    idade = arroz.perguntarIdade()
    arroz(val1 = idade)
    if idade >18:
        maiorIdad +=1
    reg = input("digite sair pra sair, senao qualquer coisa ai continua")
    
    
    

