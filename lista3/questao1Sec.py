class base:
    def __init__(self, val1 : str , val2:int, setor: int, ):
        self.val1= val1
        self.val2 = val2
        self.setor = setor
        
    def mostrarStats(self):
        print(f' val1= idade {self.val1} \n val2 = escolaridade {self.val2} \n setor = {self.setor}')
    def consultarIdade(self):
        return self.val1
    def consultarEscolaridade(self):
        return self.val2
    def consultarSetor(self):
        return self.setor
    def perguntarEscolaridade(self):
        esco = int(input("digite sua escolaridade, fazendo o favor \n só pode valor inteiro \n 1 para fundamental\n 2 para ensino medio\n 3 para superior"))
        while esco!= None:
            if esco == 1 :
                self.val1 = "fundamental"
            elif esco == 2 :
                self.val1 = "médio"
            elif esco == 3 :
                self.val1 = "superior"
            else:
                print("invalidado")
        return self.val1
    def perguntarIdade(self):
        texto = "digite sua idade\n só pode inteiros"
        print(texto)
        idad = int(input())
        while idad!= None:
            if idad !=0 :
                self.val2 = idad
            else:
                print("invalidado, faz de novo :)")
        return self.val2    
    def perguntarSetor(self):
        setor = int(input("digite qual seu setor, fazendo o favor \n só pode valor inteiro \n 1 para A\n 2 para B\n 3 para C"))
        while setor!= None:
            if setor == 1 :
                self.setor = "setorA"
            elif esco == 2 :
                self.setor = "setorB"
            elif esco == 3 :
                self.setor = "setorC"
            else:
                print("invalidado")
        return self.setor
    