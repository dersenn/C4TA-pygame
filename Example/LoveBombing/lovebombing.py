import pygame
import os

pygame.font.init()
pygame.mixer.init()

# C:/Desktop Users\Desktop

# Aspect ratio scaling
def aspect_scale(img, bx, by):
    ix, iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (sx, sy))

WIDTH, HEIGHT = 1000, 800
# Tuple (width, height) vs python ((width, height))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love bombing")


HEALTH_FONT = pygame.font.Font(os.path.join("Assets", "I-pixel-u.ttf"), 40)
WINNER_FONT = pygame.font.Font(os.path.join("Assets", "I-pixel-u.ttf"), 80)

IMG_WIDTH = 120
GOOD_GUY = pygame.image.load(os.path.join("Assets", "goodguy.png"))
GOOD_GUY = aspect_scale(GOOD_GUY, IMG_WIDTH, 100)
BAD_GUY = pygame.image.load(os.path.join("Assets", "badguy.png"))
BAD_GUY = aspect_scale(BAD_GUY, IMG_WIDTH, 100)

WHITE = (255, 255, 255)
RED = (255, 0,0)
BLACK= (0,0,0)
FPS = 60
VEL = 5

MAX_BULLET = 5
BULLETS_VEL = 10
BULLET_WIDTH = 40

HEART = aspect_scale(pygame.image.load(os.path.join("Assets", "heart.png")), BULLET_WIDTH, 43)
BOMB = aspect_scale(pygame.image.load(os.path.join("Assets", "bomb.png")), BULLET_WIDTH, 42)

GG_HIT = pygame.USEREVENT + 1
BD_HIT = pygame.USEREVENT + 2
RESTART = pygame.USEREVENT + 3

BORDER = pygame.Rect(WIDTH//2 -3 , 0, 6, HEIGHT)

HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "ouch.mp3"))
BOMB_SOUND = pygame.mixer.Sound(os.path.join("Assets", "bomb.mp3"))
HEART_SOUND = pygame.mixer.Sound(os.path.join("Assets", "heart.mp3"))

def draw(goodguy, badguy ,hearts, bombs, goodguy_health, badguy_health):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)

    goodguy_health_text = HEALTH_FONT.render("Health: " + str(goodguy_health), 1, BLACK)
    badguy_health_text = HEALTH_FONT.render("Health: " + str(badguy_health), 1, BLACK)

    WIN.blit( goodguy_health_text, ((WIDTH - goodguy_health_text.get_width() - 150), 10))
    WIN.blit( badguy_health_text, ((badguy_health_text.get_width()//2 + 50), 10))

    WIN.blit(BAD_GUY, (badguy.x, badguy.y))
    WIN.blit(GOOD_GUY, (goodguy.x, goodguy.y))

    for heart in hearts:
        WIN.blit( HEART, (heart.x, heart.y))
    
    for bomb in bombs:
        WIN.blit( BOMB, (bomb.x, bomb.y))


    pygame.display.update()

def draw_winner(text, color):
    winner_text = WINNER_FONT.render(text, 1, color)
    WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width()//2, HEIGHT/2 - winner_text.get_height()//2))

    restart_text = HEALTH_FONT.render("Resart?", 1 , BLACK)
    restart_text2 = HEALTH_FONT.render("Yes = 1    No = 0", 1, BLACK)

    WIN.blit(restart_text, (WIDTH/2 - restart_text.get_width()//2, HEIGHT/2 - restart_text.get_height() + 100))
    WIN.blit(restart_text2, (WIDTH/2 - restart_text2.get_width()//2, HEIGHT/2 - restart_text2.get_height() + 150))

    pygame.display.update()
    pygame.time.delay(200)

    restart_key = pygame.key.get_pressed()
    if restart_key[pygame.K_1] == True:
        pygame.event.post(pygame.event.Event(RESTART))
    elif restart_key[pygame.K_0] == True:
        pygame.quit()

   

def moveCharacter(character, keyUp, keyDown, keyLeft, keyRight):
    keyPressed = pygame.key.get_pressed()

    if keyPressed[keyUp] and character.y - VEL > 0:
        character.y -= VEL
    
    if keyPressed[keyDown] and character.y + VEL +character.height < HEIGHT :
        character.y += VEL
    
    if keyPressed[keyLeft]:
        if keyLeft == pygame.K_LEFT and character.x - VEL > BORDER.x + BORDER.width :
            character.x -= VEL
        
        if keyLeft == pygame.K_a and character.x - VEL > 0:
            character.x -= VEL
    

    if keyPressed[keyRight]:
        if keyRight == pygame.K_RIGHT and character.x + VEL < WIDTH - character.width :
            character.x += VEL
        
        if keyRight == pygame.K_d and character.x + VEL + character.width < BORDER.x - BORDER.width :
            character.x += VEL


def gotHit( hearts, bombs, goodguy, badguy):

    for heart in hearts :
        heart.x -= BULLETS_VEL
        if badguy.colliderect(heart):
            hearts.remove(heart)
            pygame.event.post(pygame.event.Event(BD_HIT))
        elif heart.x < 0:
            hearts.remove(heart)
    
    for bomb in bombs:
        bomb.x += BULLETS_VEL
        if goodguy.colliderect(bomb):
            bombs.remove(bomb)
            pygame.event.post(pygame.event.Event(GG_HIT))
        elif bomb.x > WIDTH:
            bombs.remove(bomb)


def main():
    clock = pygame.time.Clock()

    badguy = pygame.Rect( 100, HEIGHT/2, BAD_GUY.get_width(), BAD_GUY.get_height())
    goodguy = pygame.Rect( 900, HEIGHT/2, GOOD_GUY.get_width(), GOOD_GUY.get_height())

    run = True

    hearts = []
    bombs = []

    goodguy_health = 10
    badguy_health = 10

    while run:
        clock.tick (FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT and len(hearts) < MAX_BULLET :
                    heart = pygame.Rect( goodguy.x + goodguy.width//2, goodguy.y , HEART.get_width() , HEART.get_height())
                    HEART_SOUND.play()
                    hearts.append(heart)
                
                if event.key == pygame.K_LSHIFT and len(bombs) < MAX_BULLET :
                    bomb = pygame.Rect( badguy.x + badguy.width // 2, badguy.y, BOMB.get_width(), BOMB.get_height())
                    BOMB_SOUND.play()
                    bombs.append(bomb)

            
            if event.type == GG_HIT:
                HIT_SOUND.play()
                goodguy_health -= 2
            
            if event.type == BD_HIT:
                HIT_SOUND.play()
                badguy_health -=2
            
            if event.type == RESTART:
                main()
        
        WINNER_TEXT = ""

        if goodguy_health <= 0 :
            WINNER_TEXT = "VIOLENCE WINS!"
            draw_winner(WINNER_TEXT, BLACK)
        
        if badguy_health <= 0 :
            WINNER_TEXT = "LOVE WINS!"
            pygame.draw.rect( WIN, WHITE, BORDER)
            draw_winner(WINNER_TEXT, RED)

        
        
        moveCharacter(goodguy, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        moveCharacter(badguy, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        gotHit(hearts, bombs, goodguy, badguy)

        draw(goodguy, badguy, hearts, bombs, goodguy_health, badguy_health)

if __name__ == "__main__":
    main()