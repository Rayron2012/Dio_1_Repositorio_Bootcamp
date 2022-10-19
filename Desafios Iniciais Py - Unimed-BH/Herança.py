class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('Ligando o motor')
    
class Motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor,placa, numero_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta('Branca', 'xyx-1234', 2)
moto.ligar_motor()

carro = carro('Preto', 'abc-1234', 4)
carro.ligar_motor()


caminhao = caminhao('Azul', 'asc-7598', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()