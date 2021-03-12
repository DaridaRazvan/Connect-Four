class Game:
    def __init__(self,board,computer):
        self._board = board
        self._computer = computer

    def playerMove(self,position,var):
        '''
        gets the player move
        '''
        position = position - 1

        if self._board._data[position] == 0:
            x = 35
            while not self._board._data[position + x] == 0:
                x -= 7

            self._board._moves += 1
            self._board._data[position + x] = var     

    def computerMove(self,var):
        '''
        gets the computer move
        '''
        move = self._computer.computerMove()   
        if not move == -1:
            self._board._moves += 1 
            self._board._data[move] = var