curvilinea=0
class Racetrax:
    def __init__(self,nome,km,curvas):
        self.nome=nome
        self.km= float(km)
        self.curvas= int(curvas)
    def mostrardados(self):
        print(f'GP de: {self.nome}')
        print(f'Percurso: {self.km}km')
        print(f'Número de Curvas: {self.curvas}')
    def mostrarcurvas(self):
        global curvilinea
        curvilinea = self.curvas
        return curvilinea

gpbr= Racetrax('interlagos','4.3','15')
gpjp= Racetrax('suzuka','5.8','18')
gpita= Racetrax('imola','4.9','19')
gpmon= Racetrax('monaco','3.3','20')

gpjp.mostrarcurvas()


