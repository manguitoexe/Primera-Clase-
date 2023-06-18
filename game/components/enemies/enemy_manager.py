import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import BURST_TYPE


class EnemyManager:
  def __init__(self):
    self.enemies = []
    
  def update(self, game):
    self.add_enemy()
    
    for enemy in self.enemies:
      if game.player.power_up_type != BURST_TYPE:
          enemy.update(self.enemies, game)
      else:
          self.enemies = []
  
  def draw(self, screen):
    for enemy in self.enemies:
      enemy.draw(screen)
      
  def add_enemy(self):
    enemy_type = random.randint(1,2)
    if enemy_type == 1:
      enemy = Enemy()
    else:
      x_speed = 5
      y_speed = 2
      move_x_for = [50, 120]
      enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)

    if len(self.enemies) < 1:
      self.enemies.append(enemy)
      
  def reset(self):
    self.enemies = []