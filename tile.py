import pygame 
from settings import *

class Tile(pygame.sprite.Sprite): 
    def __init__(self,pos,groups): 
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

class SpecTile(pygame.sprite.Sprite): 
    def __init__(self,pos,groups): 
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image = pygame.image.load("C:\\Users\\log94\\OneDrive\\Desktop\\zt_work\\pixilart-drawing.png")
        self.rect = self.image.get_rect(topleft = pos)


class SpecTile1(pygame.sprite.Sprite): 
    def __init__(self,pos,groups): 
        super().__init__(groups)
        self.image = pygame.Surface((4 * TILE_SIZE,TILE_SIZE//3))
        self.image = pygame.image.load("C:\\Users\\log94\\OneDrive\\Desktop\\zt_work\\Bigg Platform.png")
        self.rect = self.image.get_rect(topleft = pos)
