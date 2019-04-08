STRONG_WALL = "#"
WEAK_WALL = "X"
START = "@"
FINISH = "$"
SOUTH = "S"
EAST = "E"
NORTH = "N"
WEST = "W"
BEER = "B"
INVERTER = "I"
TELEPORTER = "T"
EMPTY = " "


class Cell:
    def __init__(self, symbol):
        self.symbol = symbol
        self.reset()

    def reset(self):
        self.reverse = None
        self.break_mode = None
        self.direction = None


class Bender:
    def __init__(self):
        self.priorities = ["SOUTH", "EAST", "NORTH", "WEST"]
        self.direction = "SOUTH"
        self.reverse = False
        self.break_mode = False
        self.x = 0
        self.y = 0
        self.moves = []

    def add_move(self):
        if self.direction == "SOUTH":
            self.y += 1
        elif self.direction == "EAST":
            self.x += 1
        elif self.direction == "NORTH":
            self.y -= 1
        else:  # WEST
            self.x -= 1
        self.moves.append(self.direction)


class City:
    def __init__(self):
        self.teleporter1 = None
        self.teleporter2 = None
        self.height = 0
        self.width = 0
        self.loop = False


grid = []
bender = Bender()
city = City()


def read_game_input():
    city.height, city.width = [int(i) for i in input().split()]

    for y in range(city.height):
        row = input()
        cell_list = []
        for x, symbol in enumerate(row):
            cell = Cell(symbol)
            cell_list.append(cell)
            if symbol == START:
                bender.x = x
                bender.y = y
            elif symbol == TELEPORTER:
                if city.teleporter1 is None:
                    city.teleporter1 = (x, y)
                else:
                    city.teleporter2 = (x, y)
        grid.append(cell_list)


def reset_grid_state():
    for y in range(city.height):
        for x in range(city.width):
            grid[y][x].reset()


def current_symbol():
    return grid[bender.y][bender.x].symbol


def is_valid_move(direction):
    if direction == "SOUTH":
        return is_valid_position(bender.x, bender.y + 1)
    elif direction == "EAST":
        return is_valid_position(bender.x + 1, bender.y)
    elif direction == "NORTH":
        return is_valid_position(bender.x, bender.y - 1)
    else:  # WEST
        return is_valid_position(bender.x - 1, bender.y)


def is_valid_position(x, y):
    s = grid[y][x].symbol
    x_valid = x >= 0 and x < city.width
    y_valid = y >= 0 and y < city.height
    s_valid = s != STRONG_WALL and (s != WEAK_WALL or bender.break_mode)
    return x_valid and y_valid and s_valid


def update_bender_state():
    if current_symbol() in (START, SOUTH):
        bender.direction = "SOUTH"
    elif current_symbol() == EAST:
        bender.direction = "EAST"
    elif current_symbol() == NORTH:
        bender.direction = "NORTH"
    elif current_symbol() == WEST:
        bender.direction = "WEST"
    elif current_symbol() == BEER:
        bender.break_mode = not bender.break_mode
    elif current_symbol() == INVERTER:
        bender.reverse = not bender.reverse
        bender.priorities.reverse()
    elif current_symbol() == TELEPORTER:
        if (bender.x, bender.y) == city.teleporter1:
            bender.x, bender.y = city.teleporter2
        else:
            bender.x, bender.y = city.teleporter1


def add_move():
    update_bender_state()

    if is_valid_move(bender.direction):
        bender.add_move()
    else:
        for direction in bender.priorities:
            if is_valid_move(direction):
                bender.direction = direction
                bender.add_move()
                break

    cell = grid[bender.y][bender.x]
    cell_state = (cell.reverse, cell.break_mode, cell.direction)
    bender_state = (bender.reverse, bender.break_mode, bender.direction)
    if cell_state == bender_state:
        city.loop = True
    else:
        cell.reverse = bender.reverse
        cell.break_mode = bender.break_mode
        cell.direction = bender.direction


def game_loop():
    while current_symbol() != FINISH:
        add_move()

        if city.loop:
            break

        if bender.break_mode and current_symbol() == WEAK_WALL:
            grid[bender.y][bender.x] = Cell(EMPTY)
            reset_grid_state()

    if city.loop:
        print("LOOP")
    else:
        for move in bender.moves:
            print(move)


read_game_input()
game_loop()
