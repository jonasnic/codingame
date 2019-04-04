import java.util.*;

class Solution {
  public static void main(String args[]) {
    final char DEAD = '0';
    final char LIVE = '1';

    // Read the game input
    Scanner in = new Scanner(System.in);
    int width = in.nextInt();
    int height = in.nextInt();
    StringBuilder[] board = new StringBuilder[height];
    StringBuilder[] newBoard = new StringBuilder[height];
    for (int i = 0; i < height; ++i) {
      String line = in.next();
      StringBuilder builder = new StringBuilder(line);
      StringBuilder newBuilder = new StringBuilder(line);
      board[i] = builder;
      newBoard[i] = newBuilder;
    } // for

    // Play the next turn
    for (int y = 0; y < height; ++y) {
      StringBuilder line = board[y];
      for (int x = 0; x < width; ++x) {
        char cell = line.charAt(x);
        char newCell = cell;

        // Get neighbors
        List<Character> neighbors = new ArrayList<>();

        if (0 < x) {
          neighbors.add(line.charAt(x - 1));
          if (0 < y)
            neighbors.add(board[y - 1].charAt(x - 1));
          if (y < (height - 1))
            neighbors.add(board[y + 1].charAt(x - 1));
        } // if

        if (x < (width - 1)) {
          neighbors.add(line.charAt(x + 1));
          if (0 < y)
            neighbors.add(board[y - 1].charAt(x + 1));
          if (y < (height - 1))
            neighbors.add(board[y + 1].charAt(x + 1));
        } // if

        if (0 < y)
          neighbors.add(board[y - 1].charAt(x));
        if (y < (height - 1))
          neighbors.add(board[y + 1].charAt(x));

        long nbLiveNeighbors = neighbors.stream().filter(n -> n == LIVE).count();

        if (cell == LIVE) {
          if (nbLiveNeighbors >= 2 && nbLiveNeighbors <= 3)
            newCell = LIVE;
          else
            newCell = DEAD;
        } else {
          if (nbLiveNeighbors == 3)
            newCell = LIVE;
        } // else

        newBoard[y].setCharAt(x, newCell);
      } // for
    } // for

    // Print the new board
    for (int y = 0; y < height; ++y) {
      StringBuilder line = newBoard[y];
      System.out.println(line);
    } // for
  } // main()
} // Solution