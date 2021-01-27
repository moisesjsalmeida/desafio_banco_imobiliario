from random import randint, shuffle

from jogador import Jogador
from tabuleiro import Propriedade, Tabuleiro

jogadores = [Jogador("impulsivo"), Jogador("exigente"),
             Jogador("cauteloso"), Jogador("aleatorio")]

propriedades = [
    Propriedade(40, 30, None),
    Propriedade(60, 50, None),
    Propriedade(55, 45, None),
    Propriedade(45, 35, None),
    Propriedade(50, 40, None),
    Propriedade(65, 55, None),
    Propriedade(45, 35, None),
    Propriedade(60, 50, None),
    Propriedade(40, 30, None),
    Propriedade(60, 50, None),
    Propriedade(65, 55, None),
    Propriedade(45, 35, None),
    Propriedade(40, 30, None),
    Propriedade(45, 35, None),
    Propriedade(65, 55, None),
    Propriedade(50, 40, None),
    Propriedade(45, 35, None),
    Propriedade(55, 45, None),
    Propriedade(65, 55, None),
    Propriedade(60, 50, None),
]


def jogada(jogador, tabuleiro):
    jogada = jogador.rola_dado()
    casa = tabuleiro.propriedades[jogada]

    # Jogada de acordo com o comportamento de cada jogador
    # impulsivo = compra todas as casas em que parar
    if jogador.comportamento == "impulsivo":
        jogador.compra(casa)

    # exigente = compra somente propriedades que tenham valor de aluguel acima de 50
    elif jogador.comportamento == "exigente":
        if casa.aluguel > 50:
            jogador.compra(casa)
        else:
            jogador.aluga(casa)

    # cauteloso = compra somente se o saldo após a compra for superior a 80
    elif jogador.comportamento == "cauteloso":
        if jogador.saldo - casa.valor >= 80:
            jogador.compra(casa)
        elif jogador.saldo - casa.valor < 80:
            jogador.aluga(casa)

    # aleatorio = 50% de chance de comprar, aleatoriamente
    elif jogador.comportamento == "aleatorio":
        chance = randint(1, 2)
        if chance == 1:
            jogador.compra(casa)
        elif chance == 2:
            jogador.aluga(casa)


def nova_partida():
    shuffle(jogadores)
    tabuleiro = Tabuleiro(propriedades, jogadores)

    rodadas = 0
    for i in range(1000):

        if len(tabuleiro.jogadores) == 1:
            break

        for j in tabuleiro.jogadores:

            if j.jogando == False:
                tabuleiro.remove_jogador(j)

            elif j.jogando == True:
                jogada(j, tabuleiro)

        rodadas += 1

    return tabuleiro.jogadores[0].comportamento, rodadas


# Executando as 300 simulações e extraindo os dados
def simula():
    resultados = [nova_partida() for i in range(300)]
    ganhadores = []
    rodadas = []

    for resultado in resultados:
        ganhadores.append(resultado[0])
        rodadas.append(resultado[1])

    timeouts = len(list(filter(lambda x: x == 1000, rodadas)))
    vitorias_impulsivo = ganhadores.count('impulsivo')
    vitorias_exigente = ganhadores.count('exigente')
    vitorias_cauteloso = ganhadores.count('cauteloso')
    vitorias_aleatorio = ganhadores.count('aleatorio')

    
    print("Timeouts: " + str(timeouts))

    print("Média de turnos das partidas: " +
          str(round(sum(rodadas)/len(rodadas))))

    print("Média de vitórias do jogador IMPULSIVO: " +
          str(round(vitorias_impulsivo/300 * 100, 2)) + "%")
    print("Média de vitórias do jogador EXIGENTE: " +
          str(round(vitorias_exigente/300 * 100, 2)) + "%")
    print("Média de vitórias do jogador CAUTELOSO: " +
          str(round(vitorias_cauteloso/300 * 100, 2)) + "%")
    print("Média de vitórias do jogador ALEATORIO: " +
          str(round(vitorias_aleatorio/300 * 100, 2)) + "%")

    print("Comportamento com mais vitórias: " + max(set(ganhadores), key = ganhadores.count) )


simula()
