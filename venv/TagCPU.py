import pygame
import sys


pygame.font.init()



WIDTH, HEIGHT = 800, 800     #SCREEN SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


COLOUR =[0,0,0] #FONT COLOUR
FPS = 60  #REFRESH RATE

FONT =pygame.font.SysFont('comic sans', 40)  #SCORE AND HISCORE FONT
HIGHEST=[0]    #HIGH SCORE LIST


#PLAYER ATTRIBUTES
PLAYERWIDTH,PLAYERHEIGHT =20,20
LEFTCOLOUR =[96,235,86]
RIGHTCOLOUR =[198,165,0]
VEL1 = 3  #SPEED OF PLAYER
VEL2 = 2.5  #SPEED OF COMPUTER PLAYER


def draw_window(LEFTPLAYER,RIGHTPLAYER,SCORE,HISCORE):
    BACKGROUND(SCORE) #BACKGROUND
    pygame.draw.rect(WIN,LEFTCOLOUR, LEFTPLAYER)   #LEFTPLAYER
    pygame.draw.rect(WIN,RIGHTCOLOUR, RIGHTPLAYER) #RIGHTPLAYER
    score = FONT.render("Score: "+ str('%.2f' % SCORE),1,COLOUR) #SCORE DISPLAY
    WIN.blit(score,(10,10))
    HI = FONT.render("Hiscore: "+ str('%.2f' % HISCORE),1,COLOUR) #SCORE DISPLAY
    WIN.blit(HI, (200, 10))
    pygame.display.update()



def LEFTMOVE(keys_pressed, LEFTPLAYER):  #MOVEMENT OF LEFT PLAYER
    if keys_pressed[pygame.K_LEFT] and LEFTPLAYER.x > 0:
        LEFTPLAYER.x -= VEL1
    if keys_pressed[pygame.K_RIGHT] and LEFTPLAYER.x < WIDTH - PLAYERWIDTH:
        LEFTPLAYER.x += VEL1
    if keys_pressed[pygame.K_UP] and LEFTPLAYER.y > 0:
        LEFTPLAYER.y -= VEL1
    if keys_pressed[pygame.K_DOWN] and LEFTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        LEFTPLAYER.y += VEL1



def RIGHTMOVE(LEFTPLAYER, RIGHTPLAYER):  #MOVEMENT OF RIGHT PLAYER
    if LEFTPLAYER.x < RIGHTPLAYER.x and RIGHTPLAYER.x > 0:
        RIGHTPLAYER.x -= VEL2
    if LEFTPLAYER.x > RIGHTPLAYER.x and RIGHTPLAYER.x < WIDTH - PLAYERWIDTH:
        RIGHTPLAYER.x += VEL2
    if LEFTPLAYER.y < RIGHTPLAYER.y and RIGHTPLAYER.y > 0:
        RIGHTPLAYER.y -= VEL2
    if LEFTPLAYER.y > RIGHTPLAYER.y and RIGHTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        RIGHTPLAYER.y += VEL2



def BACKGROUND(SCORE):

    if (SCORE//2)%2==0:
        for x in range(int(HEIGHT / PLAYERHEIGHT)+1):  # LOOP TO CREATE BACKGROUND HORIZONTAL
            if x % 2 == 0:
                pygame.draw.rect(WIN, LEFTCOLOUR, [0,x * PLAYERHEIGHT, WIDTH, PLAYERHEIGHT])
            else:
                pygame.draw.rect(WIN, RIGHTCOLOUR, [0,x * PLAYERHEIGHT, WIDTH, PLAYERHEIGHT])

    else:
        for x in range(int(WIDTH/PLAYERWIDTH)+1): #LOOP TO CREATE BACKGROUND VERTICAL
            if x%2 == 0:
                pygame.draw.rect(WIN, LEFTCOLOUR, [x*PLAYERWIDTH,0,PLAYERWIDTH,HEIGHT])
            else:
                pygame.draw.rect(WIN, RIGHTCOLOUR, [x*PLAYERWIDTH,0,PLAYERWIDTH,HEIGHT])



def CAMOFLAGUE(LEFTPLAYER, RIGHTPLAYER,COLUMNS,ROWS,SCORE):    #THIS DECIDES WHEN THE CHASER CAN MOVE
    if (SCORE // 2) % 2 == 0:
        if LEFTPLAYER.y + (PLAYERHEIGHT/2)  not in ROWS:
            RIGHTMOVE(LEFTPLAYER, RIGHTPLAYER)
    else:
        if LEFTPLAYER.x + (PLAYERWIDTH/2)  not in COLUMNS:
            RIGHTMOVE(LEFTPLAYER,RIGHTPLAYER)



def COUNTDOWN(X):
    for i,x in enumerate(X):
        HI = pygame.font.SysFont('comic sans', 60).render(str(x), 1, COLOUR)  # SCORE DISPLAY
        WIN.blit(HI, ((WIDTH/2)-HI.get_width()/2, (HEIGHT/2)+HI.get_height()*i))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.time.delay(1000)


def main():
    clock = pygame.time.Clock()
    SCORE = 0

    COLUMNS =[(x/2) * PLAYERWIDTH for x in range(1,int(WIDTH/PLAYERWIDTH),4)]
    ROWS = [(y/2) * PLAYERHEIGHT for y in range(1, int(HEIGHT/PLAYERHEIGHT), 4)]

    #INITIAL PLAYER POSITIONS
    LEFTX,  LEFTY= 100, (HEIGHT/2)-(PLAYERHEIGHT/2)
    RIGHTX, RIGHTY = WIDTH - 100 - PLAYERWIDTH, (HEIGHT/2)-(PLAYERHEIGHT/2)

    #CREATING PLAYER OBJECTS
    LEFTPLAYER =pygame.Rect( LEFTX,  LEFTY, PLAYERWIDTH, PLAYERHEIGHT)
    RIGHTPLAYER = pygame.Rect(RIGHTX, RIGHTY, PLAYERWIDTH, PLAYERHEIGHT)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()


        LEFTMOVE(keys_pressed, LEFTPLAYER)
        CAMOFLAGUE(LEFTPLAYER, RIGHTPLAYER, COLUMNS, ROWS, SCORE)

        if LEFTPLAYER.colliderect(RIGHTPLAYER):
            pygame.time.delay(1000)
            COUNTDOWN(["YOU WERE CAUGHT!","READY!","SET!","GO!"])
            HIGHEST.append(SCORE)
            break

        else:
            SCORE += 1 / FPS
            HISCORE = max(HIGHEST)
        draw_window(LEFTPLAYER,RIGHTPLAYER, SCORE, HISCORE)

    main()


if __name__ == "__main__":
    main()


