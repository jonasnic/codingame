import java.util.*;

class Solution {
  public static void main(String args[]) {
    // Read the game data
    Scanner in = new Scanner(System.in);
    int nbOpponents = in.nextInt();
    in.nextLine();
    String[] players = new String[nbOpponents];
    for (int i = 0; i < nbOpponents; ++i) {
      String timeStamp = in.nextLine();
      players[i] = timeStamp;
    } // for

    // Determine the time at which the game starts
    if (nbOpponents == 0) {
      System.out.println("NO GAME");
    } else {
      Time timer = new Time("5:00");
      Time start = new Time("0:00");
      for (String timeStamp : players) {
        timer.setTime(timeStamp);
        if (timer.seconds < start.seconds)
          startGame(start);
        if (start.nbOpponents == 6) {
          System.out.println(timeStamp);
          System.exit(0);
        } // if
        start.updateTime(timer);
      } // for
      startGame(start);
    } // else
  } // main()

  static void startGame(Time start) {
    System.out.println(start);
    System.exit(0);
  } // startGame()
} // Solution

class Time {
  final static String REGEX = ":";
  int seconds; // total time remaining in seconds
  int nbOpponents = 0; // number of players in the room

  Time(String timeStamp) {
    setTime(timeStamp);
  } // Time()

  void setTime(String timeStamp) {
    String[] array = timeStamp.split(REGEX);
    int minutes = Integer.parseInt(array[0]);
    int sec = Integer.parseInt(array[1]);
    seconds = minutes * 60 + sec;
  }

  void updateTime(Time timer) {
    ++nbOpponents;
    // t - 256 / ( 2^(p - 1) )
    seconds = timer.seconds - (int) (256 / (Math.pow(2, nbOpponents - 1)));
    if (seconds < 0)
      seconds = 0;
  } // updateCountdown()

  @Override
  public String toString() {
    int minutes = seconds / 60;
    int sec = seconds % 60;
    return String.format("%d%s%02d", minutes, REGEX, sec);
  } // toString()
} // Time