#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void printNextRoom(int roomType, int x, int y, string entrance) {
  if (roomType == 2 || roomType == 6) {
    if (entrance == "LEFT") {
      x++;
    } else {
      x--;
    }
  } else if (roomType == 4) {
    if (entrance == "TOP") {
      x--;
    } else {
      y++;
    }
  } else if (roomType == 5) {
    if (entrance == "TOP") {
      x++;
    } else {
      y++;
    }
  } else if (roomType == 10) {
    x--;
  } else if (roomType == 11) {
    x++;
  } else {
    y++;
  }
  
  cout << x << " " << y << endl;
}

int main() {
  vector<int> rooms;
  int nbColumns;
  int nbRows;
  cin >> nbColumns >> nbRows; cin.ignore();
  for (int i = 0; i < nbRows; i++) {
    string line;
    getline(cin, line);
    istringstream stream(line);
    int room;
    while (stream >> room) {
      rooms.push_back(room);
    }
  }
  int ex;
  cin >> ex; cin.ignore();

  // game loop
  while (true) {
    int x, y;
    string entrance;
    cin >> x >> y >> entrance; cin.ignore();
    printNextRoom(rooms[y * nbColumns + x], x, y, entrance);
  }
}
