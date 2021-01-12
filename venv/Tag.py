import pygame
WIDTH , HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


COLOUR =[255,255,255]
FPS = 60
VEL = 2

PLAYERWIDTH,PLAYERHEIGHT =100,100
LEFTCOLOUR =[255,255,0]
RIGHTCOLOUR =[255,0,0]

def draw_window(LEFTX,LEFTY,RIGHTX,RIGHTY):
    WIN.fill(COLOUR)
    LEFTIMAGE = pygame.draw.rect(WIN,LEFTCOLOUR, [LEFTX, LEFTY, PLAYERWIDTH,PLAYERHEIGHT])
    RIGHTIMAGE = pygame.draw.rect(WIN,RIGHTCOLOUR, [RIGHTX, RIGHTY , PLAYERWIDTH,PLAYERHEIGHT])
    pygame.display.update()


def LEFTMOVE(keys_pressed, LETX, LETY):
    if keys_pressed[pygame.K_a] and LETX > 0:
        LETX -= VEL
    if keys_pressed[pygame.K_d] and LETX < WIDTH - PLAYERWIDTH:
        LETX += VEL
    if keys_pressed[pygame.K_w] and LETY > 0:
        LETY -= VEL
    if keys_pressed[pygame.K_s] and LETY < HEIGHT - PLAYERHEIGHT:
        LETY += VEL
    return LETX, LETY


def RIGHTMOVE(keys_pressed, RIGHTX, RIGHTY):
    if keys_pressed[pygame.K_LEFT]:
        RIGHTX -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        RIGHTX += VEL
    if keys_pressed[pygame.K_UP]:
        RIGHTY -= VEL
    if keys_pressed[pygame.K_DOWN]:
        RIGHTY += VEL
    return RIGHTX, RIGHTY

def main():
    clock = pygame.time.Clock()
    run = True

    LEFTX,  LEFTY= 100, (HEIGHT/2)-(PLAYERHEIGHT/2)
    RIGHTX, RIGHTY = WIDTH - 100 - PLAYERWIDTH, (HEIGHT/2)-(PLAYERHEIGHT/2)



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()


        LEFTX,LEFTY=LEFTMOVE(keys_pressed,LEFTX,LEFTY)
        RIGHTX, RIGHTY = RIGHTMOVE(keys_pressed,RIGHTX,RIGHTY)





        draw_window(LEFTX,LEFTY,RIGHTX,RIGHTY)

    pygame.quit()


if __name__ == "__main__":
    main()