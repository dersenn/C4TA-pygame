import pygame

vertical_tile_number = 12
horizontal_tile_number = 18
tile_size = 60 

screen_height = vertical_tile_number * tile_size
screen_width = horizontal_tile_number * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)