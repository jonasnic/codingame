import heapq

EXIT = -1  # room number for the exit
START = 0  # index of the start room


class Room:
    """each room is a node of the tree"""
    def __init__(self, number, money, door1, door2):
        self.number = number
        self.money = money
        self.doors = []
        self.read_door(door1)
        self.read_door(door2)
        self.depth = -1

    def read_door(self, door):
        if door == "E":
            self.doors.append(EXIT)
        else:
            self.doors.append(int(door))

    def __lt__(self, other):
        """reversed operator for max heap"""
        return other.depth < self.depth


class Building:
    """tree representation of the building"""
    def __init__(self):
        self.rooms = []

    def read_rooms(self):
        nb_rooms = int(input())
        for i in range(nb_rooms):
            number, money, door1, door2 = input().split()
            room = Room(int(number), int(money), door1, door2)
            self.rooms.append(room)

    def calc_max_depth(self, room, parent_depth):
        room.depth = parent_depth + 1
        for door in room.doors:
            if door != EXIT:
                neighbor = self.rooms[door]
                if neighbor.depth <= room.depth:
                    self.calc_max_depth(neighbor, room.depth)

    def max_money(self):
        """
        Find the path with the max total money.
        (inspired by Dijkstra's algorithm)
        """
        unvisited = []  # heap used as a priority queue
        money = []  # maximum known money down each path
        for number in range(len(self.rooms)):
            money.append(0)  # initial money
            heapq.heappush(unvisited, self.rooms[number])

        # loop through each depth level of the tree in descending order
        while len(unvisited) != 0:
            # find max depth
            max_room = heapq.heappop(unvisited)
            max_number = max_room.number
            # find the best path for each subproblem
            next_number = self.next_door(max_number, money)
            money[max_number] = max_room.money
            if next_number != EXIT:
                money[max_number] += money[next_number]
        return money[START]

    def next_door(self, max_number, money):
        door1 = self.rooms[max_number].doors[0]
        door2 = self.rooms[max_number].doors[1]
        if door1 == EXIT:
            return door2
        elif door2 == EXIT:
            return door1
        elif money[door1] > money[door2]:
            return door1
        return door2


building = Building()
building.read_rooms()
# Calculate the max depth of each room reachable from the start with DFS
building.calc_max_depth(building.rooms[START], -1)
print(building.max_money())
