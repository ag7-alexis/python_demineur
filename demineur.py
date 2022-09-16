import sys
from colorama import init

from MineSweeper import MineSweeper
from PlayGame import PlayGame, Player

if __name__ == '__main__':
    init()
    mine_sweeper = MineSweeper()
    player = Player()
    argv = sys.argv

    game = PlayGame(mine_sweeper=mine_sweeper, player=player)
    game.run()
