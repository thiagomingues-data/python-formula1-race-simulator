from f1racetrax import*
from random import randint

class F1cars:
    def __init__(self, nome, cor, numero, statusdriver, statuscar):
        self.nome=nome
        self.cor=cor
        self.numero = numero
        self.statusdriver = statusdriver
        self.statuscar = statuscar
        self.nota = None
    def correr(self):
        curvas=curvilinea
        print(self.nome,end=' ► ')
        print(f'car nº {self.numero}', end=' ► ')
        print(self.cor)
        if curvas > 18 and self.statusdriver == 'excelente':
            self.statusdriver = 'bom'
        elif curvas > 18 and self.statusdriver == 'bom':
            self.statusdriver = 'regular'

        else:
            print('Ótima performance do motor')
        b = randint(1, 10)  # tempo no box
        if b == 1 and self.statusdriver == 'excelente':
            self.statusdriver = 'bom'
        elif b == 1 and self.statusdriver == 'bom':
            self.statusdriver = 'regular'

        if b == 1:
            print('\033[0;31mPerdeu muito tempo no box\033[m')
        else:
            print('Ótima performance no box')

        # Verificando a combinação dos status para atribuição da nota
        print(f"Status do motorista: {self.statusdriver}")
        print(f"Status do carro: {self.statuscar}")

        # criando a nota da corrida
        if self.statusdriver == 'excelente' and self.statuscar == 'excelente':
            self.nota = 'nivel SENNA!!'
        elif self.statusdriver == 'excelente' and self.statuscar == 'bom':
            self.nota = 'A'
        elif self.statusdriver == 'bom' and self.statuscar == 'excelente':
            self.nota = 'A'
        elif self.statusdriver == 'bom' and self.statuscar == 'bom':
            self.nota = 'B'
        elif self.statusdriver == 'regular' and self.statuscar == 'bom':
            self.nota = 'C'
        elif self.statusdriver == 'bom' and self.statuscar == 'regular':
            self.nota = 'C'
        elif self.statusdriver == 'regular' and self.statuscar == 'regular':
            self.nota = 'D'
        else:
            self.nota = 'B'
        c = randint(1, 10)  # carro quebrou
        if c == 1:
            print('\033[0;31mCarro quebrou\033[m')
            self.nota = 'E'
        print(f'Avaliação de performance na corrida: {self.nota}')
        if self.nota == 'nivel SENNA!!':
            print('')
        print('\033[0;36m' + '~' * 39+'\033[m')
    def pontos(self):
        if self.nota == 'nivel SENNA!!':
            return 50
        elif self.nota == 'A':
            return 40
        elif self.nota == 'B':
            return 30
        elif self.nota == 'C':
            return 20
        elif self.nota == 'D':
            return 10
        elif self.nota == 'E':
            return 0
carredb= F1cars('redbull','azul','1','excelente','bom')
carferrari= F1cars('ferrari','vermelho','16','bom','bom')
carmclaren= F1cars('mclaren','laranja','81','bom','excelente')
carmercedes= F1cars('mercedes','prata','63','bom','regular')
carastonm= F1cars('astonmartin','verde','14','excelente','regular')

carros = [carredb, carferrari, carmclaren, carmercedes, carastonm]
