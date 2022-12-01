# trabalhando com sprite no pygame
import pygame as pg
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random    

class Inimigo(pg.sprite.Sprite):
    """  Define aqui o construtor e outros metodos  """
    def __init__(self, width, heigth):
        super(Inimigo,self).__init__() # chama o construtor pai
        self.surf = pg.Surface((25,25))
        self.surf.fill((255,128,70)) # 
        self.rect = self.surf.get_rect(
            center = (
                random.randint(width+20,width+100),
                random.randint(0,heigth-80)
                )
        )   
        self.speed = random.randint(3,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()