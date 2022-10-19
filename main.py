import pygame
import random
import math
import numpy as np 
from pygame.locals import *

# esse recado é para o futuro daniel(cara que fez esse codigo): eu espero que esse não seja seu portifolio
# boa sorte você 

FPS = 1
    
BLACK = (0  , 0  ,   0)
RED   = (255, 0  ,   0)
GREEN = (0  , 255,   0)
BLUE  = (0  , 0  , 255)
WHITE = (255, 255, 255)

tileX = 100
tileY = 100
sizeP = 10

HEIGHT = 600                                        # tamanho janela 
WIDTH  = 600                                        # tamanho janela 

SIZE_SCREEN = [HEIGHT+1, WIDTH+1]

vectors = []                                         # vetores (linha verdes)

def media(num1, num2, num3, num4):
    return (num1 + num2 + num3 + num4) / 4

def main():
    pygame.init()
    
    SCREEN = pygame.display.set_mode(SIZE_SCREEN)
    SCREEN.fill(BLACK)
    
    pygame.display.set_caption('perlin noise')

    RUN = True

    for x in range(int((HEIGHT / tileX)+1)):
            vectors.append([])
            for y in range(int((WIDTH / tileY)+1)):
                angulo = random.randint(0, 360)
                angulo = math.radians(angulo)                                                                                             #|
                vectors[x].append([[x * tileX, y * tileY],                                                                                #|define um vetor aleatoria para cada cato de tile
                                  [round((x * tileX) + (math.cos(angulo) * tileX) - 1), round((y * tileY)+(math.sin(angulo) * tileY) - 1)]])            #|
        
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

        if RUN == False:
            break

        # img = pygame.image.load('img.png')
        # SCREEN.blit(img, [0,0])

        
        for y in range(int(HEIGHT / sizeP)):
            for x in range(int(WIDTH / sizeP)):

                tile = [x // 10, y // 10]
                
                a = [[x * sizeP, y * sizeP],             [tile[0] * tileX, tile[1] * tileY]]
                b = [[x * sizeP, y * sizeP],       [tile[0] * tileX +100,  tile[1] * tileY]]
                c = [[x * sizeP, y * sizeP], [tile[0] * tileX + 100, tile[1] * tileY + 100]]
                d = [[x * sizeP, y * sizeP],       [tile[0] * tileX, tile[1] * tileY + 100]]

                PeA = (a[1][0] * vectors[tile[1]]  [tile[0]]  [1][0]) + (a[1][1] * vectors[tile[1]]  [tile[0]]  [1][1])
                PeB = (b[1][0] * vectors[tile[1]]  [tile[0]+1][1][0]) + (b[1][1] * vectors[tile[1]]  [tile[0]+1][1][1])
                PeC = (c[1][0] * vectors[tile[1]+1][tile[0]+1][1][0]) + (c[1][1] * vectors[tile[1]+1][tile[0]+1][1][1])
                PeD = (d[1][0] * vectors[tile[1]+1][tile[0]]  [1][0]) + (d[1][1] * vectors[tile[1]+1][tile[0]]  [1][1])

                color = media(PeA, PeB, PeC, PeD)
                color = 100 if color > 34248 else 255
                
                print (np.array([PeA,PeB,PeC,PeD]))

                # pygame.draw.line(SCREEN, BLUE, a[0], a[1])
                # pygame.draw.line(SCREEN, BLUE, b[0], b[1])
                # pygame.draw.line(SCREEN, BLUE, c[0], c[1])
                # pygame.draw.line(SCREEN, BLUE, d[0], d[1])

                # color = random.randint(0, 200)
                pygame.draw.rect(SCREEN,
                                [color, color, color],
                                [x*sizeP, y*sizeP, x*sizeP+sizeP, y*sizeP+sizeP]) 

        for x in range(int((HEIGHT / tileX)+1)):
            for y in range(int((WIDTH / tileY)+1)):
                pygame.draw.line(SCREEN, GREEN, [vectors[x][y][0][0], vectors[x][y][0][1]], [vectors[x][y][1][0], vectors[x][y][1][1]])
            
                pygame.draw.rect(SCREEN, RED, 
                               [y*tileY, x*tileX, y*tileY+tileY+1, x*tileX+tileX+1], 1)

        pygame.display.update()
    

if __name__ == '__main__':
    print('em execução')
    main()
    # print(vectors)
