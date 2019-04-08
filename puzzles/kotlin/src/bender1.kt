import java.util.Scanner

const val UNBREAKABLE_WALL = '#'
const val BREAKABLE_WALL = 'X'
const val START = '@'
const val FINISH = '$'
const val SOUTH = 'S'
const val EAST = 'E'
const val NORTH = 'N'
const val WEST = 'W'
const val BEER = 'B'
const val INVERTER = 'I'
const val TELEPORTER = 'T'
const val EMPTY = ' '

fun main(args : Array<String>) {
  val city = City()
  val bender = Bender()
  readGameInput(city, bender)
  city.printGrid()
  gameLoop(city, bender)
}

fun readGameInput(city: City, bender: Bender) {
  val input = Scanner(System.`in`)
  city.height = input.nextInt()
  city.width = input.nextInt()
  if (input.hasNextLine()) {
    input.nextLine()
  }
  for (y in 0 until city.height) {
    val row = input.nextLine()
    val cellList = ArrayList<Cell>()
    for (x in 0 until row.length) {
      val symbol = row[x]
      val cell = Cell(symbol)
      cellList.add(cell)
      if (symbol == START) {
        bender.point.x = x
        bender.point.y = y
      } else if (symbol == TELEPORTER) {
        if (!city.teleporter) {
          city.teleporter1 = Point(x, y)
          city.teleporter = true
        } else {
          city.teleporter2 = Point(x, y)
        }
      }
    }
    city.grid.add(cellList)
  }
}

fun resetGridState(city: City) {
  for (y in 0 until city.height) {
    for (x in 0 until city.width) {
      city.grid[y][x].reset()
    }
  }
}

fun currentSymbol(city: City, bender: Bender): Char {
  return city.grid[bender.point.y][bender.point.x].symbol
}

fun isValidMove(city: City, bender: Bender, direction: Direction): Boolean {
  return when (direction) {
    Direction.SOUTH -> isValidPosition(city, bender, bender.point.x, bender.point.y + 1)
    Direction.EAST -> isValidPosition(city, bender, bender.point.x + 1, bender.point.y)
    Direction.NORTH -> isValidPosition(city, bender, bender.point.x, bender.point.y - 1)
    else -> isValidPosition(city, bender, bender.point.x - 1, bender.point.y) // WEST
  }
}

fun isValidPosition(city: City, bender: Bender, x: Int, y: Int): Boolean {
  return x >= 0 && x < city.width &&
      y >= 0 && y < city.height &&
      city.grid[y][x].symbol != UNBREAKABLE_WALL && (bender.breakMode || city.grid[y][x].symbol != BREAKABLE_WALL)
}

fun updateBenderState(city: City, bender: Bender)  {
  val symbol = currentSymbol(city, bender)
  if (symbol == START || symbol == SOUTH) {
    bender.direction = Direction.SOUTH
  } else if (symbol == EAST) {
    bender.direction = Direction.EAST
  } else if (symbol == NORTH) {
    bender.direction = Direction.NORTH
  } else if (symbol == WEST) {
    bender.direction = Direction.WEST
  } else if (symbol == BEER) {
    bender.breakMode = !bender.breakMode
  } else if (symbol == INVERTER) {
    bender.reverse = !bender.reverse
    bender.priorites.reverse()
  } else if (symbol == TELEPORTER) {
    if (bender.point == city.teleporter1) {
      bender.point = city.teleporter2.copy()
    } else {
      bender.point = city.teleporter1.copy()
    }
  }
}

fun addMove(city: City, bender: Bender) {
  updateBenderState(city, bender)

  if (isValidMove(city, bender, bender.direction)) {
    bender.addMove()
  } else {
    for (direction in bender.priorites) {
      if (isValidMove(city, bender, direction)) {
        bender.direction = direction
        bender.addMove()
        break
      }
    }
  }

  val cell = city.grid[bender.point.y][bender.point.x]

  if (cell.visited && Triple(cell.reverse, cell.breakMode, cell.direction) == Triple(bender.reverse, bender.breakMode, bender.direction)) {
    city.loop = true
  } else {
    cell.visited = true
    cell.reverse = bender.reverse
    cell.breakMode = bender.breakMode
    cell.direction = bender.direction
  }
}

fun gameLoop(city: City, bender: Bender) {
  while (currentSymbol(city, bender) != FINISH) {
    addMove(city, bender)

    if (city.loop) {
      break
    }

    if (bender.breakMode && currentSymbol(city, bender) == BREAKABLE_WALL) {
      city.grid[bender.point.y][bender.point.x] = Cell(EMPTY)
      resetGridState(city)
    }
  }

  if (city.loop) {
    println("LOOP")
  } else {
    for (move in bender.moves) {
      println(move)
    }
  }
}

data class Point(var x: Int, var y: Int)

enum class Direction {
  SOUTH,
  EAST,
  NORTH,
  WEST
}

class Cell(val symbol: Char) {
  var visited = false
  var direction = Direction.SOUTH
  var reverse = false
  var breakMode = false

  fun reset() {
    visited = false
    direction = Direction.SOUTH
    reverse = false
    breakMode = false
  }

  override fun toString(): String {
    return symbol.toString()
  }
}

class Bender {
  val priorites = arrayListOf(Direction.SOUTH, Direction.EAST, Direction.NORTH, Direction.WEST)
  var direction = Direction.SOUTH
  var reverse = false
  var breakMode = false
  var point = Point(0, 0)
  val moves = ArrayList<Direction>()

  fun addMove() {
    when (direction) {
      Direction.SOUTH -> point.y++
      Direction.EAST -> point.x++
      Direction.NORTH -> point.y--
      else -> point.x-- // WEST
    }
    moves.add(direction)
  }
}

class City {
  val grid = ArrayList<ArrayList<Cell>>()
  var teleporter = false
  var teleporter1 = Point(0, 0)
  var teleporter2 = Point(0, 0)
  var height = 0
  var width = 0
  var loop = false

  fun printGrid() {
    System.err.println("$height $width")

    for (y in 0 until height) {
      for (x in 0 until width) {
        System.err.print(grid[y][x].toString())
      }
      System.err.println()
    }
  }
}
