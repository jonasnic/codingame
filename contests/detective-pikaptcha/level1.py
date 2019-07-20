import sys
import math

PASSAGE = '0'
WALL = '#'


class Game:
    def __init__(self):
        self.rows = []
    
    def adjacent_passable_cells(self, i, j):
        count = 0
        if i > 0 and self.rows[i - 1][j] != WALL:
            count += 1
        if i < self.height - 1 and self.rows[i + 1][j] != WALL:
            count += 1
        if j > 0 and self.rows[i][j - 1] != WALL:
            count += 1
        if j < self.width - 1 and self.rows[i][j + 1] != WALL:
            count += 1
        return count
        
    def read_input(self):
        self.width, self.height = map(int, input().split())
        rows = []
        for _ in range(self.height):
            self.rows.append(input())
            
    def solve(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.rows[i][j] == WALL:
                    print(WALL, end='')
                else:
                    print(self.adjacent_passable_cells(i, j), end='')
            print()


if __name__ == "__main__":
    game = Game()
    game.read_input()
    game.solve()
