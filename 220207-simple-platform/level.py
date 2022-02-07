import pygame 
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Crate, Coin, Palm
from player import Player

class Level:
  def __init__(self, surface):
    # general setup
    self.display_surface = surface
