import pygame, sys
import os
from settings import *
from player import Player


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# level = Level(screen)

player = Player(0, 0, tile_size, tile_size, screen)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.fill('grey')


  # level.run()

  # player.move(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
  player.update()


  pygame.display.update()
  clock.tick(60)

