// The Last Crusade - Episode 2

import java.util.*;

class Player {
  public static void main(String args[]) {
    Crusade crusade = new Crusade();
    crusade.readInitInput();
    crusade.gameLoop();
  }
}

class Crusade {
  final int DEFAULT_COORDINATE = -1;
  final String TOP = "TOP";
  final String LEFT = "LEFT";
  final String RIGHT = "RIGHT";

  Scanner in = new Scanner(System.in);
  int rooms[][]; // [y][x]
  int width; // number of columns
  int height; // number of rows
  int xExit;

  void readInitInput() {
    width = in.nextInt();
    height = in.nextInt();
    if (in.hasNextLine())
      in.nextLine();

    rooms = new int[height][width];

    for (int y = 0; y < height; ++y) {
      String[] roomTypes = in.nextLine().split(" ");
      for (int x = 0; x < width; ++x) {
        rooms[y][x] = Integer.parseInt(roomTypes[x]);
      }
    }
    xExit = in.nextInt();
  }

  void gameLoop() {
    // game loop
    while (true) {
      int x = in.nextInt();
      int y = in.nextInt();
      String from = in.next();
      Node indy = new Node(x, y, from);
      Node exit = new Node(xExit, height - 1);

      Node end = search(indy, exit);
      List<Node> path = generatePath(end);
      Command command = computePathRotation(path);
      command = computeRockRotation(path, command);

      if (command != null)
        System.out.println(command.toString());
      else
        System.out.println("WAIT");
    }
  }

  // compute rotation to open a path to the exit if necessary
  Command computePathRotation(List<Node> path) {
    for (Node current : path) {
      if (current.entry.rotation != Rotation.NONE) {
        Command command = new Command();
        command.rotationNode = current;
        command.clockWise = current.entry.rotation != Rotation.COUNTERCLOCKWISE;
        command.xRotation = current.x;
        command.yRotation = current.y;
        return command;
      }
    }
    return null;
  }

  // compute rotation to block a rock if necessary
  Command computeRockRotation(List<Node> path, Command command) {
    List<Rock> rocks = new ArrayList<>();
    List<Rock> rocksCopy = new ArrayList<>(); // original state of the rocks
    int nbRocks = in.nextInt(); // the number of rocks currently in the grid.
    for (int i = 0; i < nbRocks; i++) {
      int xRock = in.nextInt();
      int yRock = in.nextInt();
      String entryRock = in.next();
      Rock rock = new Rock(xRock, yRock, entryRock);
      rocks.add(rock);
      rocksCopy.add(new Rock(rock));
    }

    if (command == null ||
        command.rotationNode.distance > 1 &&
            (command.rotationNode.entry.rotation == Rotation.CLOCKWISE ||
                command.rotationNode.entry.rotation == Rotation.COUNTERCLOCKWISE) ||
        command.rotationNode.distance > 2 &&
            command.rotationNode.entry.rotation == Rotation.DOUBLE_CLOCKWISE) {
      // for all cells on the path to the exit
      for (int i = 0; i < path.size(); ++i) {
        int x = path.get(i).x;
        int y = path.get(i).y;

        // update each rock's state for this turn
        for (int j = 0; j < rocks.size(); ++j) {
          Rock rock = rocks.get(j);
          String entry = nextEntry(type(rock), rock.entry.from);
          update(rock, entry);

          // collision?
          if (rock.x == x && rock.y == y && !rock.ignore) {
            Rock rockCopy = new Rock(rocksCopy.get(j));
            while (rockCopy.x != x || rockCopy.y != y) {
              entry = nextEntry(type(rockCopy), rockCopy.entry.from);
              update(rockCopy, entry);

              // if we can't block it before it reaches Indy's path, ignore it
              if (rockCopy.x == x && rockCopy.y == y)
                break;

              if (type(rockCopy) > 1) {
                if (command == null)
                  command = new Command();
                command.xRotation = rockCopy.x;
                command.yRotation = rockCopy.y;
                command.clockWise = true; // doesn't matter for episode 2, could take type into account
                return command;
              }
            }
          }
        }
      }
    }

    return command;
  }

  private void update(Rock rock, String entry) {
    switch (entry) {
      case LEFT:
        rock.x += 1;
        rock.entry.from = LEFT;
        break;
      case RIGHT:
        rock.x -= 1;
        rock.entry.from = RIGHT;
        break;
      case TOP:
        rock.y += 1;
        rock.entry.from = TOP;
    }
  }

  // Compute a path between start and exit using DFS
  Node search(Node start, Node exit) {
    // initialize the grid
    Cell[][] cells = new Cell[height][width];
    for (int y = 0; y < height; ++y)
      for (int x = 0; x < width; ++x)
        cells[y][x] = new Cell(x, y);
    Stack<Node> stack = new Stack<>();
    Cell startCell = cells[start.y][start.x];
    startCell.visited.add(start.entry.from);
    start.distance = 0;
    stack.push(start);

    while (!stack.isEmpty()) {
      Node current = stack.pop();
      if (current.parent != null)
        current.parent.entry.rotation = current.entry.parentRotation;
      if (current.equalPosition(exit))
        return current;
      for (Node neighbor : neighbors(cells, current)) {
        stack.push(neighbor);
      }
    }
    return null;
  }

  List<Node> generatePath(Node end) {
    List<Node> list = new ArrayList<>();
    Node current = end;
    while (current.parent != null) {
      list.add(0, current);
      current = current.parent;
    }
    return list;
  }

  String nextEntry(int type, String entry) {
    switch (Math.abs(type)) {
      case 1:
        return TOP;
      case 2:
      case 6:
        if (entry.equals(LEFT)) return LEFT;
        else if (entry.equals(RIGHT)) return RIGHT;
        break;
      case 3:
        if (entry.equals(TOP)) return TOP;
        break;
      case 4:
        if (entry.equals(TOP)) return RIGHT;
        else if (entry.equals(RIGHT)) return TOP;
        break;
      case 5:
        if (entry.equals(TOP)) return LEFT;
        else if (entry.equals(LEFT)) return TOP;
        break;
      case 7:
        if (entry.equals(TOP) || entry.equals(RIGHT)) return TOP;
        break;
      case 8:
        if (entry.equals(LEFT) || entry.equals(RIGHT)) return TOP;
        break;
      case 9:
        if (entry.equals(TOP) || entry.equals(LEFT)) return TOP;
        break;
      case 10:
        if (entry.equals(TOP)) return RIGHT;
        break;
      case 11:
        if (entry.equals(TOP)) return LEFT;
        break;
      case 12:
        if (entry.equals(RIGHT)) return TOP;
        break;
      case 13:
        if (entry.equals(LEFT)) return TOP;
        break;
    }
    return "";
  }

  List<Entry> nextEntries(Node current) {
    List<Entry> entries = new ArrayList<>();
    int type = type(current);
    String prevEntry = current.entry.from;

    String from1 = nextEntry(type, prevEntry);
    entries.add(new Entry(from1));

    if (current.distance > 0) {
      if (type > 1) {
        String from2 = nextEntry(rotateClockwise(type), prevEntry);
        Entry entry2 = new Entry(from2);
        entry2.parentRotation = Rotation.CLOCKWISE;
        entries.add(entry2);
      }
      if (type > 5) {
        String from3 = nextEntry(rotateCounterclockwise(type), prevEntry);
        Entry entry3 = new Entry(from3);
        entry3.parentRotation = Rotation.COUNTERCLOCKWISE;
        entries.add(entry3);
      }
    }

    if (type > 5 && current.distance > 1) {
      String from4 = nextEntry(rotateClockwise(rotateClockwise(type)), prevEntry);
      Entry entry4 = new Entry(from4);
      entry4.parentRotation = Rotation.DOUBLE_CLOCKWISE;
      entries.add(entry4);
    }

    return entries;
  }

  List<Node> neighbors(Cell[][] cells, Node current) {
    List<Node> neighbors = new ArrayList<>();
    List<Entry> entries = nextEntries(current);
    for (Entry entry : entries) {
      String from = entry.from;
      if (from.equals(LEFT) && current.x < width - 1) {
        Node leftNeighbor = new Node(current.x + 1, current.y);
        update(cells, neighbors, current, leftNeighbor, entry);
      } else if (from.equals(RIGHT) && current.x > 0) {
        Node rightNeighbor = new Node(current.x - 1, current.y);
        update(cells, neighbors, current, rightNeighbor, entry);
      } else if (from.equals(TOP) && current.y < height - 1) {
        Node topNeighbor = new Node(current.x, current.y + 1);
        update(cells, neighbors, current, topNeighbor, entry);
      }
    }
    return neighbors;
  }

  void update(Cell[][] cells, List<Node> neighbors, Node current, Node neighbor, Entry entry) {
    Cell neighborCell = cells[neighbor.y][neighbor.x];
    if (type(neighbor) != 0 && !neighborCell.visited.contains(entry.from)) {
      neighbor.entry = entry;
      neighborCell.visited.add(entry.from);
      neighbor.distance = current.distance + 1;
      neighbor.parent = current;
      neighbors.add(neighbor);
    }
  }

  int rotateClockwise(int type) {
    switch (type) {
      case 2:
        return 3;
      case 3:
        return 2;
      case 4:
        return 5;
      case 5:
        return 4;
      case 6:
        return 7;
      case 7:
        return 8;
      case 8:
        return 9;
      case 9:
        return 6;
      case 10:
        return 11;
      case 11:
        return 12;
      case 12:
        return 13;
      case 13:
        return 10;
      default:
        return 0;
    }
  }

  int rotateCounterclockwise(int type) {
    switch (type) {
      case 6:
        return 9;
      case 7:
        return 6;
      case 8:
        return 7;
      case 9:
        return 8;
      case 10:
        return 13;
      case 11:
        return 10;
      case 12:
        return 11;
      case 13:
        return 12;
      default:
        return 0;
    }
  }

  int type(State state) {
    return rooms[state.y][state.x];
  }

  class State {
    int x, y;
    Entry entry = new Entry();

    State(int x, int y) {
      this.x = x;
      this.y = y;
    }

    State(int x, int y, String from) {
      this(x, y);
      this.entry.from = from;
    }

    State() {}

    boolean equalPosition(State other) {
      return x == other.x && y == other.y;
    }
  }

  class Node extends State {
    Node parent = null;
    double distance = Integer.MAX_VALUE;

    Node(int x, int y) {
      super(x, y);
    }

    Node(int x, int y, String from) {
      super(x, y, from);
    }
  }

  class Rock extends State {
    boolean ignore = false; // ignore during computation

    Rock(int x, int y, String from) {
      super(x, y, from);
    }

    Rock(Rock other) {
      x = other.x;
      y = other.y;
      entry.from = other.entry.from;
      entry.rotation = other.entry.rotation;
      ignore = other.ignore;
    }
  }

  class Cell {
    int x, y;
    Set<String> visited = new TreeSet<>(); // to check for repeat states

    Cell(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }

  class Entry {
    String from = "";
    Rotation rotation = Rotation.NONE;
    Rotation parentRotation = Rotation.NONE;

    Entry() {}

    Entry(String from) {
      this.from = from;
    }

    @Override
    public String toString() {
      return "Entry{" +
          "from='" + from + '\'' +
          ", rotation=" + rotation +
          '}';
    }
  }

  enum Rotation {
    NONE,
    CLOCKWISE,
    COUNTERCLOCKWISE,
    DOUBLE_CLOCKWISE
  }

  class Command {
    boolean clockWise = false;
    int xRotation = DEFAULT_COORDINATE;
    int yRotation = DEFAULT_COORDINATE;
    Node rotationNode = null;

    @Override
    public String toString() {
      if (rotationNode != null) {
        StringBuilder output = new StringBuilder();
        output.append(xRotation);
        output.append(" ");
        output.append(yRotation);
        output.append(" ");
        if (clockWise) {
          output.append(RIGHT);
          rooms[yRotation][xRotation] = rotateClockwise(rooms[yRotation][xRotation]);
        } else {
          output.append(LEFT);
          rooms[yRotation][xRotation] = rotateCounterclockwise(rooms[yRotation][xRotation]);
        }
        return output.toString();
      }
      return "WAIT";
    }
  }
}
