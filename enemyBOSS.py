import pygame
from random import *
class Boss(pygame.sprite.Sprite):
    blood = 10000
    def __init__(self,ruler):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("pic/Dboss1.png").convert_alpha()
        self.image2 = pygame.image.load("pic/Dboss2.png").convert_alpha()
        self.image3 = pygame.image.load("pic/Dboss3.png").convert_alpha()
        # self.destroy_images = []
        # self.destroy.extend([pygame.image.load().convert_alpha])
        self.rect = self.image1.get_rect()
        self.width,self.height = ruler[0],ruler[1]
        self.rect.left,self.rect.top = (self.width -self.rect.width)//2,10
        self.speed =1
        self.speedx = 1
        self.speedy = 1
        self.blood = Boss.blood
        self.mask = pygame.mask.from_surface(self.image1)
        self.life = True
    def Bmove(self):
        if self.life == True:
            self.rect=self.rect.move(self.speed,0)
            if self.rect.left<0 or self.rect.right>self.width:
                self.speed=-self.speed
    def Bmove1(self):
            self.rect=self.rect.move(self.speedx,self.speedy)
            if self.rect.left<0 or self.rect.right>self.width:
                self.speedx=-self.speedx
            if self.rect.top<0 or self.rect.bottom>self.height:
                self.speedy=-self.speedy

        