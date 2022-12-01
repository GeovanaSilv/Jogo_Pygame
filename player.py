# trabalhando com sprite no pygame
import pygame as pg
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT)

class Player(pg.sprite.Sprite):
    """  Define aqui o construtor e outros metodos  """
    def __init__(self, width, heigth):
        super(Player,self).__init__() # chama o construtor pai
        self.width = width
        self.heigth = heigth
        self.surf = pg.Surface((75,25))
        self.surf.fill((255,0,0)) # vermelho
        self.rect = self.surf.get_rect(
            center = (10,380)
        )   

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)     
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)     
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)     
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)                         

        # mantem o objeto na classe
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.heigth:
            self.rect.bottom = self.heigth      