import pygame

from game.utils.constants import FONT_STYLE


class Counter:
  def __init__(self):
    self.count = 0 # El conteno inicia en 0

  def update(self):
    self.count += 1 # Se va sumando de 1 en 1

  def draw(self, screen):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(f'Score: {self.count}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    screen.blit(text, text_rect) # blit = Dibujar una imagen dentro de otra imagen

  def reset(self):
    self.count = 0

  def set_count(self, value):
    self.count = value # Es una variable que se usa para llevar un conteo de n veces