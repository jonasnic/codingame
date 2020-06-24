import copy

EMPTY = '.'
TARGET = '@'
WALL = '#'
EXPLOSION_TIME = 3
BOMB_RANGE = 3


class Node:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.destroy = False
        self.time_to_detonation = EXPLOSION_TIME
        self.invalid = False

    def is_valid_target(self):
        return self.char == TARGET and not self.destroy

    def is_valid_future_bomb_placement(self):
        return (not self.invalid and (self.char == EMPTY or
                (self.char == TARGET and self.destroy)))

    def update(self):
        if (self.char == TARGET and self.destroy):
            self.time_to_detonation -= 1
            if (self.time_to_detonation == 0):
                self.char = EMPTY


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def destroy(self, x, y):
        self.nodes[y][x].destroy = True

    def is_valid_target(self, x, y):
        return self.nodes[y][x].is_valid_target()

    def is_valid_future_bomb_placement(self, x, y):
        return self.nodes[y][x].is_valid_future_bomb_placement()

    def is_destroyed(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.nodes[y][x].char == TARGET:
                    return False
        return True

    def update(self):
        for y in range(self.height):
            for x in range(self.width):
                self.nodes[y][x].update()

    # greedy solution: pick the bomb placement with the highest score
    def pick_bomb_placement(self):
        max_score = 0
        max_node = None
        for y in range(self.height):
            for x in range(self.width):
                if self.is_valid_future_bomb_placement(x, y):
                    score = self.place_bomb_score(x, y)
                    if score > max_score:
                        max_score = score
                        max_node = self.nodes[y][x]
        return max_node

    # update the state of the grid
    # Precondition: The node at (x, y) should be a valid target.
    def place_bomb(self, x, y):
        # BOTTOM
        for i in range(y + 1, y + (BOMB_RANGE + 1)):
            if i >= self.height:
                break
            if self.is_valid_target(x, i):
                self.destroy(x, i)
            elif self.nodes[i][x].char == WALL:
                break

        # TOP
        for j in range(y - 1, y - (BOMB_RANGE + 1), -1):
            if j < 0:
                break
            if self.is_valid_target(x, j):
                self.destroy(x, j)
            elif self.nodes[j][x].char == WALL:
                break

        # RIGHT
        for k in range(x + 1, x + (BOMB_RANGE + 1)):
            if k >= self.width:
                break
            if self.is_valid_target(k, y):
                self.destroy(k, y)
            elif self.nodes[y][k].char == WALL:
                break

        # LEFT
        for m in range(x - 1, x - (BOMB_RANGE + 1), -1):
            if m < 0:
                break
            if self.is_valid_target(m, y):
                self.destroy(m, y)
            elif self.nodes[y][m].char == WALL:
                break

    # score = number of targets destroyed
    # Precondition: The node at (x, y) should be a valid target.
    def place_bomb_score(self, x, y):
        score = 0

        # BOTTOM
        for i in range(y + 1, y + (BOMB_RANGE + 1)):
            if i >= self.height:
                break
            if self.is_valid_target(x, i):
                score += 1
            elif self.nodes[i][x].char == WALL:
                break

        # TOP
        for j in range(y - 1, y - (BOMB_RANGE + 1), -1):
            if j < 0:
                break
            if self.is_valid_target(x, j):
                score += 1
            elif self.nodes[j][x].char == WALL:
                break

        # RIGHT
        for k in range(x + 1, x + (BOMB_RANGE + 1)):
            if k >= self.width:
                break
            if self.is_valid_target(k, y):
                score += 1
            elif self.nodes[y][k].char == WALL:
                break

        # LEFT
        for m in range(x - 1, x - (BOMB_RANGE + 1), -1):
            if m < 0:
                break
            if self.is_valid_target(m, y):
                score += 1
            elif self.nodes[y][m].char == WALL:
                break

        return score


class VoxCodei:
    def __init__(self):
        self.grid = None
        self.nb_rounds = 0  # number of rounds left before the end of the game
        self.nb_bombs = 0  # number of bombs left
        self.round = 1

    def read_init_input(self):
        width, height = [int(i) for i in input().split()]
        self.grid = Grid(width, height)
        for y in range(height):
            map_row = input()
            row = []
            self.grid.nodes.append(row)
            for x, char in enumerate(map_row):
                self.grid.nodes[y].append(Node(x, y, char))

    def game_loop(self):
        while True:
            self.nb_rounds, self.nb_bombs = [int(i) for i in input().split()]
            self.play_turn()
            self.round += 1

    def play_turn(self):
        node = self.grid.pick_bomb_placement()

        # simulate everything fox max, if it doesn't work out, backtrack
        if node is not None and self.round == 1:
            if not self.simulate_turn(node.x, node.y):
                node.invalid = True
                node = self.grid.pick_bomb_placement()

        # validate bomb placement for next turn
        if node is None or node.char != EMPTY:
            print("WAIT")  # wait until it gets destroyed
        else:
            self.grid.place_bomb(node.x, node.y)
            print("{} {}".format(node.x, node.y))

        self.grid.update()

    def simulate_turn(self, x, y):
        bombs = self.nb_bombs
        rounds = self.nb_rounds
        grid_copy = copy.deepcopy(self.grid)
        current = grid_copy.nodes[y][x]

        while bombs != 0 and rounds != 0 and not grid_copy.is_destroyed():
            if current is not None and current.char == EMPTY:
                grid_copy.place_bomb(current.x, current.y)
                bombs -= 1
            grid_copy.update()
            rounds -= 1
            current = grid_copy.pick_bomb_placement()

        while rounds != 0 and not grid_copy.is_destroyed():
            grid_copy.update()
            rounds -= 1

        return grid_copy.is_destroyed()


vox_codei = VoxCodei()
vox_codei.read_init_input()
vox_codei.game_loop()
