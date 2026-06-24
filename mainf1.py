from time import sleep
from f1cars import*
from f1racetrax import*
import pygame
for c in range (5,0,-1):
    sleep(0.8)
    print(f'\033[0;31m {c}',end='... \033[m')
sleep(0.8)
print(f'\033[0;33mGOOOOO!!! \033[m')
sleep(0.3)
pygame.init()
pygame.mixer.music.load('f1audio.mp3')  # Ajuste o caminho se necessário
pygame.mixer.music.play()
sleep(3.5)
print('\n\033[0;36m' + '~' * 39+'\033[m')
print('\033[0;36mBem Vindo a FORMULA 1\033[m'.center(49))
print('\033[0;36m' + '~' * 39+'\033[m')
print()
sleep(2)

while True:
    track = input(
        "Digite o país da prova exatamente como no exemplo e sem acentuação:\n"
        "\nbrasil\n"
        "japao\n"
        "monaco\n"
        "italia\n"
        "\nSua escolha: "
    ).lower()
    print()
    if track == "brasil":
        gpbr.mostrardados()
        gpbr.mostrarcurvas()
        break
    elif track == "japao":
        gpjp.mostrardados()
        gpjp.mostrarcurvas()
        break
    elif track == "monaco":
        gpmon.mostrardados()
        gpmon.mostrarcurvas()
        break
    elif track == "italia":
        gpita.mostrardados()
        gpita.mostrarcurvas()
        break
    else:
        print("Local de prova inválido.")
        print()
sleep(3)

print()

print('Atenção! Circuitos com muitas curvas podem reduzir o desempenho do piloto.')
print('Cuidado para não demorar demais no box e manter o carro com bom desempenho!')
print('\033[0;36m' + '~' * 76+'\033[m')
sleep(6)
print()
carredb.correr()
sleep(2)
carmclaren.correr()
sleep(2)
carferrari.correr()
sleep(2)
carmercedes.correr()
sleep(2)
carastonm.correr()
sleep(2)
ordem_chegada = sorted(carros, key=lambda c: (c.pontos(), c.statusdriver == 'excelente'), reverse=True)
print()
print("\033[1;36m== ORDEM DE CHEGADA ==\033[m")
print()
for posicao, carro in enumerate(ordem_chegada, start=1):
    print(f"{posicao}º lugar: {carro.nome}")
