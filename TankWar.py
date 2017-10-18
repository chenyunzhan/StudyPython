import pygame,sys
from pygame.locals import *

class TankGame():

    def startGame(self):
        screen = pygame.display.set_mode((600,500),0,32)
        tank = Tank(screen,(400,270))
        while True:
            screen.fill((0,0,0))
            tank.show()
            self.getEvent()
            pygame.display.set_caption('坦克大战')
            pygame.display.update()

    def stopGame(self):
        sys.exit()


    def getEvent(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()


class MySprite(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen


class Tank(MySprite):
    def __init__(self,screen,position):
        super().__init__(screen)
        self.direction="U"
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



tankGame=TankGame()
tankGame.startGame()