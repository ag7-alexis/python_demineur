import sys

from MineSweeper import MineSweeper, PartyNotStartedError

if __name__ == '__main__':

    mine_sweeper = MineSweeper()

    argv = sys.argv

    while True:
        x = input("TEST :")
        inputs = x.split(" ")
        try:
            if len(inputs) == 2:
                y = int(inputs[0])
                x = int(inputs[1])
                mine_sweeper.open(x, y)

            elif len(inputs) == 1:
                if inputs[0] != 'newgame':
                    raise Exception("Unexpected command", inputs[0])
                mine_sweeper.new_game()
                print("game started")
            else:
                if inputs[0] != 'f':
                    raise  Exception('Unexpected input expect "f" found', inputs[0])

                y = int(inputs[1])
                x = int(inputs[2])
                mine_sweeper.flag(x, y)
        except PartyNotStartedError as e:
            print("No party started, please write newgame")



