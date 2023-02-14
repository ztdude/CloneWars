import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(sel.pos.groups):
    super().__init__(groups)
    self.image = pygame.Surface((TILE.SIZE // 2,TILE_SIZE))
    self.image.fill(PLAYER_COLOR)
    self.rect = self.image.get_rect(topleft = pos)
  
  #Movement
    self.direction = pygame.math.Vector2()
    self.speed = 10
    
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_right]:
      self.direction.x = 1
    elif keys[pygame.K_left]:
      self.direction.x = -1
    else:
      self.direction = 0

    if keys[pygame.K_SPACE]:
      print('jump')
      
  def update(self):
    self.rect.topleft += self.direction * self.speed
    
    
