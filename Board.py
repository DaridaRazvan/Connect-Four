from texttable import Texttable

class Board:
    def __init__(self):
        self._data = [0] * 42
        self._moves = 0

    def drawBoard(self):
        '''
        draws the board
        '''
        t = Texttable()
        d = {-1:'O',0:' ',1:'X'}

        for i in range(0,41,7):
            row = self._data[i:i+7]
            for j in range(7):
                row[j] = d[row[j]]
            t.add_row(row)

        return t.draw()

    def isTie(self):
        '''
        checks if the game is a tie
        '''
        if self._moves == 42:
            return True
        else:
            return False    

    def isWin(self):
        '''
        0  1  2  3  4  5  6
        7  8  9  10 11 12 13
        14 15 16 17 18 19 20
        21 22 23 24 25 26 27
        28 29 30 31 32 33 34
        35 36 37 38 39 40 41 

        checks if the game is won by the player or by the computer
        '''
        d = self._data
        for position in range(0,42):
            if not d[position] == 0:
                x = position // 7
                y = position % 7

                # x = 32 : 7  = 4   ... y = 32 % 7 = 4
                # position = x * 7 + y

                # stanga in linie
                if y >= 3:
                    if d[position] == d[position-1] and d[position] == d[position-2] and d[position] == d[position-3]:
                        return True

                # dreapta in linie
                if y <= 3: 
                    if d[position] == d[position+1] and d[position] == d[position+2] and d[position] == d[position+3]:
                        return True

                # jos in coloana ( sus nu se poate)
                if x <=2:
                    if d[position] == d[position+7] and d[position] == d[position+14] and d[position] == d[position+21]:
                        return True

                # diagonala stanga jos
                if y >= 3 and  x <= 2:
                    if d[position] == d[position+6] and d[position] == d[position+12] and d[position] == d[position+18]:
                        return True

                # diagonala dreapta jos
                if y <=3 and x<=2:
                    if d[position] == d[position+8] and d[position] == d[position+16] and d[position] == d[position+24]:
                        return True

                # diagonala stanga sus
                if y>=3 and x>=3:
                    if d[position] == d[position-8] and d[position] == d[position-16] and d[position] == d[position-24]:
                        return True

                # diagonala dreapta sus
                if y <=3 and x>=3:
                    if d[position] == d[position-6] and d[position] == d[position-12] and d[position] == d[position-18]:
                        return True

        return False