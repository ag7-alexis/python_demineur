import random
from typing import List, Optional

from Tile import TileHint, TileMine, Tile


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrices: List[List[Tile]] = [[TileHint(x=x, y=y, grid=self) for x in range(width)] for y in range(height)]
        self.coordinates = [(y, x) for y in range(height) for x in range(width)]
        count_tiles = self.width * self.height
        self.number_of_mines = count_tiles // 10
        self.remaining = count_tiles - self.number_of_mines
        self.is_lost = False
        self._mines_coord()

    def _mines_coord(self):
        mines_coordinates = random.sample(self.coordinates, self.number_of_mines)

        for y, x in mines_coordinates:
            self.matrices[y][x] = TileMine(x=x, y=y, grid=self)

    def get_tile(self, y, x) -> Optional[Tile]:
        try:
            if x not in range(0, self.width) or y not in range(0, self.height):
                return None
            return self.matrices[y][x]
        except IndexError:
            return None

    def open(self, y, x):
        tile = self.matrices[y][x]

        if tile.is_flagged:
            raise Exception("Tile already flaged")

        tile.open()
        if isinstance(tile, TileMine):
            self.is_lost = True
        else:
            self.remaining = -1

    def toggle_flag(self, y, x):
        tile = self.matrices[y][x]
        if tile.is_open:
            raise Exception("Tile already opened")

        tile.is_flagged = not tile.is_flagged

    def is_win(self):
        return self.remaining == 0

    def _open_full(self, target_y, target_x):
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                tile_y = target_y + y
                tile_x = target_x + x
                tile: TileHint = self.get_tile(y=tile_y, x=tile_x)
                tile.open()
                if tile.hint == 0:
                    self._open_full(target_y=tile_y, target_x=tile_x)

    def __str__(self):
        grid = ""
        line = 1
        for x in self.coordinates:
            if x[0] == line:
                grid += "\n"
                line += 1
            grid += str(self.matrices[x[0]][x[1]])

        return grid
