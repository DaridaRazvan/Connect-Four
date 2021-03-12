from Computer import SimpleComputer
from Game import Game
from Board import Board

class Ui:
    def __init__(self,game):
        self._game = game

    def player_input(self):
        x = int(input(">"))
        while x >7:
            print("Invalid command. Number should be between 1 and 7")
            x = int(input(">"))

        return x        

    def start(self):
        while self._game._board.isTie() == False:
            print(self._game._board.drawBoard())

            #Player
            x = self.player_input()
            self._game.playerMove(x,1)
            if self._game._board.isWin() == True:
                print(self._game._board.drawBoard())
                print("You win!")
                break

            #Computer
            self._game.computerMove(-1)  
            if self._game._board.isWin() == True:
                print(self._game._board.drawBoard())
                print("You lose!")
                break
            if self._game._board.isTie() == True:
                print(self._game._board.drawBoard())
                print("It's a draw!")    
                break

b = Board()
c = SimpleComputer(b)
g = Game(b,c)
ui = Ui(g)
ui.start()