import pygame
import os
import time
import pyautogui


class Game():
    """ Class to handle the game """

    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.unitSize = self.getUnitSize()
        self.imageDict = {}

    def run(self):
        '''
        This method initializes the game and
        runs until it is quit
        '''
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == 256:
                    running = False
                if event.type == 1025:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(pos, rightClick)
            self.generateBoard()
            pygame.display.flip()
            if self.board.getWon():
                pyautogui.alert(title="Well done",
                                text="You did it! So proud of you!”")
                time.sleep(3000)
                running = False
        pygame.quit()

    def generateBoard(self):
        '''
        This function generates an empty board
        '''
        self.imageDict = self.loadImageDict()
        topLeft = (0, 0)
        for _row in range(self.board.getSize()[0]):
            for _col in range(self.board.getSize()[1]):
                unit = self.board.getUnit((_row, _col))
                image = self.getImage(unit)
                self.screen.blit(image, topLeft)
                topLeft = (topLeft[0] + self.unitSize[0], topLeft[1])
            topLeft = (0, topLeft[1] + self.unitSize[1])

    def loadImageDict(self):
        '''
        This is a helper function to map image with its name
        '''
        imageDict = {}
        for fileName in os.listdir("images"):
            if not fileName.endswith('.png'):
                continue
            else:
                image = pygame.image.load(os.path.join('images', fileName))
                image = pygame.transform.scale(image, self.unitSize)
                imageDict[fileName.split('.')[0]] = image
        return imageDict

    def getUnitSize(self):
        '''
        This is a helper function to calculate the 
        size of each unit
        '''
        w = self.screenSize[0] // self.board.getSize()[1]
        h = self.screenSize[1] // self.board.getSize()[0]
        return (w, h)

    def getImage(self, unit):
        '''
        This method gets the filename of the image
        to be displayed in an unit
        '''
        if (unit.getClicked()):
            if (unit.getHasBomb()):
                imageName = "bomb-at-clicked-block"
            else:
                imageName = str(unit.getNumBombsAround())
        else:
            imageName = 'flag' if unit.getFlagged() else 'empty-block'
        return self.imageDict[imageName]

    def handleClick(self, pos, rightClick):
        '''
        This method handles mouseclick
        '''
        if self.board.getLost():
            pyautogui.alert(title="You lost",
                            text="Game over, you stepped on a landmine!")
            return
        index = (pos[1]//self.unitSize[0], pos[0]//self.unitSize[1])
        unit = self.board.getUnit(index)
        self.board.handleClick(unit, rightClick)
        if not rightClick and not unit.getFlagged():
            unit.setClicked(True)
        image = self.getImage(unit)
        self.screen.blit(image, index)
