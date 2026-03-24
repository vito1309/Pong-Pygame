import pygame
from settings import ALTURA, RAQUETE_LARGURA, RAQUETE_ALTURA, RAQUETE_VELOCIDADE, BRANCO


class Raquete:
    def __init__(self, x):
        self.x = x
        self.y = ALTURA // 2 - RAQUETE_ALTURA // 2
        self.largura = RAQUETE_LARGURA
        self.altura = RAQUETE_ALTURA
        self.velocidade = RAQUETE_VELOCIDADE

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover_cima(self):
        self.y = max(0, self.y - self.velocidade)

    def mover_baixo(self):
        self.y = min(ALTURA - self.altura, self.y + self.velocidade)

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
