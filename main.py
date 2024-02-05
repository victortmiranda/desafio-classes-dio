class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            self.ataque = 'magia'
        elif self.tipo == "guerreiro":
            self.ataque = 'espada'
        elif self.tipo == "monge":
            self.ataque = 'artes marciais'         
        elif self.tipo == "ninja":
            self.ataque = 'shuriken'        
        else: 
            self.ataque = 'soco'

        print(f"O {self.tipo} atacou usando {self.ataque}")

#teste 
heroiTeste = Heroi('Victor Miranda', 31, 'mago')
heroiTeste.atacar()