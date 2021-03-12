from random import randint
class SimpleComputer:
    def __init__(self,board):
            self._board = board

    def computerMove(self):
        '''
        computer move that wins if there are 3 in a row/column/diagonal
        blocks the player from winning
        else make a random move
        '''
        d = self._board._data

        if self._board._moves % 2 == 0:
            return -1

        for position in range (0,35):
            if not d[position+7] == 0 and d[position] == 0:
                
                d[position] = -1
                if self._board.isWin() == True:
                    d[position] = 0
                    return position
                    
                d[position] = 1
                if self._board.isWin() == True:
                    d[position] = 0
                    return position

                d[position] = 0  

        for position in range (35,42):
            if d[position] == 0:

                d[position] = -1
                if self._board.isWin() == True:
                    d[position] = 0
                    return position

                d[position] = 1
                if self._board.isWin() == True:
                    d[position] = 0
                    return position

                d[position] = 0    

                          
        return self.randomComputerMove()

    def randomComputerMove(self):
        '''
        random move used in computerMove
        '''
        randomPosition = randint(0,6)
        x = 35
        while not self._board._data[randomPosition + x] == 0:
            x -= 7    
            if x < 0:
                randomPosition = randint(0,6)
                x = 35

        return randomPosition + x