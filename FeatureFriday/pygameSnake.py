#Feature Friday (9/23/2016)

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.font: print('Warning, sound disabled')

class PyManMain:
    
    def __init__(self, width=640, height=640):
        
        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
if __name__ == '__main__':
    MainWindow = PyManMain()
    MainWindow.MainLoop()
