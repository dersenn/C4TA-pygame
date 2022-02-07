import pygame
import os
pygame.init()



speed = 10
dwell = 1

first_character =  1
second_character = 2
third_character =  3
fourth_character = 5

direction = "idle"
screen = pygame.display.set_mode((800,600))

class AnimatedSprite:
    # Javascript  constructor( screen, x, y, frames) {
    #   this.screen = screen;
    # }
    def __init__(self, screen, x, y, frames): 
        self.screen = screen
        self.x = x
        self.y = y
        self.index = 0
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()
        self.dwell_countdown = dwell

    def advanceImage(self, index, frame_set_start, frame_set_end ):
        
        self.dwell_countdown -= 1
        
        if self.dwell_countdown < 0:
            self.dwell_countdown = dwell
            print(self.index)    
            self.index = (self.index + 1)%(frame_set_end+1)
            if self.index<frame_set_start:
                self.index = frame_set_start
                
                

    def draw(self):
        screen.blit(self.frames[self.index],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))


def addFrames():

    sheet = pygame.image.load(os.path.join("Assets", 'walkcycles.png'))
    r = sheet.get_rect()
    rows = 8
    columns = 12
    img_width = r.w/columns
    img_height = r.h/rows

    frames = []
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(col*img_width, row*img_height, img_width, img_height)
            frames.append(sheet.subsurface(rect))

    return frames

def main() :
    clock = pygame.time.Clock()

    set_index = 0
    frame_set_start = set_index * 12 + 6
    frame_set_end = frame_set_start + 2

    frames = addFrames()
 
    image_dims = frames[0].get_rect()

    #Reminder: this is how you resize the image if you want.
    image_scale = 3
    image_dims = (image_dims.w*image_scale,image_dims.h*image_scale)

    for i in range(len(frames)):
        frames[i] = pygame.transform.scale(frames[i], image_dims)

    sprite = AnimatedSprite(screen, 400, 300, frames)

   

    #Draw all images on the screen
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    set_index = first_character
                elif event.key == pygame.K_2:
                    set_index = second_character
                elif event.key == pygame.K_3:
                    set_index = third_character
                elif event.key == pygame.K_4:
                    set_index = fourth_character

            #Since set index has usually just been adjusted,
            #update the frame starts and ends.
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            sprite.x-=speed
            direction = "left"
        elif pressed[pygame.K_RIGHT]:
            sprite.x+=speed   
            direction = "right"
        else:
            direction = "idle"
        
        if (direction == "left"):
            frame_set_start = set_index * 12 + 9
            frame_set_end = frame_set_start + 2
        elif (direction == "right"):
            frame_set_start = set_index * 12 + 3
            frame_set_end = frame_set_start + 2
        else:
            frame_set_start = set_index * 12 + 6
            frame_set_end = frame_set_start + 2
            
        screen.fill((0,0,0)) #fill screen with black
        sprite.draw()
        sprite.advanceImage(set_index, frame_set_start, frame_set_end )
        pygame.display.flip()

        #Delay to get 30 fps
        clock.tick(10)

if __name__ == "__main__":
    main()
