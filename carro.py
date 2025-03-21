class Carro:
    def __init__(self, marca, modelo, ano, cor, combustivel, ligado, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 100
        self.ligado = True
        self.velocidade = 0

    def __str__(self):
        return f"marca:  {self.marca}, modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}, ligado: {self.ligado}, velocidade: {self.velocidade}"
    
    def ligar(self):
           if self.ligado is True:
               print("O Carro está ligado!")
    
    def desligar(self):
         if self.ligado is False:
              print("O Carro está desligado")
    
    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 10
            self.combustivel -= 5
            print(f"Acelerando... Velocidade: {self.velocidade} km/h. Combustível: {self.combustivel}%")
        elif self.combustivel <= 0:
            print("Não há COMBUSTÍVEL suficiente para ACELERAR!.")
        elif not self.ligado:
            print("O Carro está DESLIGADO. Ligue o Carro para ACELERAR!!!.")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
            print(f"Freiando... Velocidade: {self.velocidade} km/h.")
        else:
            self.velocidade = 0
            print(f"Carro parado. Velocidade: {self.velocidade} km/h.")

    def abastecer(self):
        self.combustivel = 100
        print(f"O {self.modelo} foi Abastecido. Combustível atual: {self.combustivel}.")

    def buzinar(self):
        print("BEEP! BEEP!")

    def status(self):
        status_ligado = "Ligado" if self.ligado else "Desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Combustível: {self.combustivel}%, Velocidade: {self.velocidade} km/h, Status: {status_ligado}")


carro1 = Carro("Volkswagen", "Virtus", "2018", "Brinco", 100, True, 100)
carro2 = Carro("Chevrolet", "Onix", "2015", "Preto", 60, False, 0)


carro1.status()
carro1.ligar()
carro1.acelerar()
carro1.abastecer()
carro1.acelerar()
carro1.frear()
carro1.buzinar()
carro1.desligar()


