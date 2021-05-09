from unit import Unit
from random import random


class Board():
    """ Class to handle the board and its attributes """

    def __init__(self, boardSize, prob):
        self._size = boardSize
        self.prob = prob
        self._lost = False
        self._numClicked = 0
        self._numNonBombs = 0
        self.board = self.setBoard()
        self.setNeighbours()

    def setNeighbours(self):
        '''
        This method sets the neighbours of all the units
        '''
        for _row in range(self.getSize()[0]):
            for _col in range(self.getSize()[1]):
                unit = self.getUnit((_row, _col))
                neighbours = self.getListOfNeighbours((_row, _col))
                unit.setNeighbours(neighbours)

    def setBoard(self):
        '''
        This method initializes the board with the numbers and bombs
        '''
        board = []
        for row in range(self._size[0]):
            row_item = []
            for col in range(self._size[1]):
                hasBomb = random() < self.prob
                if not hasBomb:
                    self._numNonBombs += 1
                unit = Unit(hasBomb)
                row_item.append(unit)
            board.append(row_item)
        return board

    def getListOfNeighbours(self, index):
        ''' 
        This method will fetch the list of neighbours of an unit
        '''
        _row, _col = index
        neighbours = []
        for row in range(_row-1, _row+2):
            for col in range(_col-1, _col+2):
                outOfBounds = (row < 0 or row > self.getSize()[0]-1) or (
                    col < 0 or col > self.getSize()[1]-1)
                sameUnit = row == _row and col == _col
                if (outOfBounds or sameUnit):
                    continue
                neighbours.append(self.getUnit((row, col)))
        return neighbours

    def handleClick(self, unit, flag):
        ''' 
        This method implements the functionality of a mouseclick
        '''
        if (unit.getClicked() or (not flag and unit.getFlagged())):
            return
        if flag:
            unit.setFlagged(not unit.getFlagged())
            return
        self._numClicked += 1
        unit.setClicked(True)
        if unit.getHasBomb():
            self._lost = True
        else:
            self._won = self.getWon()
        if unit.getNumBombsAround() == 0 and not unit.getHasBomb():
            for neighbour in unit.getNeighbours():
                self.handleClick(neighbour, flag=False)

    def getSize(self):
        ''' This method returns the size of the board '''
        return self._size

    def getUnit(self, index):
        ''' 
        This method gets unit object at the given index
        '''
        row, col = index
        return self.board[row][col]

    def getWon(self):
        ''' This method checks if the player has won '''
        return self._numClicked == self._numNonBombs

    def getLost(self):
        ''' This method checks if the game is lost '''
        return self._lost
