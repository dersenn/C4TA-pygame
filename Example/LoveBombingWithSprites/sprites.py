import pygame
pygame.init()

speed = 2
dwell = 3

WIDTH, HEIGHT = 1000, 800
# Tuple (width, height) vs python ((width, height))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class AnimatedSprite:
    # Javascript  constructor( screen, x, y, frames) {
    #   this.screen = screen;
    # }
    def __init__(self, screen, x, y, frames): 
        self.screen = WIN
        self.x = x
        self.y = y
        self.index = 0
        self.frames = frames
        self.rect = pygame.Rect(self.x, self.y, self.frames[self.index].get_width() -self.frames[self.index].get_width()/2, self.frames[self.index].get_height())
        self.width = self.rect.width
        self.height =self.rect.height
        
        self.dwell_countdown = dwell

    def advanceImage(self, index, frame_set_start, frame_set_end ):
        
        self.dwell_countdown -= 1
        
        if self.dwell_countdown < 0:
            self.dwell_countdown = dwell 
            self.index = (self.index + 1)%(frame_set_end+1)
            if self.index<frame_set_start:
                self.index = frame_set_start
                
    def colliderect2(self, sprite):
        return self.rect.colliderect(sprite)

    def draw(self):
        WIN.blit(self.frames[self.index],(self.x,self.y) )

     