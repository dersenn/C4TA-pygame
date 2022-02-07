import pygame, sys
import os
from settings import *
from level import Level
from player import Player


# Pygame setup
pygame.init()
clock = pygame.time.Clock()
level = Level(screen)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.fill('grey')


  level.run()


  pygame.display.update()
  clock.tick(30)




###############     CMD+B      to run programme
