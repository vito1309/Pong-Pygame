import pygame
from settings import LARGURA, ALTURA, PRETO, BRANCO, CINZA


class Renderer:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_placar = pygame.font.SysFont(None, 48)
        self.fonte_titulo = pygame.font.SysFont(None, 80)
        self.fonte_media = pygame.font.SysFont(None, 36)
        self.fonte_pequena = pygame.font.SysFont(None, 28)

    def limpar(self):
        self.tela.fill(PRETO)

    def desenhar_linha_central(self):
        segmento = 20
        espaco = 10
        for y in range(0, ALTURA, segmento + espaco):
            pygame.draw.rect(self.tela, CINZA, (LARGURA // 2 - 2, y, 4, segmento))

    def desenhar_placar(self, placar):
        texto = self.fonte_placar.render(f"{placar.pontos_j1}  {placar.pontos_j2}", True, BRANCO)
        self.tela.blit(texto, texto.get_rect(center=(LARGURA // 2, 30)))

    def desenhar_jogo(self, bola, raquete1, raquete2, placar):
        self.limpar()
        self.desenhar_linha_central()
        raquete1.desenhar(self.tela)
        raquete2.desenhar(self.tela)
        bola.desenhar(self.tela)
        self.desenhar_placar(placar)

    def desenhar_menu(self):
        self.limpar()

        titulo = self.fonte_titulo.render("PONG", True, BRANCO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))

        controles = self.fonte_pequena.render("Jogador: Setas  |  Oponente: IA", True, CINZA)
        self.tela.blit(controles, controles.get_rect(center=(LARGURA // 2, ALTURA // 2)))

        if pygame.time.get_ticks() % 2000 < 1000:
            instrucao = self.fonte_pequena.render("Pressione ESPACO para jogar", True, BRANCO)
            self.tela.blit(instrucao, instrucao.get_rect(center=(LARGURA // 2, ALTURA // 2 + 60)))

    def desenhar_vitoria(self, vencedor):
        self.limpar()

        titulo = self.fonte_titulo.render(f"{vencedor} venceu!", True, BRANCO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, ALTURA // 3)))

        opcao1 = self.fonte_media.render("ESPACO  —  Jogar novamente", True, CINZA)
        opcao2 = self.fonte_media.render("ESC  —  Voltar ao menu", True, CINZA)
        self.tela.blit(opcao1, opcao1.get_rect(center=(LARGURA // 2, ALTURA // 2 + 20)))
        self.tela.blit(opcao2, opcao2.get_rect(center=(LARGURA // 2, ALTURA // 2 + 60)))
