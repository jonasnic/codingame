import sys
from collections import deque

WALL = '#'
BEGINNING = 'T'
CONTROL_ROOM = 'C'
UNKNOWN = '?'


class Maze:
    def __init__(self):
        self.grid = []
        self.nb_rows = 0
        self.nb_columns = 0
        self.kirk = (0, 0)  # (x, y)
        self.start = (0, 0)
        self.control_room = (0, 0)
        self.explore = True
        self.control_room_reached = False

    def read_init_input(self):
        self.nb_rows, self.nb_columns, rounds = map(int, input().split())
        for y in range(self.nb_rows):
            row = []
            for x in range(self.nb_columns):
                row.append(UNKNOWN)
            self.grid.append(row)

    def game_loop(self):
        while True:
            self.kirk = tuple(map(int, reversed(input().split())))
            self.update_grid()

            if self.kirk == self.control_room:
                self.control_room_reached = True

            if self.explore:
                # explore the maze
                # until every unknown position is discovered
                result = self.search(self.kirk, UNKNOWN)
                if result is None:
                    self.explore = False
                    self.go_somewhere()
                else:
                    self.print_next_move(result)
            else:
                self.go_somewhere()

    def update_grid(self):
        for y in range(self.nb_rows):
            row = input()  # row of the ASCII maze
            for x, c in enumerate(row):
                self.grid[y][x] = c
                if c == BEGINNING:
                    self.start = (x, y)
                elif c == CONTROL_ROOM:
                    self.control_room = (x, y)

    def go_somewhere(self):
        if not self.control_room_reached:
            # go to the control room
            result = self.search(self.kirk, CONTROL_ROOM)
            self.print_next_move(result)
        else:
            # go back to the start
            result = self.search(self.kirk, BEGINNING)
            self.print_next_move(result)

    def print_next_move(self, result):
        parents, current = result
        next_position = (0, 0)
        # go back to Kirk
        if result is not None:
            while current != self.kirk:
                next_position = current
                current = parents.get(current, (0, 0))

        # Kirk's next move
        if self.kirk[0] < next_position[0]:
            print("RIGHT")
        elif self.kirk[0] > next_position[0]:
            print("LEFT")
        elif self.kirk[1] < next_position[1]:
            print("DOWN")
        else:
            print("UP")

    # BFS from start until goal is reached
    def search(self, start, goal):
        visited = set()
        queue = deque()
        parents = {}  # (x, y): parent
        visited.add(start)
        queue.append(start)

        while len(queue) != 0:
            current = queue.popleft()
            if self.grid[current[1]][current[0]] == goal:
                return (parents, current)
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parents[neighbor] = current
        return None

    def neighbors(self, pos):
        positions = []
        self.add(positions, (pos[0] + 1, pos[1]))
        self.add(positions, (pos[0], pos[1] + 1))
        self.add(positions, (pos[0] - 1, pos[1]))
        self.add(positions, (pos[0], pos[1] - 1))
        return positions

    def add(self, positions, pos):
        if self.is_valid(pos):
            positions.append(pos)

    def is_valid(self, pos):
        c = self.grid[pos[1]][pos[0]]
        valid_x = pos[0] >= 0 and pos[0] < self.nb_columns
        valid_y = pos[1] >= 0 and pos[1] <= self.nb_rows
        return c != WALL and valid_x and valid_y


maze = Maze()
maze.read_init_input()
maze.game_loop()
