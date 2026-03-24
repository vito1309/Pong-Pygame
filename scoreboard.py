from settings import PONTOS_PARA_VENCER


class Placar:
    def __init__(self):
        self.pontos_j1 = 0
        self.pontos_j2 = 0

    def ponto_jogador1(self):
        self.pontos_j1 += 1

    def ponto_jogador2(self):
        self.pontos_j2 += 1

    def vencedor(self):
        if self.pontos_j1 >= PONTOS_PARA_VENCER:
            return "Jogador 1"
        if self.pontos_j2 >= PONTOS_PARA_VENCER:
            return "Jogador 2"
        return None

    def resetar(self):
        self.pontos_j1 = 0
        self.pontos_j2 = 0
