from typing import List, Optional, Tuple


Position = Tuple[int, int]

STRONG_WALL_SYMBOL = "#"
WEAK_WALL_SYMBOL = "X"
START_SYMBOL = "@"
FINISH_SYMBOL = "$"
SOUTH_SYMBOL = "S"
EAST_SYMBOL = "E"
NORTH_SYMBOL = "N"
WEST_SYMBOL = "W"
BEER_SYMBOL = "B"
INVERTER_SYMBOL = "I"
TELEPORTER_SYMBOL = "T"
EMPTY_SYMBOL = " "

SOUTH = "SOUTH"
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"


class Cell:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.reset()

    def reset(self):
        self.prev_bender_reverse_state: Optional[str] = None
        self.prev_bender_break_mode_state: Optional[str] = None
        self.prev_bender_direction: Optional[str] = None


class Bender:
    def __init__(self):
        self.priorities: List[str] = [SOUTH, EAST, NORTH, WEST]
        self.reverse_state = False
        self.break_mode_state = False
        self.direction = SOUTH
        self.x = 0
        self.y = 0
        self.moves: List[str] = []

    def move(self):
        if self.direction == SOUTH:
            self.y += 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == NORTH:
            self.y -= 1
        elif self.direction == WEST:
            self.x -= 1
        self.moves.append(self.direction)


class Game:
    def __init__(self):
        self.grid: List[List[Cell]] = []
        self.grid_height = 0
        self.grid_width = 0
        self.bender = Bender()
        self.teleporter1: Optional[Position] = None
        self.teleporter2: Optional[Position] = None
        self.loop = False

    @property
    def current_symbol(self) -> str:
        return self.grid[self.bender.y][self.bender.x].symbol

    def reset_grid_state(self):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                self.grid[y][x].reset()

    def is_valid_move(self, direction: str) -> bool:
        if direction == SOUTH:
            return self.is_valid_position(self.bender.x, self.bender.y + 1)
        elif direction == EAST:
            return self.is_valid_position(self.bender.x + 1, self.bender.y)
        elif direction == NORTH:
            return self.is_valid_position(self.bender.x, self.bender.y - 1)
        else:  # WEST
            return self.is_valid_position(self.bender.x - 1, self.bender.y)

    def is_valid_position(self, x: int, y: int) -> bool:
        symbol = self.grid[y][x].symbol
        return all([
            x >= 0 and x < self.grid_width,
            y >= 0 and y < self.grid_height,
            symbol != STRONG_WALL_SYMBOL and (symbol != WEAK_WALL_SYMBOL or self.bender.break_mode_state),
        ])

    def update_bender_state(self):
        if self.current_symbol == SOUTH_SYMBOL:
            self.bender.direction = SOUTH
        elif self.current_symbol == EAST_SYMBOL:
            self.bender.direction = EAST
        elif self.current_symbol == NORTH_SYMBOL:
            self.bender.direction = NORTH
        elif self.current_symbol == WEST_SYMBOL:
            self.bender.direction = WEST
        elif self.current_symbol == BEER_SYMBOL:
            self.bender.break_mode_state = not self.bender.break_mode_state
        elif self.current_symbol == INVERTER_SYMBOL:
            self.bender.reverse_state = not self.bender.reverse_state
            self.bender.priorities.reverse()
        elif self.current_symbol == TELEPORTER_SYMBOL:
            if (self.bender.x, self.bender.y) == self.teleporter1:
                self.bender.x, self.bender.y = self.teleporter2
            elif (self.bender.x, self.bender.y) == self.teleporter2:
                self.bender.x, self.bender.y = self.teleporter1

    def move_bender(self):
        self.update_bender_state()

        if not self.is_valid_move(self.bender.direction):
            for direction in self.bender.priorities:
                if self.is_valid_move(direction):
                    self.bender.direction = direction
                    self.bender.move()
                    break
        else:
            self.bender.move()

        cell = self.grid[self.bender.y][self.bender.x]
        cell_state = (cell.prev_bender_reverse_state, cell.prev_bender_break_mode_state, cell.prev_bender_direction)
        bender_state = (self.bender.reverse_state, self.bender.break_mode_state, self.bender.direction)
        if cell_state != bender_state:
            cell.prev_bender_reverse_state = self.bender.reverse_state
            cell.prev_bender_break_mode_state = self.bender.break_mode_state
            cell.prev_bender_direction = self.bender.direction
        else:
            self.loop = True


def read_input_data(game):
    game.grid_height, game.grid_width = map(int, input().split())

    for y in range(game.grid_height):
        row = input()
        cell_list: List[Cell] = []
        for x, symbol in enumerate(row):
            cell = Cell(symbol)
            cell_list.append(cell)
            if symbol == START_SYMBOL:
                game.bender.x = x
                game.bender.y = y
            elif symbol == TELEPORTER_SYMBOL:
                if game.teleporter1 is None:
                    game.teleporter1 = (x, y)
                elif game.teleporter2 is None:
                    game.teleporter2 = (x, y)
        game.grid.append(cell_list)


if __name__ == "__main__":
    game = Game()
    read_input_data(game)

    while game.current_symbol != FINISH_SYMBOL:
        game.move_bender()
        if game.loop:
            break
        if game.bender.break_mode_state and game.current_symbol == WEAK_WALL_SYMBOL:
            game.grid[game.bender.y][game.bender.x] = Cell(EMPTY_SYMBOL)
            game.reset_grid_state()

    if not game.loop:
        for move in game.bender.moves:
            print(move)
    else:
        print("LOOP")
