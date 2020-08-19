# working through https://opensource.com/article/17/12/game-framework-python
import sys
import os
import pygame



'''
Objects
'''

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.images = []
        for i in range(1, 4):
            img = pygame.image.load(os.path.join('images', ('player' + str(i) + '.png')))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        
    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        if self.movex > 0:
            self.frame += 1
            if self.frame > 4:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        self.rect.y = self.rect.y + self.movey
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, move_dist, speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.move_dist = move_dist
        self.speed = speed
    
    def move(self):

        distance = self.move_dist
        speed = self.speed

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance *2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

class Level():

    def bad(self, level):
        if level == 1:
            print("Level " + str(level))
            enemy1 = Enemy(200, 20, 80, 8, 'yeti.png')
            enemy2 = Enemy(100, 100, 60, 10, 'yeti.png')
            enemy3 = Enemy(5, 100, 10, 1, 'yeti.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy1)
            enemy_list.add(enemy2)
            enemy_list.add(enemy3)
        if level == 2:
            print("Level " + str(level))
        return enemy_list

    
'''
Setup
'''

worldx = 960
worldy = 720

fps = 10
ani = 4
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #pixel movement speed

current_level = Level()
enemy_list = current_level.bad(1)

'''
Main Loop
'''
main = True

while main == True:
    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    enemy_list.draw(world)
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
                print(player.frame)
                print('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
                print(player.frame)
                print('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
                print('right stop')
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False 