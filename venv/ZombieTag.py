import pygame
import sys
import random

width, height=1500,700
colour =(0,0,0)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")
fps=60



class Player:
    def __init__(self,startingx,startingy,size,speed,colour):
        self.x = startingx
        self.y = startingy
        self.size = size
        self.speed = speed
        self.colour = colour
        self.left_wall = [self.y+x for x in range(size)]
        self.right_wall =[self.x+x for x in range(size)]
        self.top_wall = [self.x+x for x in range(size)]
        self.bottom_wall = [self.x+x for x in range(size)]


    def move(self,keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.x < width - self.size:
            self.x += self.speed
        if keys_pressed[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.y < height - self.size:
            self.y += self.speed
        self.rect = pygame.Rect( self.x, self.y , self.size, self.size) #if defined earlier, will only call initial values


class Zombie:
    def __init__(self,startingx,startingy,size,speed,colour):
        self.x = startingx
        self.y = startingy
        self.size = size
        self.speed = speed
        self.colour = colour
        self.left_wall = [self.y+x for x in range(size)]
        self.right_wall =[self.x+x for x in range(size)]
        self.top_wall = [self.x+x for x in range(size)]
        self.bottom_wall = [self.x+x for x in range(size)]

    def chase(self,Player):
        if Player.x < self.x and self.x > 0:
            self.x -= self.speed
        if Player.x > self.x and self.x < width - self.size:
            self.x += self.speed
        if Player.y < self.y and self.y > 0:
            self.y -= self.speed
        if Player.y > self.y and self.y < height - self.size:
            self.y += self.speed
        self.rect = pygame.Rect( self.x, self.y , self.size, self.size)

    def randommove(self):
        self.x -= random.randint(0, 2)
        self.y +=random.randint(0,2)
        self.x += random.randint(0, 2)
        self.y -= random.randint(0, 2)
        self.rect = pygame.Rect( self.x, self.y , self.size, self.size)


class Island:
    def __init__(self,size, colour, startingx , startingy):
        self.size = size
        self.colour = colour
        self.x = startingx
        self.y = startingy
        self.rect = pygame.Rect( self.x, self.y , self.size, self.size)
    
def draw_player(Player):
    pygame.draw.rect(window, Player.colour,(Player.rect))

def draw_window(Play,Zomb,land,time):
    window.fill(colour)
    if int(time) < 5:
        pygame.draw.rect(window, land.colour, (land.rect))
    draw_player(Zomb)
    draw_player(Play)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    time = 0
    Play = Player(0,0,20,2,(255,7,6))
    Zomb = Zombie(900, 600, 20, 1.5, (200, 7, 200))
    land = Island(200,(0,250,0), 200,200)
    while True:
        clock.tick(fps)
        if int(time)==10:
            time=0
            landx=random.randint(0,width-land.size)
            landy=random.randint(0,height-land.size)
            land= Island(200,(0,250,0), landx,landy)
        else:
            time += 1/60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys_pressed = pygame.key.get_pressed()

        Play.move(keys_pressed)
        if Play.rect.colliderect(land) and int(time)<5:
            Zomb.randommove()
        else:
            Zomb.chase(Play)

        if Play.rect.colliderect(Zomb):
            break

        draw_window(Play, Zomb,land,time)



main()