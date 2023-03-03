import pygame
from settings import *
 


class Player(pygame.sprite.Sprite):
  def __init__(self,pos,groups,collision_sprites):
    super().__init__(groups)
    self.image = pygame.Surface((TILE_SIZE // 2,TILE_SIZE))
    self.image = pygame.image.load("asssets/Clone Trooper2.png")
    self.rect = self.image.get_rect(topleft = pos)

  #Movement
    self.direction = pygame.math.Vector2()
    self.speed = 8
    self.gravity = .35
    self.jump_speed = 5
    self.collision_sprites = collision_sprites
    self.on_floor = False 
    self.dead = False

      
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]: 
      self.direction.x = 1
    elif keys[pygame.K_d]:
      self.direction.x = 1
    elif keys[pygame.K_a]:
      self.direction.x = -1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0

    if keys[pygame.K_SPACE] and self.on_floor:
      self.direction.y = -self.jump_speed
    elif keys[pygame.K_w] and self.on_floor:
      self.direction.y = -self.jump_speed




  def vertical_collisions(self):
     self.rect.y += self.direction.y * self.speed
   
     for sprite in self.collision_sprites.sprites():
      if sprite.rect.colliderect(self.rect):
        if self.direction.y > 0:
          self.rect.bottom = sprite.rect.top
          self.direction.y = 0
          self.on_floor = True
        if self.direction.y < 0: 
          self.rect.top = sprite.rect.bottom
          self.direction.y = 0
     if self.on_floor and self.direction.y != 0: 
      self.on_floor = False 
     if self.rect.top > SCREEN_HEIGHT:
      pygame.quit()

    
  def horizontal_collisions(self):  
     self.rect.x += self.direction.x * self.speed

     for sprite in self.collision_sprites.sprites():
      if sprite.rect.colliderect(self.rect):
        if self.direction.x < 0:
          self.rect.left = sprite.rect.right
          self.direction.x = 0
        if self.direction.x > 0:
          self.rect.right = sprite.rect.left 
          self.direction.x = 0
  
 

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y
    

  

  def update(self):
    self.input()
    self.horizontal_collisions() 
    self.vertical_collisions()
    self.apply_gravity()
