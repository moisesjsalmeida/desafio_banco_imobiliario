class Propriedade:
    def __init__(self, valor, aluguel, proprietario):
        self.valor = valor
        self.aluguel = aluguel
        self.proprietario = proprietario


class Tabuleiro:
    def __init__(self, propriedades, jogadores):
        self.propriedades = propriedades
        self.jogadores = jogadores

    def remove_jogador(self, jogador):
        self.jogadores.remove(jogador)
