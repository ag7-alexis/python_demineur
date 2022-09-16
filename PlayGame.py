from Action import Action, ActionNewGame, ActionQuit, ActionFlag, ActionOpen
from MineSweeper import MineSweeper


class Player:
    def get_action(self, input: str) -> Action:
        command = input.split(" ")
        try:
            if command[0] == "newgame":
                return ActionNewGame()
            if command[0] == "quit":
                return ActionQuit()
            if command[0] == "f":
                y = int(command[1])
                x = int(command[2])
                return ActionFlag(x=x, y=y)

            if command[0].isnumeric():
                y = int(command[0])
                x = int(command[1])
                return ActionOpen(x=x, y=y)

            raise Exception("Unknow command")
        except IndexError:
            print("Unknow instruction")


class PlayGame():
    def __init__(self, mine_sweeper: MineSweeper, player: Player):
        self.mine_sweeper = mine_sweeper
        self.player = player
        self.playing = True

    def run(self):
        while self.playing:
            user_input = input(">")
            action = self.player.get_action(input=user_input)
            if isinstance(action, ActionQuit):
                self.quit()
            if isinstance(action, ActionNewGame):
                self.mine_sweeper.new_game()
            if isinstance(action, ActionOpen):
                self.mine_sweeper.open(y=action.y, x=action.x)
            if isinstance(action, ActionFlag):
                self.mine_sweeper.flag(y=action.y, x=action.x)

        exit("END")

    def quit(self):
        self.mine_sweeper.is_playing = False
        self.playing = False

    def game_over(self):
        return self.mine_sweeper.grid.is_lost
