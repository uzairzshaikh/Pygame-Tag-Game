import pygame
import sys
pygame.font.init()

WIDTH, HEIGHT = 1500, 700     #SCREEN SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


COLOUR =[255,255,255]
FPS = 60  #REFRESH RATE

FONT =pygame.font.SysFont('comic sans', 40)  #SCORE AND HISCORE FONT
HIGHEST=[0]    #HIGH SCORE LIST


#PLAYER ATTRIBUTES
PLAYERWIDTH,PLAYERHEIGHT =20,20
LEFTCOLOUR =[0,0,0]
RIGHTCOLOUR =[5,255,255]
VEL = 5  #SPEED OF PLAYERS



def draw_window(LEFTPLAYER,RIGHTPLAYER,SCORE,HISCORE):
    WIN.fill(COLOUR)
    BACKGROUND(SCORE) #BACKGROUND
    pygame.draw.rect(WIN,LEFTCOLOUR, LEFTPLAYER)   #LEFTPLAYER
    pygame.draw.rect(WIN,RIGHTCOLOUR, RIGHTPLAYER) #RIGHTPLAYER
    score = FONT.render("Score: "+ str('%.2f' % SCORE),1,[255,0,0]) #SCORE DISPLAY
    WIN.blit(score,(10,10))
    HI = FONT.render("Hiscore: "+ str('%.2f' % HISCORE),1,[255,0,0]) #SCORE DISPLAY
    WIN.blit(HI, (200, 10))
    pygame.display.update()



def LEFTMOVE(keys_pressed, LEFTPLAYER):  #MOVEMENT OF LEFT PLAYER
    if keys_pressed[pygame.K_a] and LEFTPLAYER.x > 0:
        LEFTPLAYER.x -= VEL
    if keys_pressed[pygame.K_d] and LEFTPLAYER.x < WIDTH - PLAYERWIDTH:
        LEFTPLAYER.x += VEL
    if keys_pressed[pygame.K_w] and LEFTPLAYER.y > 0:
        LEFTPLAYER.y -= VEL
    if keys_pressed[pygame.K_s] and LEFTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        LEFTPLAYER.y += VEL



def RIGHTMOVE(keys_pressed, RIGHTPLAYER):  #MOVEMENT OF RIGHT PLAYER
    if keys_pressed[pygame.K_LEFT]and RIGHTPLAYER.x > 0:
        RIGHTPLAYER.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and RIGHTPLAYER.x < WIDTH - PLAYERWIDTH:
        RIGHTPLAYER.x += VEL
    if keys_pressed[pygame.K_UP] and RIGHTPLAYER.y > 0:
        RIGHTPLAYER.y -= VEL
    if keys_pressed[pygame.K_DOWN] and RIGHTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        RIGHTPLAYER.y += VEL



def BACKGROUND(SCORE):

    if (SCORE//2)%2==0:
        for x in range(int(HEIGHT / PLAYERHEIGHT)):  # LOOP TO CREATE BACKGROUND HORIZONTAL
            if x % 2 == 0:
                pygame.draw.rect(WIN, LEFTCOLOUR, [0,x * PLAYERHEIGHT, WIDTH, PLAYERHEIGHT])
            else:
                pygame.draw.rect(WIN, RIGHTCOLOUR, [0,x * PLAYERHEIGHT, WIDTH, PLAYERHEIGHT])

    else:
        for x in range(int(WIDTH/PLAYERWIDTH)): #LOOP TO CREATE BACKGROUND VERTICAL
            if x%2 == 0:
                pygame.draw.rect(WIN, LEFTCOLOUR, [x*PLAYERWIDTH,0,PLAYERWIDTH,HEIGHT])
            else:
                pygame.draw.rect(WIN, RIGHTCOLOUR, [x*PLAYERWIDTH,0,PLAYERWIDTH,HEIGHT])

def COUNTDOWN(X):
    for i,x in enumerate(X):
        HI = FONT.render(str(x), 1, [255, 0, 0])  # SCORE DISPLAY
        WIN.blit(HI, ((WIDTH/2)-HI.get_width()/2, (HEIGHT/2)+HI.get_height()*i))
        pygame.display.update()
        pygame.time.delay(1000)


def main():
    clock = pygame.time.Clock()
    TIME = 0


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
        RIGHTMOVE(keys_pressed,RIGHTPLAYER)

        if LEFTPLAYER.colliderect(RIGHTPLAYER):
            pygame.time.delay(1000)
            COUNTDOWN(["YOU WERE CAUGHT!","READY!","SET!","GO!"])
            HIGHEST.append(TIME)
            HISCORE = max(HIGHEST)
            break

        else:
            TIME += 1 / FPS
            HISCORE = max(HIGHEST)
        draw_window(LEFTPLAYER,RIGHTPLAYER, TIME, HISCORE)

    main()





if __name__ == "__main__":
    main()