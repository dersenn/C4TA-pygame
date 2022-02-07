from settings import *
import os
import pygame


def import_folder(path):
  surface_list = []

  for _,__,image_files in walk(path):
    for image in image_files:
      full_path = path + '/' + image
      image_surf = pygame.image.load(full_path).convert_alpha()
      surface_list.append(image_surf)

  return surface_list