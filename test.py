import pygame
from pygame.locals import *


class AAA():

    def startGame(self):
        screen = pygame.display.set_mode((600,500),0,32)
        pygame.display.set_caption('坦克大战')

        while True:
            screen.fill((255,255,255))
            pygame.display.update()
            self.getEvent()


    def getEvent(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()

tankGame=AAA()
tankGame.startGame()