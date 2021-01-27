from random import randint


class Jogador():
    def __init__(self, comportamento):
        self.jogando = True
        self.saldo = 300
        self.propriedades = []
        self.comportamento = comportamento
        self.posicao = 0

    def __str__(self):
        return self.comportamento

    def compra(self, propriedade):
        # O jogador só poderá comprar se tiver saldo e a propriedade não tiver proprietário
        if self.saldo >= propriedade.valor and propriedade.proprietario == None:
            self.saldo -= propriedade.valor
            propriedade.proprietario = self
            self.propriedades.append(propriedade)
        # Caso o jogador não possa comprar a propriedade, deve alugá-la
        else:
            self.aluga(propriedade)

    def aluga(self, propriedade):
        # O jogador não paga aluguel em suas propriedades
        if self.saldo >= propriedade.aluguel and propriedade not in self.propriedades:
            self.saldo -= propriedade.aluguel
            # Caso já exista um proprietário, este vai receber o valor do aluguel
            if propriedade.proprietario != None and propriedade.proprietario != self:
                propriedade.proprietario.recebe(propriedade.aluguel)
        elif self.saldo < propriedade.aluguel:
            # Caso o jogador não possua saldo para alugar a propriedade, perderá o jogo
            self.game_over()

    def recebe(self, valor):
        self.saldo += valor

    def game_over(self):
        self.jogando = False
        for propriedade in self.propriedades:
            propriedade.proprietario = None
        self.propriedades.clear()
        return False

    def rola_dado(self):
        resultado = randint(1, 6)
        # Tomei a liberdade de fazer esse método hard-coded. É uma excessão nesse projeto.
        # A cada volta no tabuleiro, o jogador recebe + 100 de saldo
        if(self.posicao + resultado > 19):
            novo_resultado = self.posicao - 20 + resultado
            self.posicao = novo_resultado
            self.saldo += 100
            return novo_resultado
        else:
            self.posicao += resultado
            return resultado
