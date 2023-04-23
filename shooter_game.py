from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption('АРТЕМЙ АТАКУЕТ!!!!???!?!???!!!')


background = transform.scale(image.load('galaxy.jpg'), (700, 500))





class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (gs_x, gs_y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__(pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y)
    
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed




class Enemy(GameSprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__(pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 490:
            self.rect.x = randint(80, 700-80)
            self.rect.y = 0
    def tp(self):
        self.rect.y = 0
        self.rect.x = randint(80, 620)



class Bullet(GameSprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y):
        super().__init__(pl_image, pl_x, pl_y, pl_speed, gs_x, gs_y)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > 500:
            self.kill()
            



bullets = sprite.Group()


monsters = sprite.Group()
for i in range(4):
    monsters.add(Enemy('ufo.png', randint(0, 600), randint(-55, 25), 2, 65, 45))









rocket = Player('rocket.png', 315, 395, 3, 60, 90)



game = True
while game:
    window.blit(background,(0, 0))
    rocket.update()
    rocket.reset()

    key_pressed = key.get_pressed()
    if key_pressed[K_UP]:
        bullet = Bullet('bullet.png', rocket.rect.centerx, rocket.rect.top, 5, 20, 30)
        bullets.add(bullet)
    bullets.update()
    bullets.draw(window)
    monsters.update()
    monsters.draw(window)



    for e in event.get():
        if e.type == QUIT:
            game = False

    spisok = sprite.groupcollide(monsters, bullets, False, True)
    if spisok:
        for i in spisok:
            i.tp()



    display.update()