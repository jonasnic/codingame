import java.util.Scanner
import java.util.ArrayDeque

const val WALL = '#'
const val BEGINNING = 'T'
const val CONTROL_ROOM = 'C'
const val UNKNOWN = '?'

fun main(args : Array<String>) {
  val maze = Maze()
  maze.readInitInput()
  maze.gameLoop()
}

class Maze {
  val input = Scanner(System.`in`)

  val map = ArrayList<ArrayList<Char>>()
  var nbRows = 0
  var nbColumns = 0

  val kirk = Position()
  val start = Position()
  val controlRoom = Position()

  var explore = true
  var controlRoomReached = false

  fun readInitInput() {
    nbRows = input.nextInt() // number of rows.
    nbColumns = input.nextInt() // number of columns.
    for (y in 0 until nbRows) {
      val row = ArrayList<Char>()
      for (x in 0 until nbColumns) {
        row.add(UNKNOWN)
      }
      map.add(row)
    }
    val rounds = input.nextInt()
  }

  fun gameLoop() {
    while (true) {
      kirk.y = input.nextInt()
      kirk.x = input.nextInt()
      updateMap()

      if (kirk == controlRoom) {
        controlRoomReached = true
      }

      if (explore) {
        // explore the maze until every reachable position is discovered
        val result = search(kirk, UNKNOWN)
        if (result == null) {
          explore = false
          goSomewhere()
        } else {
          printNextMove(result)
        }
      } else {
        goSomewhere()
      }
    }
  }

  fun updateMap() {
    for (y in 0 until nbRows) {
      val row = input.next() // row of the ASCII maze
      for ((x, char) in row.withIndex()) {
        map[y][x] = char
        if (char == BEGINNING) {
          start.x = x
          start.y = y
        } else if (char == CONTROL_ROOM) {
          controlRoom.x = x
          controlRoom.y = y
        }
      }
    }
  }

  fun goSomewhere() {
    if (!controlRoomReached) {
      // go to the control room
      val result = search(kirk, CONTROL_ROOM)
      printNextMove(result)
    } else {
      // go back to the start
      val result = search(kirk, BEGINNING)
      printNextMove(result)
    }
  }

  fun printNextMove(result: Result?) {
    var next = Position()

    if (result != null) {
      while (result.current != kirk) {
        next = result.current
        result.current = result.parents.getOrDefault(result.current, Position())
      }
    }

    // Kirk's next move
    when {
      kirk.x < next.x -> println("RIGHT")
      kirk.x > next.x -> println("LEFT")
      kirk.y < next.y -> println("DOWN")
      else -> println("UP")
    }
  }

  // BFS from start until goal is reached
  fun search(start: Position, goal: Char): Result? {
    val visited = HashSet<Position>()
    val queue = ArrayDeque<Position>()
    val parents = HashMap<Position, Position>()
    visited.add(start)
    queue.add(start)

    while (queue.isNotEmpty()) {
      val current = queue.remove()
      if (map[current.y][current.x] == goal) {
        return Result(parents, current)
      }
      for (neighbor in neighbors(current)) {
        if (!visited.contains(neighbor)) {
          visited.add(neighbor)
          queue.add(neighbor)
          parents[neighbor] = current
        }
      }
    }

    return null
  }

  fun neighbors(position: Position): MutableList<Position> {
    val positions = ArrayList<Position>()
    add(positions, Position(position.x + 1, position.y))
    add(positions, Position(position.x, position.y + 1))
    add(positions, Position(position.x - 1, position.y))
    add(positions, Position(position.x, position.y - 1))
    return positions
  }

  fun add(positions: MutableList<Position>, position: Position) {
    if (isValid(position)) {
      positions.add(position)
    }
  }

  fun isValid(position: Position): Boolean {
    val char = map[position.y][position.x]
    return char != WALL && position.x >= 0 && position.x < nbColumns && position.y >= 0 && position.y < nbRows
  }
}

class Result(val parents : HashMap<Position, Position>, var current: Position)

data class Position(var x: Int = 0, var y: Int = 0)
