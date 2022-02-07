import pygame, sys
import os
from settings import * 
from player import Player


class Level:
  def __init__(self, surface):
    self.surface = surface
    self.player = Player(0, 0, tile_size, tile_size, self.surface)

    self.obstacle = Obstacle(600, 200, tile_size, tile_size * 3, self.surface)

    self.running = True

  def collision(self):
    if self.obstacle.bounds.colliderect(self.player.bounds):
      # print('collision')
      self.running = False

  def restart(self):
    restart_key = pygame.key.get_pressed()
    if restart_key[pygame.K_1] == True:
      pygame.event.post(pygame.event.Event(pygame.USEREVENT + 3))
    elif restart_key[pygame.K_0] == True:
      pygame.quit()


  def run(self):
    self.obstacle.draw()
    self.collision()
    self.player.update(self.running)
    if not self.running:
      self.restart()
    #   print('restart?')



class Obstacle:
  def __init__(self, x, y, w, h, surface):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.surface = surface
    self.bounds = pygame.Rect(self.x, self.y, self.w, self.h)

  def draw(self):
    pygame.draw.rect(self.surface, green, self.bounds)

