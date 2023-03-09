import pygame, sys 
from settings import *  
from level import Level 
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Backround
background_image = pygame.image.load("asssets/Backround.jpeg")

def make_bg():
  scaled_bg = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0,0))

pygame.display.set_caption('Clone Wars Platformer')
clock = pygame.time.Clock()

level = Level()

while True: 
  for event in pygame.event.get():
       if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

  make_bg()
  
  level.run()

  pygame.display.update()
  clock.tick(60)
