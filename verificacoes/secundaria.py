class Seconde:
    def __init__(self, nome:str, idade:float, salario: float):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    def _mostrarStatus(self):
        print(f"{self.nome} , {self.idade}, {self.salario}\n")
    def _pegaridade(self):
        return self.idade
    def _pegarNome(self):
        return self.nome
    def _pegarSalario(self):
        return self.salario
