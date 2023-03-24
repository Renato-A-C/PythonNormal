class Seconde:
    def __init__(self, salario:float, idade:float, sexo: str,):
        self.salario = salario
        self.idade = idade
        self.sexo = sexo
    def _mostrarStatus(self):
        print(f"{self.salario} , {self.idade}, {self.sexo}\n")
    def _colocarIdade(self, idad):
        idad = input("coloca algo ae ")
        self.idade = idad
    def _pegaridade(self):
        return self.idade
    def _pegarSalario(self):
        return self.salario
    def _pegarSexo(self):
        return self.sexo
    