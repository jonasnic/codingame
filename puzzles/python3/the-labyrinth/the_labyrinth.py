from collections import deque


# Kirk's Possible Moves
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

# Possible ASCII Maze Characters
WALL = '#'
EMPTY = '.'
START = 'T'
CONTROL_ROOM = 'C'
UNKNOWN = '?'


class Game:
    def __init__(self, height, width):
        self.maze_explored = False
        self.control_room_reached = False
        self.height = height
        self.width = width
        self.maze = []
        self.kirk_position = (0, 0)  # (x, y)

    def loop(self):
        while True:
            kirk_y, kirk_x = map(int, input().split())
            self.kirk_position = (kirk_x, kirk_y)
            self.maze = []
            for y in range(height):
                row = input()
                self.maze.append(row)
                for x, c in enumerate(row):
                    if c == CONTROL_ROOM and (x, y) == self.kirk_position:
                        self.control_room_reached = True
            self.play()

    def play(self):
        came_from, neighbor = None, None
        if not self.maze_explored:
            to_avoid = [WALL, CONTROL_ROOM]
            came_from, neighbor = self.bfs(UNKNOWN, to_avoid)
            if came_from is None:
                self.maze_explored = True
        if self.maze_explored:
            to_avoid = [WALL]
            if not self.control_room_reached:
                came_from, neighbor = self.bfs(CONTROL_ROOM, to_avoid)
            else:
                came_from, neighbor = self.bfs(START, to_avoid)
        
        path = self.reconstruct_path(came_from, neighbor)
        next_position = path[-2]
        self.print_next_move(next_position)

    def bfs(self, goal, to_avoid):
        """Compute the shortest path between Kirk and the goal with BFS."""
        visited = set()
        queue = deque()
        came_from = {}  # position => parent position on the shortest path
        queue.append(self.kirk_position)
        visited.add(self.kirk_position)

        while len(queue) != 0:
            position = queue.popleft()
            for neighbor in self.neighbors(position, to_avoid):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    came_from[neighbor] = position
                    neighbor_x, neighbor_y = neighbor
                    if self.maze[neighbor_y][neighbor_x] == goal:
                        return (came_from, neighbor)

        return (None, None)

    def neighbors(self, position, to_avoid):
        neighbors = []
        x, y = position
        if x > 0:
            self.add_neighbor(to_avoid, neighbors, x - 1, y)
        if x < (self.width - 1):
            self.add_neighbor(to_avoid, neighbors, x + 1, y)
        if y > 0:
            self.add_neighbor(to_avoid, neighbors, x, y - 1)
        if y < (self.height - 1):
            self.add_neighbor(to_avoid, neighbors, x, y + 1)
        return neighbors

    def add_neighbor(self, to_avoid, neighbors, x, y):
        if self.maze[y][x] not in to_avoid:
            neighbors.append((x, y))

    def reconstruct_path(self, came_from, neighbor):
        current_position = neighbor
        stack = []
        while current_position in came_from:
            stack.append(current_position)
            current_position = came_from[current_position]
        stack.append(current_position)
        return stack

    def print_next_move(self, next_position):
        kirk_x, kirk_y = self.kirk_position
        next_x, next_y = next_position
        if kirk_x < next_x:
            print(RIGHT)
        elif kirk_x > next_x:
            print(LEFT)
        elif kirk_y < next_y:
            print(DOWN)
        else:
            print(UP)


if __name__ == "__main__":
    height, width, _ = map(int, input().split())
    game = Game(height, width)
    game.loop()
