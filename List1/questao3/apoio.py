class Seconde:
    def __init__(self, nome:str, idade:float, sexo: str):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def _mostrarStatus(self):
        print(f"{self.nome} , {self.idade}, {self.sexo}\n")
    def _pegaridade(self):
        return self.idade
    def _pegarNome(self):
        return self.nome
    def _pegarSexo(self):
        return self.sexo
    