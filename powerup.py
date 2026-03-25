import random
import pygame
from settings import LARGURA, ALTURA, BOLA_RAIO, BOLA_VELOCIDADE


class BolaDistracao:

    def __init__(self):
        self.raio = BOLA_RAIO
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.vel_x = random.choice([-1, 1]) * BOLA_VELOCIDADE
        self.vel_y = random.uniform(-BOLA_VELOCIDADE, BOLA_VELOCIDADE)
        self.cor = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

    @property
    def rect(self):
        """Retorna o retângulo de colisão da bola."""
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

    def atualizar(self):
        """Move a bola e rebate nas bordas superior e inferior."""
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y - self.raio <= 0 or self.y + self.raio >= ALTURA:
            self.vel_y = -self.vel_y

    def rebater_raquete(self, raquete_rect):
        """Rebate na raquete sem pontuar."""
        if self.rect.colliderect(raquete_rect):
            if raquete_rect.centerx < LARGURA // 2 and self.vel_x < 0:
                self.vel_x = -self.vel_x
            elif raquete_rect.centerx > LARGURA // 2 and self.vel_x > 0:
                self.vel_x = -self.vel_x

    def saiu_da_tela(self):
        """Retorna True se a bola saiu pela esquerda ou direita."""
        return self.x + self.raio < 0 or self.x - self.raio > LARGURA

    def desenhar(self, tela):
        """Desenha a bola com sua cor unica."""
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)


class GerenciadorPowerUp:
    """Controla o timer do power-up e a lista de bolas de distração ativas."""

    INTERVALO_MS = 5000
    QUANTIDADE_BOLAS = 3

    def __init__(self):
        """Inicializa o gerenciador sem bolas de distração."""
        self.bolas = []
        self._ultimo_powerup = pygame.time.get_ticks()
        self._powerup_ativo = False

    def atualizar(self, bola_verdadeira, raquete1, raquete2):
        """Verifica o timer, gera bolas na colisão e atualiza as bolas existentes."""
        agora = pygame.time.get_ticks()

        if agora - self._ultimo_powerup >= self.INTERVALO_MS:
            self._powerup_ativo = True

        if self._powerup_ativo and bola_verdadeira.rect.colliderect(raquete1.rect) or \
           self._powerup_ativo and bola_verdadeira.rect.colliderect(raquete2.rect):
            self._fragmentar()
            self._powerup_ativo = False
            self._ultimo_powerup = agora

        for bola in self.bolas:
            bola.atualizar()
            bola.rebater_raquete(raquete1.rect)
            bola.rebater_raquete(raquete2.rect)

        self.bolas = [b for b in self.bolas if not b.saiu_da_tela()]

    def _fragmentar(self):
        """Gera 3 novas bolas de distração."""
        for _ in range(self.QUANTIDADE_BOLAS):
            self.bolas.append(BolaDistracao())

    def desenhar(self, tela):
        """Desenha todas as bolas de distração ativas."""
        for bola in self.bolas:
            bola.desenhar(tela)

    def resetar(self):
        """Limpa todas as bolas de distração ao reiniciar a partida."""
        self.bolas = []
        self._ultimo_powerup = pygame.time.get_ticks()
        self._powerup_ativo = False