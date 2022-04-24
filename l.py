from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()        
        self.image = transform.scale(image.load(player_image),(50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self. image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
            window = display.set_mode((700, 500))

window = display.set_mode((500, 247))
display.set_caption('Лабиринт')
background = transform.scale(image.load('doramap.png'),(500, 247))
clock = time.Clock()
FPS = 160
game = True
finish = False



while game:   
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.reset()
        player.update()

    clock.tick(FPS)
    display.update()
        
