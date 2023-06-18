import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.boom import Burst
from game.utils.constants import SPACESHIP_SHIELD, BURST_SOUND, POWER_SOUND

class PowerUpManager:
    INITIAL_TME = 5000 
    FINAL_TIME= 10000
    def __init__ (self):
        self.power_ups = []
        self.when_appears = random.randint(self.INITIAL_TME,self.FINAL_TIME)
        self.duration = random.randint(3, 5)
        self.duration_power_2 = 2


    def generate_power_up(self):
        self.powers = random.randint(1,2)
        if self.powers == 1 :
            power_up = Shield()
            self.powers = 1 
        elif self.powers == 2 :
            power_up = Burst()
            self.powers = 2

        self.when_appears += random.randint(self.INITIAL_TME,self.FINAL_TIME)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if (self.powers == 1):
                if game.player.rect.colliderect(power_up.rect):
                    pygame.mixer.Sound.play(POWER_SOUND)
                    game.player.power_time_up = power_up.start_time + (self.duration*1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
            elif (self.powers == 2): 
                if game.player.rect.colliderect(power_up.rect):
                    pygame.mixer.Sound.play(BURST_SOUND)
                    game.player.power_time_up = power_up.start_time + (self.duration_power_2*1000)
                    self.power_ups.remove(power_up)
                    game.bullet_manager.reset()
            power_up.start_time = pygame.time.get_ticks()
            game.player.power_up_type = power_up.type
            game.player.has_power_up = True

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + 5000, now +10000 )