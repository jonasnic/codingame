WALL = '#'

FOLLOW_RIGHT = 'R'
FOLLOW_LEFT = 'L'

RIGHT = '>'
DOWN = 'v'
LEFT = '<'
UP = '^'

DIRECTIONS = {RIGHT, DOWN, LEFT, UP,}

FOLLOW_RIGHT_PRIORITIES = {
    UP: [RIGHT, UP, LEFT, DOWN],
    DOWN: [LEFT, DOWN, RIGHT, UP],
    RIGHT: [DOWN, RIGHT, UP, LEFT],
    LEFT: [UP, LEFT, DOWN, RIGHT],
}

FOLLOW_LEFT_PRIORITIES = {
    UP: [LEFT, UP, RIGHT, DOWN],
    DOWN: [RIGHT, DOWN, LEFT, UP],
    RIGHT: [UP, RIGHT, DOWN, LEFT],
    LEFT: [DOWN, LEFT, UP, RIGHT],
}


class Pikachu():
    def __init__(self):
        self.start = (0, 0)
        self.previous = (0, 0)
        self.x = 0
        self.y = 0
        self.facing = ''
        self.priorities = {}

    def is_trapped(self):
        return self.previous == (self.x, self.y)


class Game:
    def __init__(self):
        self.rows = []
        self.width = 0
        self.height = 0
        self.pikachu = Pikachu()

    def read_input(self):
        self.width, self.height = map(int, input().split())
        for y in range(self.height):
            line = input()
            self.rows.append([])
            for x in range(self.width):
                if line[x] in DIRECTIONS:
                    self.pikachu.start = (x, y)
                    self.pikachu.x = x
                    self.pikachu.y = y
                    self.pikachu.facing = line[x]
                if line[x] == WALL:
                    self.rows[y].append(WALL)
                else:
                    self.rows[y].append(0)
        follow = input()
        if follow == FOLLOW_RIGHT:
            self.pikachu.priorities = FOLLOW_RIGHT_PRIORITIES
        elif follow == FOLLOW_LEFT:
            self.pikachu.priorities = FOLLOW_LEFT_PRIORITIES

    def solve(self):
        while not self.is_pikachu_back_at_the_start():
            priority_list = self.pikachu.priorities[self.pikachu.facing]
            self.pikachu.previous = (self.pikachu.x, self.pikachu.y)

            for priority in priority_list:
                if priority == RIGHT:
                    if self.pikachu_can_go_right():
                        self.pikachu.facing = RIGHT
                        self.pikachu.x += 1
                        break
                elif priority == DOWN:
                    if self.pikachu_can_go_down():
                        self.pikachu.facing = DOWN
                        self.pikachu.y += 1
                        break
                elif priority == LEFT:
                    if self.pikachu_can_go_left():
                        self.pikachu.facing = LEFT
                        self.pikachu.x -= 1
                        break
                else:
                    if self.pikachu_can_go_up():
                        self.pikachu.facing = UP
                        self.pikachu.y -= 1
                        break

            if self.pikachu.is_trapped():
                break
            self.rows[self.pikachu.y][self.pikachu.x] += 1

    def is_pikachu_back_at_the_start(self):
        x, y = self.pikachu.x, self.pikachu.y
        return (x, y) == self.pikachu.start and self.rows[y][x] != 0

    def pikachu_can_go_down(self):
        x, y = self.pikachu.x, self.pikachu.y
        return y < self.height - 1 and self.rows[y + 1][x] != WALL

    def pikachu_can_go_left(self):
        x, y = self.pikachu.x, self.pikachu.y
        return x > 0 and self.rows[y][x - 1] != WALL

    def pikachu_can_go_right(self):
        x, y = self.pikachu.x, self.pikachu.y
        return x < self.width - 1 and self.rows[y][x + 1] != WALL

    def pikachu_can_go_up(self):
        x, y = self.pikachu.x, self.pikachu.y
        return y > 0 and self.rows[y - 1][x] != WALL

    def print_solution(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.rows[y][x], end='')
            print()

if __name__ == "__main__":
    game = Game()
    game.read_input()
    game.solve()
    game.print_solution()
