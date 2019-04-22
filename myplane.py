#-*-coding:utf-8-*-
"""
   个人尝试pygame第一个游戏
"""
import pygame,sys
from pygame.locals import *
import enemyBOSS
import bullet
from random import *
pygame.init()
ruler = wigth,height =600,800
bg_one = "F:\muyun_project\pic/fillgroud.png"
screen = pygame.display.set_mode(ruler)
title = pygame.display.set_caption("Planwar")
bg_zero = pygame.image.load(bg_one)
red = (255,0,0)
black = (0,0,0)
kind = True

#生成boss
xBoss = enemyBOSS.Boss(ruler)
weizhi3 = xBoss.rect.center
#生成子弹
#boss一型子弹
bullet2 = []
bullet2_index = 0
BULLET2_NUM = 100
for en in range(BULLET2_NUM):
    bullet2.append(bullet.Bullet2(xBoss.rect.midbottom))

#生成boss散弹
sandan1 = []
sandan1_index = 0
sandan1_NUM = 4
for en in range(sandan1_NUM):
    sandan1.append(bullet.Bullet4(weizhi3))
sandan2 = []
sandan2_index = 0
sandan2_NUM = 4
for en in range(sandan2_NUM):
    sandan2.append(bullet.Bullet4(weizhi3))
sandan3 = []
sandan3_index = 0
sandan3_NUM = 4
for en in range(sandan3_NUM):
    sandan3.append(bullet.Bullet4(weizhi3))
sandan4 = []
sandan4_index = 0
sandan4_NUM = 4
for en in range(sandan4_NUM):
    sandan4.append(bullet.Bullet4(weizhi3))
sandan5 = []
sandan5_index = 0
sandan5_NUM = 4
for en in range(sandan5_NUM):
    sandan5.append(bullet.Bullet4(weizhi3))
sandan6 = []
sandan6_index = 0
sandan6_NUM = 4
for en in range(sandan6_NUM):
    sandan6.append(bullet.Bullet4(weizhi3))
sandan7 = []
sandan7_index = 0
sandan7_NUM = 4
for en in range(sandan7_NUM):
    sandan7.append(bullet.Bullet4(weizhi3))
sandan8 = []
sandan8_index = 0
sandan8_NUM = 4
for en in range(sandan8_NUM):
    sandan8.append(bullet.Bullet4(weizhi3))

#激光炮
weizhi1 = xBoss.rect.left + 180,xBoss.rect.top + 160
jiguang1 = bullet.Bullet3(weizhi1)
weizhi2 = xBoss.rect.left - 20,xBoss.rect.top + 160
jiguang2 = bullet.Bullet3(weizhi2)

clock = pygame.time.Clock()
change = False

#用于延迟播放
delay = 100

while True:
    
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
    
    
   #boss绘制
   screen.blit(bg_zero,(0,0))

   #发射子弹
   if not(delay % 10):
      bullet2[bullet2_index].reset(xBoss.rect.midbottom)
      bullet2_index = (bullet2_index + 1) % BULLET2_NUM
   
   if delay%900 == 0:
      kind = not kind
   
   
   if xBoss.blood>220:
      if kind == True:
         for b in bullet2:
               if b.touches:
                  b.move()
                  screen.blit(b.image, b.rect)
      else:
         for b in bullet2:
               b.reset(xBoss.rect.midbottom)
         weizhi1 = xBoss.rect.left + 180,xBoss.rect.top + 160
         jiguang1.move(weizhi1)
         if not(delay%20):
               screen.blit(jiguang1.image1,jiguang1.rect)
         else:
               screen.blit(jiguang1.image3,jiguang1.rect)
         weizhi2 = xBoss.rect.left - 20,xBoss.rect.top + 160
         jiguang2.move(weizhi2)
         if not(delay%20):
               screen.blit(jiguang2.image1,jiguang2.rect)
         else:
               screen.blit(jiguang2.image3,jiguang2.rect)
   else:
      for d in sandan1:
         d.move1()
         screen.blit(d.image,d.rect)
      for d in sandan2:
         d.move2()
         screen.blit(d.image,d.rect)
      for d in sandan3:
         d.move3()
         screen.blit(d.image,d.rect)
      for d in sandan4:
         d.move4()
         screen.blit(d.image,d.rect)
      for d in sandan5:
         d.move5()
         screen.blit(d.image,d.rect)
      for d in sandan6:
         d.move6()
         screen.blit(d.image,d.rect)
      for d in sandan7:
         d.move7()
         screen.blit(d.image,d.rect)
      for d in sandan8:
         d.move8()
         screen.blit(d.image,d.rect)
   weizhi3 = xBoss.rect.center
   if not(delay%60):
      sandan1[sandan1_index].reset(weizhi3)
      sandan1_index = (sandan1_index + 1) % sandan1_NUM
      sandan2[sandan2_index].reset(weizhi3)
      sandan2_index = (sandan2_index + 1) % sandan2_NUM
      sandan3[sandan3_index].reset(weizhi3)
      sandan3_index = (sandan3_index + 1) % sandan3_NUM
      sandan4[sandan4_index].reset(weizhi3)
      sandan4_index = (sandan4_index + 1) % sandan4_NUM
      sandan5[sandan5_index].reset(weizhi3)
      sandan5_index = (sandan5_index + 1) % sandan5_NUM
      sandan6[sandan6_index].reset(weizhi3)
      sandan6_index = (sandan6_index + 1) % sandan6_NUM
      sandan7[sandan7_index].reset(weizhi3)
      sandan7_index = (sandan7_index + 1) % sandan7_NUM
      sandan8[sandan8_index].reset(weizhi3)
      sandan8_index = (sandan8_index + 1) % sandan8_NUM
   
   delay += 1
   #boss血条
   pygame.draw.line(screen,black,(0,0),(600,0),20)
   boss_life = xBoss.blood/enemyBOSS.Boss.blood
   pygame.draw.line(screen,red,(0,0),(600*boss_life,0),20)

   if not(delay%100):
      xBoss.speedx=randint(-2,2)
      xBoss.speedy=randint(-3,2)

   #绘制boss
   if boss_life > 0.7:
      xBoss.Bmove()
      screen.blit(xBoss.image1,xBoss.rect)

   elif boss_life < 0.7 and boss_life > 0.4 or boss_life == 0.4:
      xBoss.Bmove()
      screen.blit(xBoss.image2,xBoss.rect)
      xBoss.mask = pygame.mask.from_surface(xBoss.image3)

   elif boss_life == 0.4 or boss_life < 0.4 and boss_life > 0:
      if change == False:
         xBoss.rect = xBoss.image3.get_rect()
         xBoss.rect.left,xBoss.rect.top = (xBoss.width -xBoss.rect.width)//2,10
         change = True
      xBoss.life = False
      xBoss.Bmove1()
      screen.blit(xBoss.image3,xBoss.rect)

   pygame.display.update()
   clock.tick(60)