import pygame, sys
import os
from settings import * 

class Player:
  def __init__(self, x, y, w, h, surface):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.bounds = pygame.Rect(self.x, self.y, self.w, self.h)
    self.surface = surface
    self.vel = 10


  def move(self):
    keyPressed = pygame.key.get_pressed()

    if keyPressed[pygame.K_UP] and self.y - self.vel >= 0:
      self.y -= self.vel

    if keyPressed[pygame.K_DOWN] and self.y + self.vel + self.h <= screen_height:
      self.y += self.vel

    if keyPressed[pygame.K_LEFT] and self.x - self.vel >= 0:
      self.x -= self.vel

    if keyPressed[pygame.K_RIGHT] and self.x + self.vel <= screen_width - self.w:
      self.x += self.vel


  def draw(self, color):
    self.bounds = pygame.Rect(self.x, self.y, self.w, self.h)
    pygame.draw.rect(self.surface, color, self.bounds)


  def update(self, running):
    if running == False:
      self.draw(red)
    else:
      self.move()
      self.draw(black)
