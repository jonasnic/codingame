import java.util.Scanner
import java.util.PriorityQueue

const val EXIT = -1
const val START = 0

fun main(args : Array<String>) {
  val building = Building()
  building.readRooms()
  building.calcAllMaxDepths()
  println(building.maxMoney())
}

class Room(val number: Int, val money: Int, door1: String, door2: String) : Comparable<Room> {
  val doors = ArrayList<Int>()
  var depth = -1

  init {
    readDoor(door1)
    readDoor(door2)
  }

  fun readDoor(door: String) {
    if (door == "E") {
      doors.add(EXIT)
    } else {
      doors.add(door.toInt())
    }
  }

  // reversed operator for max heap
  override fun compareTo(other: Room): Int {
    return other.depth - depth
  }
}

// graph representation of the building
class Building {
  val rooms = ArrayList<Room>()

  fun readRooms() {
    val input = Scanner(System.`in`)
    val n = input.nextInt()
    if (input.hasNextLine()) {
      input.nextLine()
    }
    for (i in 0 until n) {
      val (number, money, door1, door2) = input.nextLine().split(" ")
      val room = Room(number.toInt(), money.toInt(), door1, door2)
      rooms.add(room)
    }
  }

  // Calculate the max depth of each room reachable from the start with DFS
  fun calcAllMaxDepths() {
    calcMaxDepth(rooms[START], -1)
  }

  fun calcMaxDepth(room: Room, parentDepth: Int) {
    room.depth = parentDepth + 1
    for (door in room.doors) {
      if (door != EXIT) {
        val neighbor = rooms[door]
        if (neighbor.depth <= room.depth) {
          calcMaxDepth(neighbor, room.depth)
        }
      }
    }
  }

  // Find the path with the max total money (inspired by Dijkstra's algorithm)
  fun maxMoney(): Int {
    val unvisited = PriorityQueue<Room>()
    val money = ArrayList<Int>()
    for (number in 0 until rooms.size) {
      money.add(0)
      unvisited.add(rooms[number])
    }

    // loop through each depth level of the graph in descending order
    while (!unvisited.isEmpty()) {
      // find max depth
      val maxRoom = unvisited.poll()
      val maxNumber = maxRoom.number
      // find the best path for each subproblem
      val nextNumber = nextDoor(maxNumber, money)
      money[maxNumber] = maxRoom.money
      if (nextNumber != EXIT) {
        money[maxNumber] += money[nextNumber]
      }
      if (maxNumber == START) {
        break
      }
    }

    return money[START]
  }

  fun nextDoor(maxNumber: Int, money: ArrayList<Int>): Int {
    val door1 = rooms[maxNumber].doors[0]
    val door2 = rooms[maxNumber].doors[1]
    return when {
      door1 == EXIT -> door2
      door2 == EXIT -> door1
      money[door1] > money[door2] -> door1
      else -> door2
    }
  }
}
