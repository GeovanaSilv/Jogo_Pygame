# trabalhando com sprite no pygame
import pygame as pg
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random    

class Tiro(pg.sprite.Sprite):
    """  Define aqui o construtor e outros metodos  """
    def __init__(self, x,y):
        super(Tiro,self).__init__() # chama o construtor pai
        self.surf = pg.Surface((5,15))
        self.surf.fill((255,128,70)) # 
        self.rect = self.surf.get_rect(
            center = (
                x,y
                )
        )   
        self.speed = 3

    def update(self):
        self.rect.move_ip(0,-self.speed)
        if self.rect.bottom < 0:
            self.kill()