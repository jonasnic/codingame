#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const int EXIT = -1; // room number for the exit
const int START = 0; // index of the start room
const int DOORS_PER_ROOM = 2;

class Room {
  public:
    int number, money, depth;
    int doors[DOORS_PER_ROOM];

    Room(int n, int m, string door1, string door2) : number(n), money(m) {
      depth = -1;
      readDoor(door1, 0);
      readDoor(door2, 1);
    }

    Room(const Room& other) : number(other.number), money(other.money), depth(other.depth) {
      doors[0] = other.doors[0];
      doors[1] = other.doors[1];
    }

    ~Room() {}

    Room& operator = (const Room& other) {
      if (this != &other) {
        number = other.number;
        money = other.money;
        depth = other.depth;
        doors[0] = other.doors[0];
        doors[1] = other.doors[1];
      }
      return *this;
    }

    bool operator < (const Room& other) const {
      return depth < other.depth;
    }

  private:
    void readDoor(string door, int index) {
      if (door == "E") {
        doors[index] = EXIT;
      } else {
        doors[index] = stoi(door);
      }
    }
};

class Building {
  public:
    vector<Room> rooms;

    void readRooms() {
      int nbRooms;
      cin >> nbRooms; cin.ignore();
      for (int i = 0; i < nbRooms; i++) {
        int number, money;
        string door1, door2;
        cin >> number >> money >> door1 >> door2;
        Room room(number, money, door1, door2);
        rooms.push_back(room);
      }
    }

    void calcMaxDepth(Room& room, int parentDepth) {
      room.depth = parentDepth + 1;
      for (int i = 0; i < DOORS_PER_ROOM; i++) {
        int door = room.doors[i];
        if (door != EXIT) {
          Room& neighbor = rooms[door];
          if (neighbor.depth <= room.depth) {
            calcMaxDepth(neighbor, room.depth);
          }
        }
      }
    }

    int maxMoney() {
      priority_queue<Room> unvisited;
      vector<int> money;
      for (unsigned i = 0; i < rooms.size(); i++) {
        money.push_back(0);
        unvisited.push(rooms[i]);
      }

      int count = 0;
      // loop through each depth level of the tree in descending order
      while (!unvisited.empty()) {
        // find max depth
        const Room& maxRoom = unvisited.top();
        int maxNumber = maxRoom.number;
        // find the best path for each subproblem
        int nextNumber = nextDoor(maxNumber, money);
        money[maxNumber] = maxRoom.money;
        if (nextNumber != EXIT) {
          money[maxNumber] += money[nextNumber];
        }
        unvisited.pop();
      }

      return money[START];
    }

  private:
    int nextDoor(int maxNumber, vector<int>& money) {
      int door1 = rooms[maxNumber].doors[0];
      int door2 = rooms[maxNumber].doors[1];
      if (door1 == EXIT) {
        return door2;
      } else if (door2 == EXIT) {
        return door1;
      } else if (money[door1] > money[door2]) {
        return door1;
      }
      return door2;
    }
};

int main() {
  Building building;
  building.readRooms();
  // Calculate the max depth of each room reachable from the start with DFS
  building.calcMaxDepth(building.rooms[START], -1);
  cout << building.maxMoney() << endl;
}
