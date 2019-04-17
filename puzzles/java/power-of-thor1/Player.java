import java.util.*;

class Player {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int lightX = in.nextInt(); // the X position of the light of power
    int lightY = in.nextInt(); // the Y position of the light of power
    int thorX = in.nextInt(); // Thor's starting X position
    int thorY = in.nextInt(); // Thor's starting Y position

    // game loop
    while (true) {
      String direction = "";

      if (thorY > lightY) {
        direction += "N";
        thorY -= 1;
      } else if (thorY < lightY) {
        direction += "S";
        thorY += 1;
      }

      if (thorX > lightX) {
        direction += "W";
        thorX -= 1;
      } else if (thorX < lightX) {
        direction += "E";
        thorX += 1;
      }

      // A single line providing the move to be made: N NE E SE S SW W or NW
      System.out.println(direction);
    }
  }
}
