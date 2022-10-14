import pygame
import sys
import random
import math
import numpy as np
from pygame.locals import *

FPS = 60
    
BLACK = (0  , 0  ,   0)
RED   = (255, 0  ,   0)
GREEN = (0  , 255,   0)
BLUE  = (0  , 0  , 255)
WHITE = (255, 255, 255)

global tileX                                        # tamanho horizontal do tile
global tileY                                        # tamanho vertical do tile 
global sizeP                                        # tamanho do pixel

tileX = 100
tileY = 100
sizeP = 10

HEIGHT = 600                                        # tamanho janela 
WIDTH  = 600                                        # tamanho janela 

SIZE_SCREEN = [HEIGHT+1, WIDTH+1]

vectors = []
dists = []

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(SIZE_SCREEN)
    SCREEN.fill(BLACK)
    
    pygame.display.set_caption('perlin noise')

    RUN = True
    
    while RUN:
        clock = pygame.time.Clock()
        clock.tick(FPS)
        
        SCREEN.fill(BLACK)
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                RUN = False

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            RUN = False        
        
        # img = pygame.image.load('img.png')
        # SCREEN.blit(img, [0,0])

        for x in range(int((HEIGHT / tileX)+1)):
            vectors.append([])
            for y in range(int((WIDTH / tileY)+1)):
                angulo = random.randint(0, 360)
                angulo = math.radians(angulo)                                                                                             #|
                vectors[x].append([[x * tileX, y * tileY],                                                                                #|define um vetor aleatoria para cada cato de tile
                                  [round((x * tileX) + (math.cos(angulo) * tileX) - 1), round((y * tileY)+(math.sin(angulo) * tileY) - 1)]])            #|
        
        for y in range(int(HEIGHT / sizeP)):
            dists.append([])
            for x in range(int(WIDTH / sizeP)):
                tile = [y // 10, x // 10]
                # print(x, y)

#(tile[0] * tileX) + (tile[0] * tileX), (tile[1] * tileY) + (tile[1] * tileY)



                dists[y].append([[[tile[0] * tileY + 100, tile[1] * tileX], [x * sizeP, y * sizeP]]])
                # dists[y].append([[[tile[0] * tileY,  tile[1] * tileX +100], [y * sizeP, x * sizeP]]])
                # dists[y].append([[[tile[0] * tileY + 100, tile[1] * tileY + 100], [y * sizeP, x * sizeP]]])
                # dists[y].append([[[tile[0] * tileY, tile[1] * tileX], [y * sizeP, x * sizeP]]])
                
                # if(random.randint(0, 100) == 50):
                #     pygame.draw.line(SCREEN, BLUE, dists[y][x][0][0], dists[y][x][0][1])
                #     pygame.draw.line(SCREEN, BLUE, dists[y][x][1][0], dists[y][x][1][1])
                #     pygame.draw.line(SCREEN, BLUE, dists[y][x][2][0], dists[y][x][2][1])
                #     pygame.draw.line(SCREEN, BLUE, dists[y][x][3][0], dists[y][x][3][1])

                # color = random.randint(0, 200)
                # pygame.draw.rect(SCREEN,
                #                 [color, color, color],
                #                 [x*sizeP, y*sizeP, x*sizeP+sizeP, y*sizeP+sizeP]) 
        print(str(dists))
        pygame.quit()
        for x in range(int((HEIGHT / tileX)+1)):
            for y in range(int((WIDTH / tileY)+1)):
                pygame.draw.line(SCREEN, GREEN, [vectors[x][y][0][0], vectors[x][y][0][1]], [vectors[x][y][1][0], vectors[x][y][1][1]])
            
                pygame.draw.rect(SCREEN, RED, 
                               [y*tileY, x*tileX, y*tileY+tileY+1, x*tileX+tileX+1], 1)

        pygame.display.update()
        # print(vectors)
    

if __name__ == '__main__':
    print('em execução')
    main()
    
