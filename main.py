# working through https://opensource.com/article/17/12/game-framework-python
import sys
import os
import pygame



'''
Objects
'''

# put Python classes and functions here

'''
Setup
'''

worldx = 960
worldy = 720

fps = 40
ani = 4
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

'''
Main Loop
'''
main = True

while main == True:
    world.blit(backdrop, backdropbox)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
    pygame.display.flip()
    clock.tick(fps)