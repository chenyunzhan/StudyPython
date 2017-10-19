import pygame,sys,time
from pygame.locals import *
from random import randint,sample

class TankGame():

    gameWidth=600
    gameHeight=500
    myTankMissile=[]
    booms=[]
    enemyTanks = pygame.sprite.Group()

    def startGame(self):
        pygame.init()
        screen = pygame.display.set_mode((TankGame.gameWidth,TankGame.gameHeight),0,32)
        tank = MyTank(screen)
        for i in range(0,500):
            enemyTank = EnemyTank(screen)
            TankGame.enemyTanks.add(enemyTank)
        while True:
            screen.fill((0,0,0))
            tank.show()
            tank.move()
            for enemyTank in TankGame.enemyTanks:
                enemyTank.show()
                enemyTank.move()
            for missile in TankGame.myTankMissile:
                if not missile.alive:
                    TankGame.myTankMissile.remove(missile)
                missile.show()
                missile.move()
            for boom in TankGame.booms:
                boom.show()
            self.getEvent(tank,screen)
            self.showText(screen)
            pygame.display.set_caption('坦克大战')
            time.sleep(0.05)
            pygame.display.update()

    def stopGame(self):
        sys.exit()

    def showText(self,screen):
        font = pygame.font.SysFont("SimHei",20)
        text1=font.render("enemyTanks's count: %s"%len(TankGame.enemyTanks),0,(255,0,0))
        text2=font.render("myTankMissile's count: %s"%len(TankGame.myTankMissile),0,(255,0,0))
        screen.blit(text1,(0,0))
        screen.blit(text2,(0,15))

    def getEvent(self,tank,screen):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()
            if event.type==KEYDOWN:
                if event.key==K_a:
                    tank.direction = "L"
                    tank.stop=False
                elif event.key==K_w:
                    tank.direction = "U"
                    tank.stop=False
                elif event.key==K_d:
                    tank.direction = "R"
                    tank.stop=False
                elif event.key==K_s:
                    tank.direction = "D"
                    tank.stop=False
                elif event.key==K_j:
                    misslie=Missile(screen,tank)
                    TankGame.myTankMissile.append(misslie)
            elif event.type==KEYUP:
                if event.key==K_a:
                    tank.stop=True
                elif event.key==K_w:
                    tank.stop=True
                elif event.key==K_d:
                    tank.stop=True
                elif event.key==K_s:
                    tank.stop=True

class MySprite(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen


class Tank(MySprite):
    def __init__(self,screen,position):
        super().__init__(screen)
        self.direction="U"
        self.speed=20
        self.alive=True
        self.stop=True
        self.images={}
        self.images["U"]=pygame.image.load("images/p1tankU.gif")
        self.images["D"]=pygame.image.load("images/p1tankD.gif")
        self.images["L"]=pygame.image.load("images/p1tankL.gif")
        self.images["R"]=pygame.image.load("images/p1tankR.gif")
        self.image=self.images[self.direction]
        self.position=position
        self.rect = self.image.get_rect()
        self.rect.top=position[0]
        self.rect.left=position[1]


    def show(self):
        self.image = self.images[self.direction]
        self.screen.blit(self.image,self.rect)

    def move(self):

        if not self.stop:
            if self.direction=="L":
                if self.rect.left>0:
                    self.rect.left -= self.speed
                else:
                    self.rect.left=0
            elif self.direction=="R":
                if self.rect.right<TankGame.gameWidth:
                    self.rect.right += self.speed
                else:
                    self.rect.right=TankGame.gameWidth
            elif self.direction=="U":
                if self.rect.top>0:
                    self.rect.top -= self.speed
                else:
                    self.rect.top=0
            elif self.direction=="D":
                if self.rect.bottom<TankGame.gameHeight:
                    self.rect.bottom += self.speed
                else:
                    self.rect.bottom=TankGame.gameHeight

    def fire(self):
        pass

class MyTank(Tank):
    def __init__(self,screen):
        super().__init__(screen,(400,270))



class EnemyTank(Tank):
    def __init__(self, screen):
        position=(0,randint(0,5)*100)
        super().__init__(screen,position)
        self.images["U"]=pygame.image.load("images/enemy1U.gif")
        self.images["D"]=pygame.image.load("images/enemy1D.gif")
        self.images["L"]=pygame.image.load("images/enemy1L.gif")
        self.images["R"]=pygame.image.load("images/enemy1R.gif")
        self.stop=False
        self.step=0
        self.speed=10
        self.direction = sample(["U","D","L","R"],1)[0]


    def move(self):
        self.step+=1
        if self.step == randint(5,10) or self.step>10:
            self.step=0
            self.direction = sample(["U","D","L","R"],1)[0]
        super().move()

class Missile(MySprite):
    def __init__(self,screen,tank):
        super().__init__(screen)
        self.image=pygame.image.load("images/tankmissile.gif")
        self.alive=True
        self.rect = self.image.get_rect()
        self.direction = tank.direction

        position=(0,0)
        if self.direction=="U":
            position = (tank.rect.top-self.rect.height,tank.rect.left+(tank.rect.width-self.rect.width)/2)
        elif self.direction == "D":
            position = (tank.rect.top + tank.rect.height, tank.rect.left + (tank.rect.width - self.rect.width) / 2)
        elif self.direction == "L":
            position = (tank.rect.top + (tank.rect.height - self.rect.height) / 2, tank.rect.left-self.rect.width)
        elif self.direction == "R":
            position = (tank.rect.top + (tank.rect.height - self.rect.height) / 2, tank.rect.left+tank.rect.width)
        self.rect.top=position[0]
        self.rect.left=position[1]
        self.speed=30

    def show(self):
        self.screen.blit(self.image,self.rect)

    def move(self):

        self.hit()
        if self.alive:
            if self.direction=="L":
                print(self.rect.left)
                if self.rect.left>-self.rect.width:
                    self.rect.left -= self.speed
                else:
                    self.alive = False
            elif self.direction=="R":
                if self.rect.right<TankGame.gameWidth+self.rect.width:
                    self.rect.right += self.speed
                else:
                    self.alive = False
            elif self.direction=="U":
                if self.rect.top>-self.rect.height:
                    self.rect.top -= self.speed
                else:
                    self.alive = False
            elif self.direction=="D":
                if self.rect.bottom<TankGame.gameHeight+self.rect.height:
                    self.rect.bottom += self.speed
                else:
                    self.alive = False

    def hit(self):
        blocks_hit_list = pygame.sprite.spritecollide(self, TankGame.enemyTanks, True)

        for hitTank in blocks_hit_list:
            hitTank.alive=False
            self.alive=False
            boom = Boom(self.screen,hitTank)
            TankGame.booms.append(boom)

class Boom(MySprite):
    def __init__(self,screen,tank):
        super().__init__(screen)
        self.alive=True
        self.imageIndex=0
        self.hitTank = tank
        self.images=[pygame.image.load("images/blast1.gif"), \
                     pygame.image.load("images/blast2.gif"), \
                     pygame.image.load("images/blast3.gif"), \
                     pygame.image.load("images/blast4.gif"), \
                     pygame.image.load("images/blast5.gif"), \
                     pygame.image.load("images/blast6.gif"), \
                     pygame.image.load("images/blast7.gif"), \
                     pygame.image.load("images/blast8.gif")]
    def show(self):
        if self.alive:
            print(self.imageIndex)
            if self.imageIndex==len(self.images):
                self.alive=False
            else:
                self.screen.blit(self.images[self.imageIndex], self.hitTank.rect)
                self.imageIndex += 1

        else:
            pass

tankGame=TankGame()
tankGame.startGame()