import java.util.*;

class Player {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    // game loop
    while (true) {
      int max = -1;
      int indexMax = 0;
      for (int i = 0; i < 8; i++) {
        int height = in.nextInt(); // represents the height of one mountain.
        if (height > max) {
          max = height;  
          indexMax = i;      
        }
      }
      System.out.println(indexMax); // The index of the mountain to fire on.
    }
  }
}
