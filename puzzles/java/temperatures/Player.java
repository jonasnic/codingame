import java.util.*;

class Solution {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(); // the number of temperatures to analyse
    int minTemperature = 5526;
    for (int i = 0; i < n; i++) {
      int temperature = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
      if (Math.abs(temperature) < Math.abs(minTemperature) || Math.abs(temperature) == Math.abs(minTemperature) && temperature > minTemperature) {
        minTemperature = temperature;
      }
    }

    if (n == 0) {
      System.out.println(0);
    } else {
      System.out.println(minTemperature);
    }
  }
}
