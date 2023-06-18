import pygame

from game.utils.constants import MUSIC_BG

class Volumen:
    def __init__(self):
        pygame.mixer.music.load('Sounds/MusicFond.mp3')
        pygame.mixer.music.play(-1)
