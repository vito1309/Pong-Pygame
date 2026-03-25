import sys
import pygame
from settings import LARGURA, ALTURA, FPS, TITULO, MARGEM_RAQUETE, RAQUETE_LARGURA
from ball import Bola
from paddle import Raquete
from scoreboard import Placar
from ai_controller import ControladorIA
from renderer import Renderer
from audio_manager import AudioManager
from powerup import GerenciadorPowerUp


class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.tela)
        self.ia = ControladorIA()
        self.audio = AudioManager()

    def _criar_entidades(self):
        self.bola = Bola()
        self.raquete1 = Raquete(x=MARGEM_RAQUETE)
        self.raquete2 = Raquete(x=LARGURA - MARGEM_RAQUETE - RAQUETE_LARGURA)
        self.placar = Placar()
        self.powerup = GerenciadorPowerUp()

    def _processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _mover_jogador(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.raquete1.mover_cima()
        if teclas[pygame.K_DOWN]:
            self.raquete1.mover_baixo()

    def cena_menu(self):
        while True:
            self._processar_eventos()
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                return

            self.renderer.desenhar_menu()
            pygame.display.flip()
            self.clock.tick(FPS)

    def cena_jogo(self):
        self._criar_entidades()

        while True:
            self._processar_eventos()
            self._mover_jogador()
            self.ia.atualizar(self.raquete2, self.bola)

            bateu_parede = self.bola.atualizar()
            if bateu_parede:
                self.audio.tocar_parede()

            if self.bola.rebater_raquete(self.raquete1.rect):
                self.audio.tocar_raquete()
            if self.bola.rebater_raquete(self.raquete2.rect):
                self.audio.tocar_raquete()

            if self.bola.saiu_pela_esquerda():
                self.placar.ponto_jogador2()
                self.audio.tocar_ponto()
                self.bola.resetar(direcao=1)

            if self.bola.saiu_pela_direita():
                self.placar.ponto_jogador1()
                self.audio.tocar_ponto()
                self.bola.resetar(direcao=-1)

            self.powerup.atualizar(self.bola, self.raquete1, self.raquete2)

            vencedor = self.placar.vencedor()
            if vencedor:
                return vencedor

            self.renderer.desenhar_jogo(self.bola, self.raquete1, self.raquete2, self.placar, self.powerup)
            pygame.display.flip()
            self.clock.tick(FPS)

    def cena_vitoria(self, vencedor):
        while True:
            self._processar_eventos()
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_SPACE]:
                return True
            if teclas[pygame.K_ESCAPE]:
                return False

            self.renderer.desenhar_vitoria(vencedor)
            pygame.display.flip()
            self.clock.tick(FPS)

    def executar(self):
        while True:
            self.cena_menu()

            while True:
                vencedor = self.cena_jogo()
                jogar_novamente = self.cena_vitoria(vencedor)
                if not jogar_novamente:
                    break