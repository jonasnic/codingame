// Detective Pikaptcha EP1

import java.util.*;

class Player {
  public static void main(String args[]) {
    final char WALL = '#';
    final char PASSAGE = '0';
    
    Scanner in = new Scanner(System.in);
    int width = in.nextInt();
    int height = in.nextInt();
    String[] grid = new String[height];
    for (int y = 0; y < height; y++) {
      String line = in.next();
      grid[y] = line;
    }
    
    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        if (grid[y].charAt(x) == WALL) {
          System.out.print(WALL);
        } else if (grid[y].charAt(x) == PASSAGE) {
          int count = 0;
          // left
          if (x - 1 >= 0 && grid[y].charAt(x - 1) == PASSAGE) {
            count++;
          }
          // right
          if (x + 1 < grid[y].length() && grid[y].charAt(x + 1) == PASSAGE) {
            count++;
          }
          // up
          if (y - 1 >= 0 && grid[y - 1].charAt(x) == PASSAGE) {
            count++;
          }
          // down
          if (y + 1 < grid.length && grid[y + 1].charAt(x) == PASSAGE) {
            count++;
          }
          System.out.print(count);
        }
      }
      System.out.println();
    }
  }
}
