import sys
import math

WALL = '#'

FOLLOW_RIGHT = 'R'

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


class Game:
    def __init__(self):
        self.rows = []
    
    def can_go_right(self, x, y):
        return x < self.width - 1 and self.rows[y][x + 1] != WALL

    def can_go_down(self, x, y):
        return y < self.height - 1 and self.rows[y + 1][x] != WALL

    def can_go_left(self, x, y):
        return x > 0 and self.rows[y][x - 1] != WALL

    def can_go_up(self, x, y):
        return y > 0 and self.rows[y - 1][x] != WALL

    def read_input(self):
        self.width, self.height = map(int, input().split())
        for y in range(self.height):
            line = input()
            self.rows.append([])
            for x in range(self.width):
                if line[x] in DIRECTIONS:
                    self.start = (x, y)
                    self.facing = line[x]
                if line[x] == WALL:
                    self.rows[y].append(WALL)
                else:
                    self.rows[y].append(0)
        follow = input()
        if follow == FOLLOW_RIGHT:
            self.priorities = FOLLOW_RIGHT_PRIORITIES
        else:
            self.priorities = FOLLOW_LEFT_PRIORITIES
        
    def solve(self):
        x = self.start[0]
        y = self.start[1]
        
        while True:
            if (x, y) == self.start and self.rows[y][x] != 0:
                break
            
            priority_list = self.priorities[self.facing]
            previous = (x, y)

            for priority in priority_list:
                if priority == RIGHT:
                    if self.can_go_right(x, y):
                        self.facing = RIGHT
                        x = x + 1
                        break
                elif priority == DOWN:
                    if self.can_go_down(x, y):
                        self.facing = DOWN
                        y = y + 1
                        break
                elif priority == LEFT:
                    if self.can_go_left(x, y):
                        self.facing = LEFT
                        x = x - 1
                        break
                else:
                    if self.can_go_up(x, y):
                        self.facing = UP
                        y = y - 1
                        break

            # check if pikachu is trapped
            if previous == (x, y):
                break
            self.rows[y][x] += 1

        # print solution
        for i in range(self.height):
            for j in range(self.width):
                print(self.rows[i][j], end='')
            print()


if __name__ == "__main__":
    game = Game()
    game.read_input()
    game.solve()
