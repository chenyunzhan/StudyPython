import pygame,sys
from pygame.locals import *

class TankGame():

    gameWidth=600
    gameHeight=500

    def startGame(self):
        pygame.init()
        screen = pygame.display.set_mode((TankGame.gameWidth,TankGame.gameHeight),0,32)
        tank = MyTank(screen)
        while True:
            screen.fill((0,0,0))
            tank.show()
            self.getEvent(tank)
            self.showText(screen)
            pygame.display.set_caption('坦克大战')
            pygame.display.update()

    def stopGame(self):
        sys.exit()

    def showText(self,screen):
        font = pygame.font.SysFont("SimHei",20)
        text=font.render("陈云展",0,(255,0,0))
        screen.blit(text,(0,0))

    def getEvent(self,tank):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()
            if event.type==KEYDOWN:
                if event.key==K_a:
                    tank.direction = "L"
                    tank.move()
                elif event.key==K_w:
                    tank.direction = "U"
                    tank.move()
                elif event.key==K_d:
                    tank.direction = "R"
                    tank.move()
                elif event.key==K_s:
                    tank.direction = "D"
                    tank.move()

class MySprite(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen


class Tank(MySprite):
    def __init__(self,screen,position):
        super().__init__(screen)
        self.direction="U"
        self.speed=20
        self.images={}
        self.images["U"]=pygame.image.load("images/p1tankU.gif")
        self.images["D"]=pygame.image.load("images/p1tankD.gif")
        self.images["L"]=pygame.image.load("images/p1tankL.gif")
        self.images["R"]=pygame.image.load("images/p1tankR.gif")
        self.image=self.images[self.direction]
        self.postion=position
        self.rect = self.image.get_rect()
        self.rect.top=position[0]
        self.rect.left=position[1]


    def show(self):
        self.image = self.images[self.direction]
        self.screen.blit(self.image,self.rect)

    def move(self):
        pass

    def fire(self):
        pass

class MyTank(Tank):
    def __init__(self,screen):
        super().__init__(screen,(400,270))

    def move(self):
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
tankGame=TankGame()
tankGame.startGame()