import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(sel.pos.groups):
    super().__init__(groups)
    self.image = pygame.Surface((TILE.SIZE // 2,TILES_SIZE))
    self.image.fill(PLAYER_COLOR)
    self.rect = self.image.get_rect(toplefty = pos)
  
  #Movement
    self.direction = pygame.math.Vector2()
    self.speed = 10
    
  def input(self):
    keys = pygame.
