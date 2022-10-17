import pygame
import random
import math
from pygame.locals import *

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

                PeA = a[1][0] * (vectors[tile[1]][tile[0]][1][0] + a[1][0]) * (vectors[tile[1]][tile[0]][1][1] + a[1][0])
                PeB = b[1][0] * (vectors[tile[1]][tile[0]+1][1][0] + b[1][0]) * (vectors[tile[1]][tile[0]+1][1][1] + b[1][0])
                PeC = c[1][0] * (vectors[tile[1]+1][tile[0]+1][1][0] + c[1][0]) * (vectors[tile[1]+1][tile[0]+1][1][1] + c[1][0])
                PeD = d[1][0] * (vectors[tile[1]+1][tile[0]][1][0] + d[1][0]) * (vectors[tile[1]+1][tile[0]][1][1] + d[1][0])

                color = media(PeA, PeB, PeC, PeD)
                color = 100 if color > 2000000 else 255
                 

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
    print(vectors)

[[[[0, 0], [61, 78]], [[0, 100], [99, 99]], [[0, 200], [-100, 183]], [[0, 300], [20, 397]], [[0, 400], [89, 355]], [[0, 500], [-100, 511]], [[0, 600], [41, 690]]],
 [[[100, 0], [85, -100]], [[100, 100], [27, 168]], [[100, 200], [123, 296]], [[100, 300], [197, 320]], [[100, 400], [42, 481]], [[100, 500], [146, 587]], [[100, 600], [24, 533]]], 
 [[[200, 0], [175, 96]], [[200, 100], [154, 188]], [[200, 200], [106, 235]], [[200, 300], [112, 349]], [[200, 400], [289, 355]], [[200, 500], [185, 400]], [[200, 600], [145, 683]]],
 [[[300, 0], [304, 99]], [[300, 100], [202, 121]], [[300, 200], [247, 113]], [[300, 300], [347, 212]], [[300, 400], [383, 345]], [[300, 500], [321, 402]], [[300, 600], [297, 699]]],
 [[[400, 0], [496, 25]], [[400, 100], [490, 57]], [[400, 200], [491, 238]], [[400, 300], [449, 212]], [[400, 400], [302, 375]], [[400, 500], [375, 402]], [[400, 600], [309, 643]]], 
 [[[500, 0], [599, -6]], [[500, 100], [411, 52]], [[500, 200], [573, 132]], [[500, 300], [475, 396]], [[500, 400], [513, 300]], [[500, 500], [414, 552]], [[500, 600], [586, 549]]], 
 [[[600, 0], [646, 87]], [[600, 100], [693, 133]], [[600, 200], [587, 100]], [[600, 300], [580, 201]], [[600, 400], [578, 301]], [[600, 500], [499, 501]], [[600, 600], [517, 656]]]]