import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self,pos,groups):
    super().__init__(groups)
    self.image = pygame.Surface((TILE.SIZE // 2,TILE_SIZE))
    self.image.fill(PLAYER_COLOR)
    self.rect = self.image.get_rect(topleft = pos)
  
  #Movement
    self.direction = pygame.math.Vector2()
    self.speed = 10
    self.gravity = .9
    self.jump_speed = 18
    
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_right]:
      self.direction.x = 1
    elif keys[pygame.K_left]:
      self.direction.x = -1
    else:
      self.direction.x = 0

    if keys[pygame.K_SPACE]:
      self.direction.y = -self.jump_speed
      
  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y
    
  def update(self):
    self.input()
    self.rect.x += self.direction.x * self.speed
    self.apply_gravity()
