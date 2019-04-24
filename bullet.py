import pygame
'''
这是我之前写的玩家子弹
class Bullet1(pygame.sprite.Sprite):
    def __init__(self,weizhi):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("pic/zidan0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = weizhi
        self.speed = 12
        self.touches = True
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        self.rect.top = self.rect.top - self.speed

        if self.rect.top<0:
            self.touches = False
    def reset(self,weizhi):
        self.rect.left , self.rect.top = weizhi
        self.touches = True
'''

class Bullet2(pygame.sprite.Sprite):
    def __init__(self,weizhi):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pic/bdan.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = weizhi
        self.speedx = 6
        self.speedy = 1
        self.touches = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.left , self.rect.top = self.rect.left - self.speedx , self.rect.top + self.speedy
        if self.rect.left < 0 or self.rect.left > 600:
            self.speedx = -self.speedx
        if self.rect.top<0:
            self.touches = False
    def reset(self,weizhi):
        self.rect.left , self.rect.top = weizhi
        self.touches = True
class Bullet3(pygame.sprite.Sprite):
    def __init__(self,weizhi):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("pic/jiguang8.png").convert_alpha()
        # self.image2 = pygame.image.load("pic/jiguang1.png").convert_alpha()
        self.image3 = pygame.image.load("pic/jiguang9.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.rect.left , self.rect.top = weizhi
        self.touches = True
        self.speed1 = 1
        self.mask = pygame.mask.from_surface(self.image1)
    def move(self,weizhi):
        self.rect.left , self.rect.top = weizhi
class Bullet4(pygame.sprite.Sprite):
    def __init__(self,weizhi):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pic/sandan.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = weizhi
        self.touches = True
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
    def move1(self):
        self.rect=self.rect.move(0,2)
    def move2(self):
        self.rect=self.rect.move(0,-2)
    def move3(self):
        self.rect=self.rect.move(-2,0)
    def move4(self):
        self.rect=self.rect.move(2,0)
    def move5(self):
        self.rect=self.rect.move(2,2)
    def move6(self):
        self.rect=self.rect.move(-2,-2)
    def move7(self):
        self.rect=self.rect.move(-2,2)
    def move8(self):
        self.rect=self.rect.move(2,-2)
    def reset(self,weizhi):
        self.rect.left , self.rect.top = weizhi