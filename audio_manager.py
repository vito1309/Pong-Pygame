import pygame


class AudioManager:

    def __init__(self):
        pygame.mixer.init()
        self.som_raquete = self._carregar_som("osu-hit-sound.mp3")
        self.som_parede = self._carregar_som("cartoon-hammer.mp3")
        self.som_ponto = self._carregar_som("sfx_taunt.mp3")
        self._iniciar_musica("jojo.mp3")

    def _carregar_som(self, caminho):
        try:
            return pygame.mixer.Sound(caminho)
        except FileNotFoundError:
            return None

    def _iniciar_musica(self, caminho):
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play(-1)
        except FileNotFoundError:
            pass

    def tocar_raquete(self):
        if self.som_raquete:
            self.som_raquete.play()

    def tocar_parede(self):
        if self.som_parede:
            self.som_parede.play()

    def tocar_ponto(self):
        if self.som_ponto:
            self.som_ponto.play()
