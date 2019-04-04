import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val nbColumns = input.nextInt() // number of columns.
  val nbRows = input.nextInt() // number of rows.
  if (input.hasNextLine()) {
    input.nextLine()
  }
  val rooms = Array(nbRows, {Array(nbColumns, {0})})

  for (y in 0 until nbRows) {
    val line = input.nextLine().split(" ") // represents a line in the grid
    for (x in 0 until line.size) {
      rooms[y][x] = line[x].toInt()
    }
  }
  val exit = input.nextInt() // the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

  // game loop
  while (true) {
    val x = input.nextInt()
    val y = input.nextInt()
    val entrance = input.next()
    // One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    printNextRoom(rooms[y][x], x, y, entrance)
  }
}

fun printNextRoom(roomType: Int, x1: Int, y1: Int, entrance: String) {
  var x2 = x1
  var y2 = y1

  when(roomType) {
    2, 6 -> {
      if (entrance == "LEFT") x2++ else x2--
    }
    4 -> {
      if (entrance == "TOP") x2-- else y2++
    }
    5 -> {
      if (entrance == "TOP") x2++ else y2++
    }
    10 -> x2--
    11 -> x2++
    else -> y2++
  }

  println("$x2 $y2")
}
