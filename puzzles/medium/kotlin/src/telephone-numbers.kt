import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  var nbNodes = 0
  val root = Node(-1)
  val zero = '0'.toInt()

  for (i in 0 until n) {
    val telephone = input.next()
    var current = root
    for (char in telephone) {
      val digit = char.toInt() - zero
      var index = current.index(digit)
      if (index == -1) {
        current.addChild(digit)
        nbNodes += 1
      }
      index = current.index(digit)
      current = current.children[index]
    }
  }

  // The number of elements (referencing a number) stored in the structure.
  println(nbNodes)
}

class Node(val digit: Int) {
  val children = ArrayList<Node>()

  fun index(d: Int): Int {
    return children.indexOfFirst { it.digit == d }
  }

  fun addChild(d: Int) {
    val child = Node(d)
    children.add(child)
  }
}
