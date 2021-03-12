import pygame

from Computer import SimpleComputer
from Game import Game
from Board import Board

class Gui:
    def __init__(self,game):
        self._game = game
        self._x = 40
        self._y = 120
        self._run = True
   
    def start(self):
        pygame.init()

        pygame.display.set_caption("Connect 4")
        win = pygame.display.set_mode((560,560))
        font = pygame.font.SysFont("Monospace",75) 

        while self._run == True:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(win,(0,0,0),(0,0,560,80))
                    circleX = event.pos[0]
                    pygame.draw.circle(win,(255,255,0),(circleX,40),35,35)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    x = x// 80 + 1
                    self._game.playerMove(x,1)
                    if self._game._board.isWin() == True:
                        #print("You win!")
                        pygame.draw.rect(win,(0,0,0),(0,0,560,80))
                        label = font.render("You Win!",1,(255,255,0))
                        win.blit(label,(40,10))
                        self._run = False
                        break
                    self._game.computerMove(-1)
                    if self._game._board.isWin() == True:
                        #print("You lose!")
                        pygame.draw.rect(win,(0,0,0),(0,0,560,80))
                        label = font.render("You lose!",1,(255,255,0))
                        win.blit(label,(40,10))
                        self._run = False
                        break
                    if self._game._board.isTie() == True:
                        #print("It's a draw!")
                        pygame.draw.rect(win,(0,0,0),(0,0,560,80))
                        label = font.render("Draw!",1,(255,255,0))
                        win.blit(label,(40,10))  
                        self._run = False
                        break
            
            pygame.draw.rect(win,(0,0,255),(0,80,560,480))

            for position in range(0,42):
                posX = 40 + 80*(position % 7) 
                posY = 120 + 80*(position // 7)

                if self._game._board._data[position] == 0:
                    pygame.draw.circle(win,(0,0,0),(posX,posY),35,35)
                elif self._game._board._data[position] == 1:
                    pygame.draw.circle(win,(255,255,0),(posX,posY),35,35)
                else:
                    pygame.draw.circle(win,(255,0,0),(posX,posY),35,35) 
        
            pygame.display.update()  

            if self._run == False:
                pygame.time.wait(3000)  
        
        pygame.quit()    

b = Board()
c = SimpleComputer(b)
g = Game(b,c)
g = Gui(g)
g.start()
