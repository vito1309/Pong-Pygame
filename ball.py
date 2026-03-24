import random
import pygame
from settings import LARGURA, ALTURA, BOLA_RAIO, BOLA_VELOCIDADE, BRANCO

VARIACAO_MAXIMA = 2


class Bola:

    def __init__(self):
        self.raio = BOLA_RAIO
        self.resetar(direcao=1)

    def resetar(self, direcao=1):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.vel_x = BOLA_VELOCIDADE * direcao
        self.vel_y = BOLA_VELOCIDADE

    @property
    def rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

    def _aplicar_variacao(self):
        self.vel_y += random.uniform(-VARIACAO_MAXIMA, VARIACAO_MAXIMA)
        self.vel_y = max(-8, min(8, self.vel_y))

    def atualizar(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y - self.raio <= 0 or self.y + self.raio >= ALTURA:
            self.vel_y = -self.vel_y
            self._aplicar_variacao()
            return True
        return False

    def rebater_raquete(self, raquete_rect):
        if self.rect.colliderect(raquete_rect):
            if raquete_rect.centerx < LARGURA // 2 and self.vel_x < 0:
                self.vel_x = -self.vel_x
                self._aplicar_variacao()
                return True
            elif raquete_rect.centerx > LARGURA // 2 and self.vel_x > 0:
                self.vel_x = -self.vel_x
                self._aplicar_variacao()
                return True
        return False

    def saiu_pela_esquerda(self):
        return self.x + self.raio < 0

    def saiu_pela_direita(self):
        return self.x - self.raio > LARGURA

    def desenhar(self, tela):
        pygame.draw.circle(tela, BRANCO, (self.x, self.y), self.raio)