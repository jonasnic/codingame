object Player extends App {
  var Array(lightX, lightY, thorX, thorY) = for(i <- readLine split " ") yield i.toInt

  // game loop
  while (true) {
    // Write an action using println
    // To debug: Console.err.println("Debug messages...")
    var direction : String = ""

    if (thorY > lightY) {
      direction += "N"
      thorY -= 1
    } else if (thorY < lightY) {
      direction += "S"
      thorY += 1
    }

    if (thorX > lightX) {
      direction += "W"
      thorX -= 1
    } else if (thorX < lightX) {
      direction += "E"
      thorX += 1
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    println(direction)
  }
}
