import pygame
pygame.font.init()

WIDTH , HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


COLOUR =[255,255,255]
FPS = 60
VEL = 2
COLLISION = pygame.USEREVENT
FONT =pygame.font.SysFont('comicsans', 40 )

PLAYERWIDTH,PLAYERHEIGHT =100,100
LEFTCOLOUR =[255,255,0]
RIGHTCOLOUR =[255,0,0]


def draw_window(LEFTPLAYER,RIGHTPLAYER,SCORE):
    WIN.fill(COLOUR)
    LEFTIMAGE = pygame.draw.rect(WIN,LEFTCOLOUR, LEFTPLAYER)
    RIGHTIMAGE = pygame.draw.rect(WIN,RIGHTCOLOUR, RIGHTPLAYER)
    hiscore = FONT.render("Score:"+ str('%.2f' % SCORE),1,[5,255,255])
    WIN.blit(hiscore,(10,10))
    pygame.display.update()


def LEFTMOVE(keys_pressed, LEFTPLAYER):
    if keys_pressed[pygame.K_a] and LEFTPLAYER.x > 0:
        LEFTPLAYER.x -= VEL
    if keys_pressed[pygame.K_d] and LEFTPLAYER.x < WIDTH - PLAYERWIDTH:
        LEFTPLAYER.x += VEL
    if keys_pressed[pygame.K_w] and LEFTPLAYER.y > 0:
        LEFTPLAYER.y -= VEL
    if keys_pressed[pygame.K_s] and LEFTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        LEFTPLAYER.y += VEL



def RIGHTMOVE(keys_pressed, RIGHTPLAYER):
    if keys_pressed[pygame.K_LEFT]and RIGHTPLAYER.x > 0:
        RIGHTPLAYER.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and RIGHTPLAYER.x < WIDTH - PLAYERWIDTH:
        RIGHTPLAYER.x += VEL
    if keys_pressed[pygame.K_UP] and RIGHTPLAYER.y > 0:
        RIGHTPLAYER.y -= VEL
    if keys_pressed[pygame.K_DOWN] and RIGHTPLAYER.y < HEIGHT - PLAYERHEIGHT:
        RIGHTPLAYER.y += VEL


def main():
    clock = pygame.time.Clock()
    time = 0
    run = True

    LEFTX,  LEFTY= 100, (HEIGHT/2)-(PLAYERHEIGHT/2)
    RIGHTX, RIGHTY = WIDTH - 100 - PLAYERWIDTH, (HEIGHT/2)-(PLAYERHEIGHT/2)

    LEFTPLAYER =pygame.Rect( LEFTX,  LEFTY, PLAYERWIDTH, PLAYERHEIGHT)
    RIGHTPLAYER = pygame.Rect(RIGHTX, RIGHTY, PLAYERWIDTH, PLAYERHEIGHT)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()


        LEFTMOVE(keys_pressed, LEFTPLAYER)
        RIGHTMOVE(keys_pressed,RIGHTPLAYER)

        if LEFTPLAYER.colliderect(RIGHTPLAYER):
            draw_window(LEFTPLAYER,RIGHTPLAYER, time)
        else:
            time += 1 / FPS

        draw_window(LEFTPLAYER,RIGHTPLAYER, time)


    pygame.quit()


if __name__ == "__main__":
    main()