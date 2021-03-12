from Board import Board
import unittest

class test_game(unittest.TestCase):
    def test_1(self):

        b = Board()

        b._data[0] = 1
        b._data[1] = 1
        b._data[2] = 1
        b._data[3] = 1

        assert b.isWin() == True

    def test_2(self):

        b = Board()

        b._data[11] = 1
        b._data[12] = 1
        b._data[13] = 1
        b._data[14] = 1

        assert b.isWin() == False

    def test_3(self):

        b = Board()

        b._data[35] = 1
        b._data[29] = 1
        b._data[23] = 1
        b._data[17] = 1

        assert b.isWin() == True        
    
    def test_4(self):

        b = Board()

        b._data[14] = 1
        b._data[22] = 1
        b._data[30] = 1
        b._data[38] = 1

        assert b.isWin() == True 

    def test_5(self):

        b = Board()

        b._data[35] = 1
        b._data[29] = 1
        b._data[23] = 1

        assert b.isWin() == False       

unittest.main()
