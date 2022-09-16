from Grid import Grid


def _is_playing(decorated_function):
    def newf(self, *args, **kwargs):
        if not self.is_playing:
            raise PartyNotStartedError("Unexpected is playing at False when try to play")
        if self.grid.is_lost:
            raise PartyLostError("Party already lost")
        decorated_function(self, *args, **kwargs)

    return newf


class MineSweeper(object):
    def __init__(self):
        self.is_playing = False
        self.grid = None

    def new_game(self):
        self.is_playing = True
        self.grid = Grid(width=10, height=10)

    @_is_playing
    def open(self, x, y):
        print('open', x, y)
        try:
            self.grid.open(y=y, x=x)
        except IndexError:
            print("Out of range")
        except Exception as e:
            print(e)
        print(self.grid)

    @_is_playing
    def flag(self, x, y):
        print('tag', x, y)
        try:
            self.grid.toggle_flag(x=x, y=y)
        except IndexError:
            print("Out of range")
        except Exception as e:
            print(e)
        print(self.grid)


class PartyNotStartedError(Exception):
    pass


class PartyLostError(Exception):
    pass
