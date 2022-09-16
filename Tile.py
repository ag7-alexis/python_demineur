class Tile:
    def __init__(self, x, y, grid, is_open=False, is_flagged=False):
        self.x = x
        self.y = y
        self.is_open = is_open
        self.is_flagged = is_flagged
        self.grid = grid

    def __str__(self):
        if self.is_flagged:
            return "F"
        if not self.is_open:
            return "#"

        raise NotImplementedError

    def open(self):
        if self.is_open:
            raise Exception("Tile already opened")
        self.is_open = True


class TileMine(Tile):
    def __init__(self, x, y, grid, is_open=False, is_flagged=False):
        super(TileMine, self).__init__(x, y, grid, is_open, is_flagged)

    def __str__(self):
        if not self.is_open:
            return super(TileMine, self).__str__()
        return "💣"


class TileHint(Tile):
    def __init__(self, x, y, grid, is_open=False, is_flagged=False):
        super(TileHint, self).__init__(x, y, grid, is_open, is_flagged)
        self._hint = None

    @property
    def hint(self):
        if self._hint is not None:
            return self._hint
        count_mines = 0
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                tile = self.grid.get_tile(y=y + self.y, x=x + self.x)
                if isinstance(tile, TileMine):
                    count_mines += 1
        self._hint = str(count_mines)
        return str(count_mines)

    def open(self):
        if self._hint != 0:
            return

        self.grid._open_full()


    def __str__(self):
        if not self.is_open:
            return super(TileHint, self).__str__()
        return self.hint
