class Unit():
    """ Class to handle an unit and its attrbutes """

    def __init__(self, hasBomb):
        self._hasBomb = hasBomb
        self._clicked = False
        self._flagged = False
        self._neighbours = []

    def numBombsAround(self):
        ''' This method calculates number of bombs around an unit '''
        numBombsAround = 0
        for unit in self.getNeighbours():
            if unit.getHasBomb():
                numBombsAround += 1
        return numBombsAround

    def getNeighbours(self):
        ''' This method gets all the neighbours of an unit '''
        return self._neighbours

    def getHasBomb(self):
        ''' This method checks if an unit has bomb '''
        return self._hasBomb

    def getClicked(self):
        ''' This method checks if an unit is clicked or not '''
        return self._clicked

    def getFlagged(self):
        ''' This method checks whether an unit is flagged '''
        return self._flagged

    def getNumBombsAround(self):
        ''' This method returns the number of bombs around an unit '''
        return self.numBombsAround

    def setNeighbours(self, neighbours):
        ''' This method sets neighbours and the bombs arounds an unit '''
        self._neighbours = neighbours
        self.numBombsAround = self.numBombsAround()

    def setClicked(self, clicked):
        ''' This method sets unit click '''
        self._clicked = clicked

    def setFlagged(self, flagged):
        ''' This method sets unit flag '''
        self._flagged = flagged
