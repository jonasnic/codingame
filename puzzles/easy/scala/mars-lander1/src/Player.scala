object Player extends App {
  val surfacen = readInt // the number of points used to draw the surface of Mars.
  for(i <- 0 until surfacen) {
    val Array(landx, landy) = for(i <- readLine split " ") yield i.toInt
  }

  // game loop
  while(true) {
    // vspeed: the vertical speed (in m/s), can be negative.
    // rotate: the rotation angle in degrees (-90 to 90).
    // power: the thrust power (0 to 4).
    var Array(x, y, hspeed, vspeed, fuel, rotate, power) = for(i <- readLine split " ") yield i.toInt

    rotate = 0
    if (vspeed <= -40) {
      power = 4
    } else {
      power = 0
    }

    // Write an action using println
    // To debug: Console.err.println("Debug messages...")

    // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    println(rotate + " " + power)
  }
}
