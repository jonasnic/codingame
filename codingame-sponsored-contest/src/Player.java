import java.util.*;

class Player {
  // region region 1
  ArrayList<Player> path = new ArrayList<>();
  int x, y;

  Player() {}

  Player(int x, int y) {
    this.x = x;
    this.y = y;
  } // Player()


  @Override
  public boolean equals(Object obj) {
    if (obj instanceof Player) {
      Player player = (Player) obj;
      return this.x == player.x && this.y == player.y;
    } // if
    return false;
  } // equals()
  // endregion

  public static void main(String args[]) {
    Game game = new Game();
    game.readInitInput();

    // game loop
    while (true) {
      game.readGameInput();
      if (game.playerPositionIsValid()) {
        //System.err.println("findUnkown()");
        Player move = game.findUnkown();
        //System.err.println("move = " + move.x + " " + move.y);
        if (game.isSafeMove(move)) {
          //System.err.println("playMove()");
          game.playMove(move);
        } else {
          //System.err.println("playAlternativeMove()");
          game.playAlternativeMove();
        } // else
      } else {
        game.playStay();
      } // else
    } // while
  } // main()
} // Player

class Game {
  // region Declarations
  enum Direction { Y_DOWN, X_UP, Y_UP, X_DOWN, STAY }

  static final int NEGATIVE = -1;
  static final char UNKNOWN = '?';
  static final char OPEN = '_';
  static final char WALL = '#';
  HashMap<Direction, Character> hash = new HashMap<>();
  Scanner in = new Scanner(System.in);
  char[][] grid;
  int xSize, ySize, nbPlayers;
  Player player = new Player();
  ArrayList<Player> enemies = new ArrayList<>();
  int turn = 2;
  // endregion

  public Game() {
    hash.put(Direction.Y_DOWN, 'C');
    hash.put(Direction.X_UP, 'A');
    hash.put(Direction.Y_UP, 'D');
    hash.put(Direction.X_DOWN, 'E');
    hash.put(Direction.STAY, 'B');
  } // Game()

  void readInitInput() {
    xSize = in.nextInt();
    ySize = in.nextInt();
    nbPlayers = in.nextInt();
    System.err.println("Initialization input");
    System.err.println(xSize + " " + ySize + " " + nbPlayers);
    initGame();
  } // readInitInput()

  void readGameInput() {
    String c = in.next();
    String a = in.next();
    String d = in.next();
    String e = in.next();
    //System.err.println("game turn " + turn);

    for (int i = 0; i < nbPlayers; ++i) {
      int x = in.nextInt();
      int y = in.nextInt();
      if (i + 1 != nbPlayers) {
        Player enemy = new Player(x - 1, y - 1);
        if (posIsValid(enemy)) {
          enemies.set(i, enemy);
          grid[enemy.x][enemy.y] = OPEN;
          //System.err.println("enemy " + i + " @ " + enemies.get(i).x + " " + enemies.get(i).y);
        } // if
      } else {
        player.x = x - 1;
        player.y = y - 1;
        System.err.println("player " + " @ " + player.x + " " + player.y);
      } // else
    } // for

    if (playerPositionIsValid()) {
      grid[player.x][player.y] = OPEN;
      if (player.y - 1 >= 0) grid[player.x][player.y - 1] = c.charAt(0);
      if (player.x + 1 <= xSize - 1) grid[player.x + 1][player.y] = a.charAt(0);
      if (player.y + 1 <= ySize - 1) grid[player.x][player.y + 1] = d.charAt(0);
      if (player.x - 1 >= 0) grid[player.x - 1][player.y] = e.charAt(0);
    } // if

    printGrid(); // Debug
    ++turn;
  } // readGameInput()

  boolean playerPositionIsValid() {
    return (player.x >= 0) && (player.x < xSize) && (player.y >= 0) && (player.y < ySize);
  } // playerPositionIsValid()

  boolean posIsValid(Player pos) {
    return (pos.x >= 0) && (pos.x < xSize) && (pos.y >= 0) && (pos.y < ySize);
  } // enemyPositionIsValid()

  void printGrid() {
    String format = "1";
/*    System.err.print("  ");
    for (int j = 0; j < ySize; ++j) {
      System.err.printf("%" + format + "d", j % 10);
    } // for
    System.err.println("");*/

    for (int i = 0; i < xSize; ++i) {
      //System.err.printf("%" + format + "d", i % 10);
      for (int j = 0; j < ySize; ++j) {
        int index = enemyIndex(i, j);
        if (index == NEGATIVE) {
          if (player.equals(new Player(i, j))) {
            System.err.printf("%" + format + "c", 'p');
          } else {
            System.err.printf("%" + format + "c", grid[i][j]);
          } // else
        } else {
          System.err.printf("%" + format + "d", index);
        } // else
      } // for
      System.err.println();
    } // for
  } // printGrid()
  
  void initGame() {
    grid = new char[xSize][ySize];
    for (int i = 0; i < xSize; ++i) {
      for (int j = 0; j < ySize; ++j) {
        grid[i][j] = UNKNOWN;
      } // for
    } // for

    for (int i = 0; i < nbPlayers - 1; ++i) {
      enemies.add(new Player());
    } // for
  } // initGame()

  int enemyIndex(int x, int y) {
    return enemies.indexOf(new Player(x, y));
  } // enemyIndex()

  /**
   * @param x horizontal coordinate
   * @param y vertical coordinate
   * @return <code>true</code> if an enemy is located at this position
   */
  boolean enemAtPos(int x, int y) {
    return enemyIndex(x, y) != NEGATIVE;
  }

  boolean yDownIsPossible(int x, int y) {
    return (y - 1 >= 0) && (grid[x][y - 1] != WALL) && !enemAtPos(x, y - 1) &&
        !enemAtPos(x, y - 2) && !enemAtPos(x - 1, y - 1) && !enemAtPos(x + 1, y - 1);
  }

  boolean xUpIsPossible(int x, int y) {
    return (x + 1 <= xSize - 1) && (grid[x + 1][y] != WALL) && !enemAtPos(x + 1, y) &&
        !enemAtPos(x + 2, y) && !enemAtPos(x + 1, y - 1) && !enemAtPos(x + 1, y + 1);
  }

  boolean yUpIsPossible(int x, int y) {
    return (y + 1 <= ySize - 1) && (grid[x][y + 1] != WALL) && !enemAtPos(x, y + 1) &&
        !enemAtPos(x ,y + 2) && !enemAtPos(x - 1, y + 1) && !enemAtPos(x + 1, y + 1);
  }

  boolean xDownIsPossible(int x, int y) {
    return (x - 1 >= 0) && (grid[x - 1][y] != WALL) && !enemAtPos(x - 1, y) &&
        !enemAtPos(x - 2, y) && !enemAtPos(x - 1, y - 1) && !enemAtPos(x - 1, y + 1);
  }

  boolean isSafeMove(Player move) {
    int x = move.x;
    int y = move.y;
    return !((y - 1 >= 0) && enemAtPos(x, y - 1)) &&
           !((x + 1 <= xSize - 1) && enemAtPos(x + 1, y)) &&
           !((y + 1 <= ySize - 1) && enemAtPos(x, y + 1)) &&
           !((x - 1 >= 0) && enemAtPos(x - 1, y));
  } // safeMove()

  void playMove(Player move) {
    int x = move.x;
    int y = move.y;
    if (y == player.y - 1) {
      System.out.println(hash.get(Direction.Y_DOWN));
    } else if (x == player.x + 1) {
      System.out.println(hash.get(Direction.X_UP));
    } else if (y == player.y + 1) {
      System.out.println(hash.get(Direction.Y_UP));
    } else if (x == player.x - 1) {
      System.out.println(hash.get(Direction.X_DOWN));
    } else {
      System.out.println(hash.get(Direction.STAY));
    } // else
  } // playMove()

  LinkedList<Player> getPossibleMoves(int x, int y) {
    LinkedList<Player> moves = new LinkedList<>();

    if (yDownIsPossible(x, y))
      moves.add(new Player(x, y - 1));

    if (xUpIsPossible(x, y))
      moves.add(new Player(x + 1, y));

    if (yUpIsPossible(x, y))
      moves.add(new Player(x, y + 1));

    if (xDownIsPossible(x, y))
      moves.add(new Player(x - 1, y));

    return moves;
  } // getPossibleMoves()

  // Find the closest unknown point using BFS
  Player findUnkown() {
    LinkedList<Player> visited = new LinkedList<>();
    LinkedList<Player> queue = new LinkedList<>();

    player.path.clear();
    queue.addLast(player);

    while (!queue.isEmpty()) {
      Player pos = queue.removeFirst();
      if (!visited.contains(pos)) {
        //System.err.println("new pos = " + pos.x + " " + pos.y);
        visited.add(pos);
        if (grid[pos.x][pos.y] == UNKNOWN) {
          //System.err.println("unknown found - path below");
          for (Player p : pos.path) {
            //System.err.print("(" + p.x + "," + p.y + ") ");
          } // for
          //System.err.println("");
          return pos.path.isEmpty() ? null : pos.path.get(1);
        } else {
          LinkedList<Player> moves = getPossibleMoves(pos.x, pos.y);
          for (Player move : moves) {
            //System.err.println("possible move = " + move.x + " " + move.y);
            move.path.addAll(pos.path);
            move.path.add(pos);
            queue.addLast(move);
          } // for
        } // else
      } // if
    } // while

    return player;
  } // findUnkown()

  void playAlternativeMove() {
    System.out.println(findAlternativeMove());
  } // playAlternativeMove()

  char findAlternativeMove() {
    int x = player.x;
    int y = player.y;

    // Avoid walls and enemies
    if (yDownIsPossible(x, y))
      return hash.get(Direction.Y_DOWN);

    if (xUpIsPossible(x, y))
      return hash.get(Direction.X_UP);

    if (yUpIsPossible(x, y))
      return hash.get(Direction.Y_UP);

    if (xDownIsPossible(x, y))
      return hash.get(Direction.X_DOWN);

    // The player is surrounded and tries to hit a nearby enemy.
    if (enemAtPos(x, y - 1)) {
      return hash.get(Direction.Y_DOWN);
    } else if (enemAtPos(x + 1, y)) {
      return hash.get(Direction.X_UP);
    } else if (enemAtPos(x, y + 1)) {
      return hash.get(Direction.Y_UP);
    } else if (enemAtPos(x - 1, y)) {
      return hash.get(Direction.X_DOWN);
    } // else if

    // no enemy right next to the player
    return hash.get(Direction.STAY);
  } // findAlternativeMove()

  void playStay() {
    System.out.println(hash.get(Direction.STAY));
  } // playAlternativeMove()
} // Game