using System;

class Player
{
  static void Main(string[] args)
  {
    // game loop
    while (true)
    {
      int max = 0;
      int indexMax = 0;
      for (int i = 0; i < 8; i++)
      {
        int height = int.Parse(Console.ReadLine()); // represents the height of one mountain.
        if (height > max)
        {
          max = height;
          indexMax = i;
        }
      }

      Console.WriteLine(indexMax); // The index of the mountain to fire on.
    }
  }
}

