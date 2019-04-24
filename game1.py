import pygame,itertools,sys,time,random,math,os
import enemyBOSS,bullet
from pygame.locals import *

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"

#bosss删除
def boss_kill():
    global Boss_time
    if Boss_time == True:
        if jiguang1:
            jiguang1.kill()
        if jiguang2:
            jiguang2.kill()
        for n in bullet2:
            n.reset((800,800))
        Boss_time = False
        xBoss.blood = enemyBOSS.Boss.blood

def paused():
    global Pause
    while Pause:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    Pause = False
        print_text(font, 250, 400, "P A S U E")
        pygame.display.update()
        framerate.tick(5)

def Start_bg_replay():
    Start_music.play_pause()
    Start_music.play_sound()


def audio_init():
    global st_au,main_au,boom_au,zdhh_au,js_au,warning_au
    pygame.mixer.init()
    st_au = pygame.mixer.Sound("music/bg.ogg")
    boom_au = pygame.mixer.Sound("music/boom.ogg")
    zdhh_au = pygame.mixer.Sound("music/player_shoot.ogg")
    js_au = pygame.mixer.Sound("music/gameover.wav")
    warning_au = pygame.mixer.Sound("music/bosswaring1.wav")

class Music():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound
    def play_sound(self):
        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(0.5)
        self.channel.play(self.sound)
    def play_pause(self):
        self.channel.set_volume(0.0)
        self.channel.play(self.sound)

class Music1():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound
    def play_sound(self):
        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(1.0)
        self.channel.play(self.sound)
    def play_pause(self):
        self.channel.set_volume(0.0)
        self.channel.play(self.sound)

'''class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0, 0.0)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 0, 0, width, height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
'''


class MySprite(pygame.sprite.Sprite):

    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)  # 调用父类方法
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0, 0.0)
        self.bullets = pygame.sprite.Group()
        self.dr_group = pygame.sprite.Group()
        self.drzd_group =pygame.sprite.Group()
        self.jydr_group = pygame.sprite.Group()
        self.life = 0
        # X property

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)

    def shoot(self,arrow):
        self.bullets.add(arrow)

    def drupdate(self):
        dr_pos = random.randint(0,530),-70
        dr = dr_feiji(dr_pos,'pt')
        self.dr_group.add(dr)
    def jydrupdate(self):
        jydr = dr_feiji((random.randint(0, 398), -130), 'jy')
        self.jydr_group.add(jydr)

def calc_velocity(Kw,Kd,Ks,Ka, vel=1.0):
    velocity = Point(0,0)
    if Kw == 1:  #上
        velocity.y = -vel
        if Ka == 1:
            velocity.x = -vel
        if Kd == 1:
            velocity.x = vel
    elif Kd == 1:  #右
        velocity.x = vel
        if Kw == 1:
            velocity.y = -vel
        if Ks == 1:
            velocity.y = vel
    elif Ks == 1:  #下
        velocity.y = vel
        if Ka == 1:
            velocity.x = -vel
        if Kd == 1:
            velocity.x = vel
    elif Ka == 1:  #左
        velocity.x = -vel
        if Kw == 1:
            velocity.y = -vel
        if Ks == 1:
            velocity.y = vel
    return velocity

#地图类
class MyMap(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bg = pygame.image.load("chap04/blackroom1.png").convert_alpha()

    def map_rolling(self):
        if self.y > 800:
            self.y = -800
        else:
            self.y += 0.5

    def map_update(self):
        screen.blit(self.bg, (self.x, self.y))

    def set_pos(self,x, y):
        self.x = x
        self.y = y


# 子弹类，继承自Sprite类
class Bullet(pygame.sprite.Sprite):
    def __init__(self,zidan_pos,zdlx,zydx):#zydx = 作用对象
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)
        # 设置属性
        if zdlx == 'player':
            self.image = pygame.image.load("chap04/playzidan.png").subsurface(pygame.Rect(0, 0, 42, 50))  # image属性：子弹图片
            self.speed_y = 20  # speed属性：子弹移动速度
            self.zdgjl = 100 #子弹攻击力
        elif zdlx == 'drfeiji':
            self.image = pygame.image.load("chap04/drzd_01.png").subsurface(pygame.Rect(0, 0, 15, 15))    # image属性：子弹图片
            self.speed_y = random.randint(-4,-2)  # speed属性：子弹Y轴移动速度
            self.speed_x = 1    # speed属性：子弹X轴移动速度
        self.rect = self.image.get_rect()  # rect属性：矩形
        self.rect.topleft = zidan_pos  # 矩形左上角坐标
        self.zydx = zydx
        self.zdlx = zdlx
        self.zdscwz_x, self.zdscwz_y = zidan_pos
        self.player_x = player.X
        self.zdhh_music = Music(zdhh_au)
    # 移动方法
    def update(self):
        global Boss_time
        # 修改子弹坐标
        if self.zdlx == 'drfeiji':
            if self.zdscwz_x<self.player_x:
                self.rect.top -= self.speed_y
                self.rect.left += self.speed_x
            elif self.zdscwz_x>self.player_x:
                self.rect.top -= self.speed_y
                self.rect.left -= self.speed_x
            else:
                self.rect.top -= self.speed_y
        elif self.zdlx == 'player':
            self.rect.top -= self.speed_y
        # 如果子弹移出屏幕上方，右方，左方，则销毁子弹对象
        if self.rect.top < -10 or self.rect.left >610 or self.rect.left<-10:
            self.kill()
        wjbjz = pygame.sprite.spritecollideany(player, drfeiji.drzd_group) #玩家被击中时给wjbjz赋值
        if wjbjz :
            if pygame.sprite.collide_circle_ratio(0.5)(player, wjbjz):
                player.life-=10
                drfeiji.drzd_group.remove(wjbjz)

        if Boss_time == True:
            boss_player_zdpz = pygame.sprite.spritecollideany(xBoss,playerzidan.bullets)
            if boss_player_zdpz:
                for n in playerzidan.bullets:
                    if pygame.sprite.collide_mask(xBoss,n):
                        xBoss.blood-=20
                        n.kill()

    def __del__(self):
        if self.zydx == 'drfeiji':
            if self.rect.top >= -10:
                player_zdhh = NewBoom()
                player_zdhh.load("chap04/player_zdhh.png", 40, 40, 4)
                player_zdhh.position = self.rect.left, self.rect.top
                player_zdhh_group.add(player_zdhh)
                self.zdhh_music.play_sound()

# 敌机类，继承自Sprite类
class dr_feiji(pygame.sprite.Sprite):
    def __init__(self,dr_pos,drlx):#drlx敌人类型
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)
        # 设置属性
        if drlx =='jy':
            self.image = pygame.image.load("chap04/jydr-01.png").subsurface(pygame.Rect(0, 0, 202, 130))  # image属性：飞机图片
            self.dr_life = 4000
        if drlx == 'pt':
            self.image = pygame.image.load("chap04/dr-01.png").subsurface(pygame.Rect(0, 0, 70, 70))  # image属性：飞机图片
        self.rect = self.image.get_rect()  # rect属性：矩形
        self.rect.topleft = dr_pos  # 矩形左上角坐标
        self.speed_y = random.randint(2,4)  # speed属性：敌人y轴移动速度
        self.speed_x = random.randint(1,3)  # speed属性：敌人x轴移动速度
        self.drms_sj = random.randint(1,3)#敌人行动模式随机
        self.drzd_group = pygame.sprite.Group() #敌人子弹精灵组
        self.drlx = drlx

    # 移动方法
    def update(self):
        # 修改敌人坐标
        global player_score
        if self.drlx == 'pt':
            if self.drms_sj == 1:
                self.rect.top += self.speed_y
            elif self.drms_sj == 2:
                self.rect.left += self.speed_x
                self.rect.top += self.speed_y * 1.5
            elif self.drms_sj == 3:
                self.rect.left += self.speed_x
                self.rect.top += 0.5 * self.speed_y
            # 如果敌人移出屏幕下方，则销毁敌人对象
            if self.rect.top > 800:
                self.kill()
            if self.rect.left > 530:
                self.speed_x = -self.speed_x
            elif self.rect.left < 0:
                self.speed_x = -self.speed_x
        elif self.drlx == 'jy':
            if self.drms_sj == 1:
                if self.rect.top < 300:
                    self.rect.top += self.speed_y
            elif self.drms_sj == 2:
                self.rect.left += self.speed_x
                if self.rect.top < 300:
                    self.rect.top += self.speed_y * 1.5
            elif self.drms_sj == 3:
                self.rect.left += self.speed_x
                if self.rect.top < 300:
                    self.rect.top += 0.5 * self.speed_y
            # 如果敌人移出屏幕下方，则销毁敌人对象
            if self.rect.top > 800:
                self.kill()
            if self.rect.left > 398:
                self.speed_x = -self.speed_x
            elif self.rect.left < 0:
                self.speed_x = -self.speed_x

        drpzzd = pygame.sprite.groupcollide(drfeiji.dr_group,playerzidan.bullets,False,False) #敌人碰到子弹
        if drpzzd:
            for n in drfeiji.dr_group:
                for m in playerzidan.bullets:
                    if pygame.sprite.collide_mask(n,m):
                        n.kill()
                        m.kill()

        jydrpzzd = pygame.sprite.groupcollide(jydrfeiji.jydr_group,playerzidan.bullets,False,False) #敌人碰到子弹
        if jydrpzzd:
            for n in jydrfeiji.jydr_group:
                for m in playerzidan.bullets:
                    if pygame.sprite.collide_mask(n,m):
                        m.kill()
                        n.dr_life-=100


        if self.drlx=='jy':
            if self.dr_life<=0:
                jydrboom.position = self.rect.left, self.rect.top
                jydr_boom_group.add(jydrboom)
                dr_cxwq = random.randint(0, 100)  # 敌人被击破时出现武器的几率
                if dr_cxwq < 20:
                    playerwq = player_wq((self.rect.left, self.rect.top))
                    player_wq_group.add(playerwq)
                if self.rect.top < 800:
                    player_score += 300
                self.dr_boom_music = Music1(boom_au)
                self.dr_boom_music.play_sound()
                self.kill()



        wjboom = pygame.sprite.spritecollideany(player,drfeiji.dr_group)
        if wjboom:
            if pygame.sprite.collide_circle_ratio(0.5)(player, wjboom):
                player.life-=10
                drfeiji.dr_group.remove(wjboom)


        if drzdjg % 100 ==10:
            if self.drlx == 'pt':
                drzd = Bullet((self.rect.left + 26, self.rect.top + 70), 'drfeiji','player')
                drfeiji.drzd_group.add(drzd)
            if self.drlx == 'jy':
                drzd = Bullet((self.rect.left + 26, self.rect.top + 70), 'drfeiji', 'player')
                drzd1 = Bullet((self.rect.left + 146, self.rect.top + 70), 'drfeiji', 'player')
                drfeiji.drzd_group.add(drzd)
                drfeiji.drzd_group.add(drzd1)

    def __del__(self):
        global player_score

        if self.drlx == 'pt':
            boom_x = self.rect.left
            boom_y = self.rect.top
            drboom = NewBoom()
            drboom.load("chap04/boom.png", 70, 70, 6)
            drboom.position = boom_x, boom_y
            drboom_group.add(drboom)
            if self.rect.top < 800:
                player_score += 100
            dr_cxwq = random.randint(0,100) #敌人被击破时出现武器的几率
            if dr_cxwq<10:
                playerwq = player_wq((self.rect.left,self.rect.top))
                player_wq_group.add(playerwq)
            self.dr_boom_music = Music1(boom_au)
            self.dr_boom_music.play_sound()
#玩家炸弹类
class player_zhadan(pygame.sprite.Sprite):
    def __init__(self,player_x,player_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("chap04/player_zhadan_01.png").convert_alpha()
        self.max_y = player_y-200
        self.rect = self.image.get_rect()
        self.rect.topleft = player_x+40,player_y

    def update(self):
        zhadan_weiqi.position = self.rect.left + 3, self.rect.top + 70
        if self.rect.top > self.max_y:
            self.rect.top-=3
        else:
            self.kill()
            zhadan_weiqi.kill()
            zhadanboom.position = self.rect.left-188 ,self.rect.top-200
            player_zhadan_boom_group.add(zhadanboom)



        '''        boom_x = self.rect.left-100
        boom_y = self.rect.top-100
        zhadan_boom = NewBoom(screen)
        zhadan_boom.load("chap04/zhadan_boom/player_zhadan_boom.png", 300, 300, 7)
        zhadan_boom.position = boom_x,boom_y
        player_zhadan_boom_group.add(zhadan_boom)'''

# 爆炸精灵类，继承自Sprite类
class NewBoom(pygame.sprite.Sprite):
    def __init__(self):
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)
        # 设置属性
        self.master_image = None #爆炸图片
        self.frame = 0      #当前帧
        self.old_frame = -1     #上一帧
        self.frame_width = 1    #帧宽度
        self.frame_height = 1   #帧高度
        self.first_frame = 0    #第一帧
        self.last_frame = 0     #最后一帧
        self.columns = 1        #图片列数
        self.last_time = 0      #循环一次的时间

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self,bzdx, current_time, rate=30):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
                if bzdx=='dr' or bzdx=='zidan' or bzdx=='player':
                    self.kill()
            self.last_time = current_time

        #
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame


    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)




# 尾气类，继承自Sprite类
class Weiqi(pygame.sprite.Sprite):
    def __init__(self):
        # 调用父类的构造方法
        pygame.sprite.Sprite.__init__(self)
        # 设置属性
        self.master_image = None #爆炸图片
        self.frame = 0      #当前帧
        self.old_frame = -1     #上一帧
        self.frame_width = 1    #帧宽度
        self.frame_height = 1   #帧高度
        self.first_frame = 0    #第一帧
        self.last_frame = 0     #最后一帧
        self.columns = 1        #图片列数
        self.last_time = 0      #循环一次的时间

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

class player_wq(pygame.sprite.Sprite):
    def __init__(self,drboom_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("chap04/player_wq.png").convert_alpha()
        self.rect = Rect(0,0,50,52)
        self.player_wq_speed_x = 2
        self.player_wq_speed_y = 2
        self.time = 0
        self.rect.topleft = drboom_pos
    def update(self):
        global player_wq_level
        global player_threewq_time
        if self.time > 1000:
            player_wq_group.remove(self)
        self.rect.top+=self.player_wq_speed_y
        self.rect.left+=self.player_wq_speed_x

        if self.rect.top<-50:
            self.player_wq_speed_y = -self.player_wq_speed_y
        elif self.rect.top>748:
            self.player_wq_speed_y = -self.player_wq_speed_y
        elif self.rect.left<0:
            self.player_wq_speed_x = -self.player_wq_speed_x
        elif self.rect.left>550:
            self.player_wq_speed_x = -self.player_wq_speed_x
        self.time +=1

        wqsjpz = pygame.sprite.spritecollideany(player,player_wq_group) #玩家碰到武器升级材料
        if wqsjpz:
            for n in player_wq_group:
                if pygame.sprite.collide_mask(n,player):
                    player_wq_group.remove(n)
                    if player_wq_level<3:
                        player_wq_level+=1
                    player_threewq_time=100


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x,y))

def print_chtext(font, x, y, text, color=(255,255,255)):
    font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf",20)
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x,y))

def print_bosstext(font, x, y, text, color=(255,0,0)):
    font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf",30)
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x,y))
pygame.init()
audio_init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("飞机大战")
font = pygame.font.Font(None, 36)
framerate = pygame.time.Clock()

#BOSS载入
ruler = wigth,height =600,800
red = (255,0,0)
black = (0,0,0)
kind = True

#boss出现时的警告
boss_cx_music = Music1(warning_au)
boss_cx_music_time = 0
boss_cx_music_flag = False

#游戏开始界面图片
Start_image = pygame.image.load("chap04/Gameblackgroud.png").convert_alpha()
#开始界面声音
Start_music = Music(st_au)
Start_music.play_sound()

#游戏时的背景音乐
main_bg_music = pygame.mixer.music
main_bg_music.load("music/Rockman3.ogg")
main_bg_music.set_volume(0.8)
main_bg_music_time = 0
main_bg_music_cs = True

#游戏结束时的背景音乐
gameover_music = Music1(js_au)
gameover_music_time = 0
gameover_js = 0


#精灵组
player_group = pygame.sprite.Group()
drboom_group = pygame.sprite.Group()
playerboom_group = pygame.sprite.Group()
player_zdhh_group = pygame.sprite.Group()#玩家子弹击中效果精灵组
player_zhadan_group = pygame.sprite.Group()
zhadan_weiqi_group = pygame.sprite.Group()
player_zhadan_boom_group = pygame.sprite.Group()
jydr_boom_group = pygame.sprite.Group()
player_wq_group = pygame.sprite.Group()

#初始化玩家精灵
player = MySprite(screen)
player.load("chap04/feijif.png", 100,100, 5)
player.position = 250,600
player.life = 100
player_group.add(player)
vel = 5.0
Kw=Ks=Ka=Kd=0
player_boom_music = Music(boom_au)
#玩家武器精灵

#初始化地图
bg1 = MyMap(0,0)
bg2 = MyMap(0,800)
player_moving = False
#敌人爆炸
drboom = NewBoom()
drboom.load("chap04/boom.png", 70, 70, 6)
jydrboom = NewBoom()
jydrboom.load("chap04/jydr-01_boom.png", 210, 130, 6)
#玩家爆炸
playerboom = NewBoom()
playerboom.load("chap04/player_boom.png", 100, 100, 6)
playerboomjs = False
#玩家炸弹爆炸
player_zhadan_ico = pygame.image.load("chap04/player_zhadan_ico.png").convert_alpha()
zhadanboom = NewBoom()
zhadanboom.load("chap04/zhadan_boom/player_zhadan_boom.png", 400, 400, 7)
player_zhadan_num = 5
#敌人精灵
drfeiji = MySprite(screen)
jydrfeiji = MySprite(screen)
#子弹精灵
playerzidan = MySprite(screen)
#子弹间隔
zidanjg = 0
#爆炸事件
boomtime = 0
#敌人间隔
drjg=0
#敌人出现间隔
drupdate_time = 100
#敌人子弹间隔
drzdjg=0
#字体显示间隔
ztxsjg=0
#炸弹爆炸时间
zhadantime = 0
#玩家炸弹是否存在
zhadancz = False
#炸弹爆炸次数
zhadanboomcs=4*4
zhadanboomcs_old = zhadanboomcs
old_zhadanboom_frame = zhadanboom.frame
#玩家分数
player_score = 0
#玩家武器等级
player_wq_level = 1
#3级武器持续时间
player_threewq_time = 100
#玩家和敌人的攻击持续碰撞间隔：
player_jydr_cxpz_time = 0
player_boss_cxpz_time = 0
player_boss_jgcxpz_time1 = 0
player_boss_jgcxpz_time2 = 0
boss_zhadan_cxpz_time = 0

boss_bg_music_time = 0
boss_bg_music_cs = True
boss_bg_music_playone = False

player_win = False
GameOver = False
GameStart =False
Pause = False
bg_replay_flag = True
main_bg_replay_flag = True
boss_bg_replay_flag = True
Boss_time = False
boss_cz = False
change = False
xBoss_kill = False


delay = 100
while True:
    if GameStart ==True:
        if GameOver == False:
            framerate.tick(60)
            ticks = pygame.time.get_ticks()
            zidanjg+=1
            drjg+=1
            drzdjg+=1
            zhadantime+=1
            if drzdjg == 400:
                drzdjg=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j and zhadancz == False and player_zhadan_num > 0:
                        bzjydr = None
                        playerzhadan = player_zhadan(player.X, player.Y)
                        zhadan_weiqi = Weiqi()
                        zhadan_weiqi.load("chap04/zhadan/player_zhadan_weiqi.png", 15, 30, 2)
                        zhadan_weiqi_group.add(zhadan_weiqi)
                        player_zhadan_group.add(playerzhadan)
                        zhadancz = True
                        zhadantime = 1
                        player_zhadan_num -= 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sys.exit()
            elif keys[K_w]:
                Kw=1
                player_moving = True
                if keys[K_a]:
                    Ka=1
                    Kw=1
                elif keys[K_d]:
                    Kd=1
                    Kw=1
            elif keys[K_s]:
                Ks=1
                player_moving = True
                if keys[K_a]:
                    Ka=1
                    Ks=1
                elif keys[K_d]:
                    Kd=1
                    Ks=1
            elif keys[K_a]:
                Ka=1
                player_moving = True
                if keys[K_w]:
                    Kw=1
                    Ka=1
                elif keys[K_s]:
                    Ks=1
                    Ka=1
            elif keys[K_d]:
                Kd=1
                player_moving = True
                if keys[K_w]:
                    Kw=1
                    Kd=1
                elif keys[K_s]:
                    Ks=1
                    Kd=1
            elif keys[K_F3]:
                Pause = True
            else:
                player_moving = False

            if Pause:
                paused()

            if Kw==1 or Ks==1:
                if Kd == 1:
                    player.first_frame = 0
                    player.last_frame = 1
                    if player.frame == player.last_frame:
                        player.first_frame = 1
                elif Ka == 1:
                    player.first_frame = 3
                    player.last_frame = 4
                    if player.frame == player.last_frame:
                         player.first_frame = 4
                else:
                    player.first_frame = player.last_frame = 2
            elif Kd==1:
                player.first_frame=0
                player.last_frame=1
                if player.frame == player.last_frame:
                    player.first_frame = 1
            elif Ka==1:
                player.first_frame =3
                player.last_frame = 4
                if player.frame == player.last_frame:
                    player.first_frame = 4

            if not player_moving:
                # 当停止按键（即人物停止移动的时候），停止更新动画帧
                player.last_frame = player.first_frame = 2
            else:
                player.velocity = calc_velocity(Kw,Kd,Ks,Ka,5.0)
                player.velocity.x *= 1.5
                player.velocity.y *= 1.5
                Kw = 0
                Ks = 0
                Ka = 0
                Kd = 0

            #绘制地图
            bg1.map_update()
            bg2.map_update()
            bg1.map_rolling()
            bg2.map_rolling()

            player_group.update(ticks,50)
            # 移动玩家
            if player_moving:
                player.X += player.velocity.x
                player.Y += player.velocity.y
                if player.X < 0:
                    player.X = 0
                elif player.X > 500:
                    player.X = 500
                if player.Y < 0:
                    player.Y = 0
                elif player.Y > 700:
                    player.Y = 700

            if zidanjg % 10 == 0:
                if player_wq_level == 1:
                    zidan_pos = player.X + 30, player.Y - 30
                    arrow = Bullet(zidan_pos,'player','drfeiji')
                    playerzidan.shoot(arrow)
                if player_wq_level >= 2 and player_wq_level<3:
                    arrow = Bullet((player.X+20,player.Y-30),'player','drfeiji')
                    arrow1 = Bullet((player.X+40,player.Y-30),'player','drfeiji')
                    playerzidan.shoot(arrow)
                    playerzidan.shoot(arrow1)
                if player_wq_level == 3:
                    arrow = Bullet((player.X-10,player.Y-15),'player','drfeiji')
                    arrow1 = Bullet((player.X+30,player.Y-30),'player','drfeiji')
                    arrow2 = Bullet((player.X+70, player.Y - 15), 'player', 'drfeiji')
                    playerzidan.shoot(arrow)
                    playerzidan.shoot(arrow1)
                    playerzidan.shoot(arrow2)
                    player_threewq_time -= 1
                if player_threewq_time == 0:
                    player_wq_level = 2
                    player_threewq_time = 100
                # 子弹移动
            playerzidan.bullets.update()  # 精灵组update时，会调用所有精灵的update方法

            if zhadantime % 180 == 0:
                zhadancz = False


            if Boss_time == False:
                if drjg % drupdate_time ==0:
                    drfeiji.drupdate()
                    #生成敌机
                if drjg % (drupdate_time*5) == 0 and player_score > 500:
                    jydrfeiji.jydrupdate()

            #玩家碰到敌人
            #1.精英
            if pygame.sprite.spritecollideany(player,jydrfeiji.jydr_group):
                for n in jydrfeiji.jydr_group:
                    if pygame.sprite.collide_mask(player,n):
                        if player_jydr_cxpz_time % 60 == 0:
                            player.life-=10
                        player_jydr_cxpz_time += 1
            else:
                player_jydr_cxpz_time=0




            #重置炸弹爆炸次数
            if zhadanboomcs != 0 and zhadanboom.frame==zhadanboom.last_frame:
                zhadanboom.first_frame = 0
                zhadanboom.last_frame=6
                zhadanboomcs -=1
            elif zhadanboomcs==0:
                zhadanboom.kill()
                zhadanboomcs=zhadanboomcs_old
                bzdr = bzdrzd = bzjydr = bzbosspz =  None
                boss_zhadan_cxpz_time = 0


            if zhadanboom.frame!=old_zhadanboom_frame:
                bzdr = pygame.sprite.spritecollideany(zhadanboom, drfeiji.dr_group)
                if bzdr:
                    if pygame.sprite.collide_circle_ratio(0.9)(zhadanboom, bzdr):
                        drfeiji.dr_group.remove(bzdr)
                bzdrzd = pygame.sprite.spritecollideany(zhadanboom, drfeiji.drzd_group)
                if bzdrzd:
                    if pygame.sprite.collide_circle_ratio(0.9)(zhadanboom, bzdrzd):
                        drfeiji.drzd_group.remove(bzdrzd)
                bzjydr = pygame.sprite.spritecollideany(zhadanboom, jydrfeiji.jydr_group)
                if bzjydr:
                    for n in jydrfeiji.jydr_group:
                        if pygame.sprite.collide_mask(zhadanboom,n):
                            n.dr_life-=2100
                if Boss_time == True:
                    bzbosspz = pygame.sprite.collide_mask(zhadanboom, xBoss)
                    if bzbosspz:
                        if boss_zhadan_cxpz_time % 180 == 0:
                            xBoss.blood -= 1000
                        boss_zhadan_cxpz_time+=1

            drfeiji.dr_group.update()
            drfeiji.drzd_group.update()


            drboom_group.update('dr',ticks, 80)
            player_zhadan_group.update()
            player_zhadan_boom_group.update('playerzhadan',ticks,60)
            jydrfeiji.jydr_group.update()
            jydr_boom_group.update('dr', ticks, 80)
            player_zdhh_group.update('zidan',ticks,80)
            zhadan_weiqi_group.update(ticks,60)
            player_wq_group.update()

            player_wq_group.draw(screen)
            player_zhadan_group.draw(screen)
            zhadan_weiqi_group.draw(screen)
            player_zhadan_boom_group.draw(screen)
            player_group.draw(screen)
            playerzidan.bullets.draw(screen)
            drfeiji.dr_group.draw(screen)
            jydrfeiji.jydr_group.draw(screen)
            drfeiji.drzd_group.draw(screen)
            drboom_group.draw(screen)
            player_zdhh_group.draw(screen)
            jydr_boom_group.draw(screen)

            if player_wq_level == 3:
                print_chtext(font, 0, 700, "三级武器剩余时间：" + str(player_threewq_time // 10) + "s")

            if player_score > 10000 and Boss_time == False :
                if boss_cx_music_time % 220 == 0:
                    boss_cx_music.play_sound()
                boss_cx_music_time += 1
                if boss_cx_music_time % 480 == 0:
                    boss_cx_music.play_pause()
                    Boss_time = True
                if boss_cx_music_time % 120 < 60 :
                    print_bosstext(font,175,150,"警告！BOSS即将出现！")

            if player_score > 2000 and player_score < 4000 and drupdate_time == 100:
                drupdate_time = 80
            if player_score > 4000 and player_score < 6000 and drupdate_time == 80:
                drupdate_time = 60
            if player_score > 6000 and player_score < 8000 and drupdate_time == 60:
                drupdate_time = 40
            if Boss_time == True :

                if boss_cz == False:
                    main_bg_music.stop()
                    # boss背景音乐
                    boss_bg_music = pygame.mixer.music
                    boss_bg_music.load("music/boss_bg.ogg")
                    boss_bg_music.set_volume(0.8)
                    # 生成boss
                    xBoss = enemyBOSS.Boss(ruler)
                    weizhi3 = xBoss.rect.center
                    # 生成子弹
                    # boss一型子弹
                    bullet2 = []
                    bullet2_index = 0
                    BULLET2_NUM = 100
                    for en in range(BULLET2_NUM):
                        bullet2.append(bullet.Bullet2(xBoss.rect.midbottom))

                    # 生成boss散弹
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

                    # 激光炮
                    weizhi1 = xBoss.rect.left + 180, xBoss.rect.top + 160
                    jiguang1 = bullet.Bullet3(weizhi1)
                    weizhi2 = xBoss.rect.left - 20, xBoss.rect.top + 160
                    jiguang2 = bullet.Bullet3(weizhi2)
                    boss_cz=True
                    boss_bg_music.play()


                # boss绘制

                if zidanjg % 60 == 0:
                    boss_bg_music_time += 1
                    if boss_bg_music_time % 83 == 0:
                        boss_bg_music_cs = True
                if boss_bg_music_time % 83 == 0 and boss_bg_replay_flag and boss_bg_music_cs:
                    boss_bg_music.play()
                    boss_bg_music_cs = False
                # 发射子弹
                if not (delay % 10):
                    bullet2[bullet2_index].reset(xBoss.rect.midbottom)
                    bullet2_index = (bullet2_index + 1) % BULLET2_NUM


                if delay % 900 == 0:
                    kind = not kind

                if xBoss.blood > 2000:
                    for n in bullet2:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                    if kind == True:
                        for b in bullet2:
                            if b.touches:
                                b.move()
                                screen.blit(b.image, b.rect)
                    else:
                        for b in bullet2:
                            b.reset(xBoss.rect.midbottom)
                        weizhi1 = xBoss.rect.left + 180, xBoss.rect.top + 160
                        jiguang1.move(weizhi1)
                        if pygame.sprite.collide_mask(jiguang1,player):
                            if pygame.sprite.collide_circle_ratio(0.5)(jiguang1,player):
                                if player_boss_jgcxpz_time1 % 60 == 0 :
                                    player.life-=5
                                player_boss_jgcxpz_time1 += 1
                        else:
                            player_boss_jgcxpz_time1=0
                        if not (delay % 20):
                            screen.blit(jiguang1.image1, jiguang1.rect)
                        else:
                            screen.blit(jiguang1.image3, jiguang1.rect)
                        weizhi2 = xBoss.rect.left - 20, xBoss.rect.top + 160
                        jiguang2.move(weizhi2)
                        if pygame.sprite.collide_mask(jiguang2,player):
                            if pygame.sprite.collide_circle_ratio(0.5)(jiguang2,player):
                                if player_boss_jgcxpz_time2 % 60 == 0 :
                                    player.life-=5
                                player_boss_jgcxpz_time2 += 1
                        else:
                            player_boss_jgcxpz_time2=0
                        if not (delay % 20):
                            screen.blit(jiguang2.image1, jiguang2.rect)
                        else:
                            screen.blit(jiguang2.image3, jiguang2.rect)
                else:
                    for n in sandan1:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz = None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan2:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz = None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan3:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz = None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan4:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz=None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan5:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz=None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan6:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz=None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan7:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz=None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for n in sandan8:
                        bosszdpz = pygame.sprite.spritecollideany(n, player_group)
                        zdboom_boos_zdpz = pygame.sprite.spritecollideany(n, player_zhadan_boom_group)
                        if bosszdpz:
                            if pygame.sprite.collide_circle_ratio(0.5)(n, player):
                                n.reset((800, 800))
                                player.life -= 5
                                bosszdpz=None
                        if zdboom_boos_zdpz:
                            if pygame.sprite.collide_mask(n, zdboom_boos_zdpz):
                                n.reset((800, 800))
                                zdboom_boos_zdpz = None
                    for d in sandan1:
                        d.move1()
                        screen.blit(d.image, d.rect)
                    for d in sandan2:
                        d.move2()
                        screen.blit(d.image, d.rect)
                    for d in sandan3:
                        d.move3()
                        screen.blit(d.image, d.rect)
                    for d in sandan4:
                        d.move4()
                        screen.blit(d.image, d.rect)
                    for d in sandan5:
                        d.move5()
                        screen.blit(d.image, d.rect)
                    for d in sandan6:
                        d.move6()
                        screen.blit(d.image, d.rect)
                    for d in sandan7:
                        d.move7()
                        screen.blit(d.image, d.rect)
                    for d in sandan8:
                        d.move8()
                        screen.blit(d.image, d.rect)
                weizhi3 = xBoss.rect.center
                if not (delay % 60):
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
                # boss血条
                pygame.draw.line(screen, black, (0, 0), (600, 0), 20)
                boss_life = xBoss.blood / enemyBOSS.Boss.blood
                pygame.draw.line(screen, red, (0, 0), (600 * boss_life, 0), 20)

                if not (delay % 100):
                    xBoss.speedx = random.randint(-2, 2)
                    xBoss.speedy = random.randint(-3, 2)

                # 绘制boss

                if boss_life > 0.7:
                    xBoss.Bmove()
                    screen.blit(xBoss.image1, xBoss.rect)

                elif boss_life < 0.7 and boss_life > 0.4 or boss_life == 0.4:
                    xBoss.Bmove()
                    screen.blit(xBoss.image2, xBoss.rect)
                    xBoss.mask = pygame.mask.from_surface(xBoss.image3)

                elif boss_life == 0.4 or boss_life < 0.4 and boss_life > 0:
                    if change == False:
                        xBoss.rect = xBoss.image3.get_rect()
                        xBoss.rect.left, xBoss.rect.top = (xBoss.width - xBoss.rect.width) // 2, 10
                        change = True
                    xBoss.life = False
                    xBoss.Bmove1()
                    screen.blit(xBoss.image3, xBoss.rect)
                elif boss_life<=0:
                    player_score+=10000
                    time.sleep(2)
                    player_win = True
                    playerboomjs = True


                # 2.Boss
                if pygame.sprite.collide_mask(player, xBoss):
                    if player_boss_cxpz_time % 60 == 0:
                        player.life -= 10
                    player_boss_cxpz_time+=1
                else:
                    player_boss_cxpz_time=0




            #玩家血条
            pygame.draw.rect(screen, (50, 150, 50, 180), Rect(390, 765, player.life * 2, 25))
            pygame.draw.rect(screen, (100, 200, 100, 180), Rect(390, 765, 200, 25), 2)

            #炸弹数量
            screen.blit(player_zhadan_ico, (0, 756))
            print_text(font, 40, 766, ' X  ' + str(player_zhadan_num))

            #玩家分数
            print_text(font,0,10,'Score: '+str(player_score))

            if player.life<=0:
                playerboom.position = player.X, player.Y
                player.kill()
                if playerboomjs ==False:
                    playerboom_group.add(playerboom)
                    player_boom_music.play_sound()
                if playerboom.frame >= playerboom.last_frame:
                    playerboomjs=True
                    time.sleep(2)
            if playerboomjs==True:
                GameOver =True
                for n in drfeiji.dr_group:      #初始化敌人
                    n.kill()
                for n in drfeiji.drzd_group:    #初始化敌人子弹
                    n.kill()
                for n in drboom_group:          #初始化敌人爆炸
                    n.kill()
                for n in jydr_boom_group:
                    n.kill()
                for n in jydrfeiji.jydr_group:
                    n.kill()
                for n in player_zdhh_group:
                    n.kill()
                for n in player_zhadan_boom_group:
                    n.kill()
                for n in player_zhadan_group:
                    n.kill()#
                for n in player_wq_group:
                    n.kill()
                boss_kill()
                main_bg_music.stop()
                gameover_music.play_sound()
                gameover_music_time+=1
                boss_cz = False

            playerboom_group.update('player', ticks, 100)
            playerboom_group.draw(screen)

            if Boss_time == False:
                #主要背景音乐循环
                if zidanjg % 60 ==0:
                    main_bg_music_time += 1
                    if main_bg_music_time % 149 == 0:
                        main_bg_music_cs = True
                if main_bg_music_time % 149 == 0 and main_bg_replay_flag and main_bg_music_cs and Boss_time == False:
                    main_bg_music.play()
                    main_bg_music_cs = False
        else:
            main_bg_replay_flag = False
            boss_bg_replay_flag = False
            gameover_js+=1
            framerate.tick(10)
            screen.fill((0,0,0))
            if player_win == True:
                print_chtext(font, 245, 400, "恭喜通关！")
            else:
                print_text(font, 200, 400, "G A M E   O V E R")
            print_text(font, 207,500,'You Score: '+str(player_score))
            print_chtext(font, 195, 700, "按 “F2” 重 新 开 始")
            if gameover_js%10 == 0:
                gameover_music_time+=1
                if gameover_music_time % 12 == 0:
                    gameover_music.play_pause()
                    gameover_music.play_sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            ckeys = pygame.key.get_pressed()
            if ckeys[K_F2]:
                player.life=100
                player.position = 250, 600
                player_group.add(player)
                GameOver = False
                playerboomjs=False
                player_wq_level=1
                player_score = 0
                main_bg_music_time = 0
                boss_bg_music_time = 0
                main_bg_music = pygame.mixer.music
                main_bg_music.load("music/Rockman3.ogg")
                main_bg_music.play()
                player_zhadan_num = 5
                player_win = False
                gameover_music.play_pause()
                drupdate_time = 100
                boss_cx_music_time = 0
                player_threewq_time = 100

    else:
        framerate.tick(1)
        screen.blit(Start_image,(0,0))
        if zidanjg%2 ==0 :
            print_chtext(font, 190, 600, "按 “F1” 开 始 游 戏")

        zidanjg+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            keys = pygame.key.get_pressed()
            if keys[K_F1]:
                bg_replay_flag = False
                Start_music.play_pause()
                GameStart = True
        bg_music_time = time.clock()
        if int(bg_music_time) % 14 ==0 and bg_replay_flag and int(bg_music_time)!=0:
            Start_bg_replay()
    pygame.display.update()