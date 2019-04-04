using System;

class Solution
{
  static void Main(string[] args)
  {
    int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
    int minT = 5526;
    string[] inputs = Console.ReadLine().Split(' ');
    for (int i = 0; i < n; i++)
    {
      int t = int.Parse(inputs[i]); // a temperature expressed as an integer ranging from -273 to 5526
      if (Math.Abs(t) < Math.Abs(minT) || Math.Abs(t) == Math.Abs(minT) && t > minT)
      {
        minT = t;
      }
    }

    // Write an action using Console.WriteLine()
    // To debug: Console.Error.WriteLine("Debug messages...");
    if (n == 0)
    {
      Console.WriteLine(0);
    }
    else
    {
      Console.WriteLine(minT);
    }
  }
}

