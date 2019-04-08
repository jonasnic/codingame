import java.util.Scanner

fun main(args : Array<String>) {
  val persons = ArrayList<Person>()
  var maxDepth = 0

  val input = Scanner(System.`in`)
  val n = input.nextInt() // the number of relationships of influence
  for (i in 0 until n) {
    val x = input.nextInt() // a relationship of influence between two people
    val y = input.nextInt()
    var giant = Person(x)
    var dwarf = Person(y)

    if (persons.contains(giant)) {
      giant = persons[persons.indexOf(giant)]
    } else {
      persons.add(giant)
    }

    if (persons.contains(dwarf)) {
      dwarf = persons[persons.indexOf(dwarf)]
    } else {
      persons.add(dwarf)
    }

    giant.add(dwarf)
    giant.updateDepths()
  }

  persons.asSequence().filter { it.depth > maxDepth }.forEach { maxDepth = it.depth }

  // The number of people involved in the longest succession of influences
  println(maxDepth)
}

class Person(val number: Int) {
  var depth = 1
  val dwarfs = HashSet<Person>()

  fun add(dwarf: Person) {
    dwarfs.add(dwarf)
  }

  fun updateDepths() {
    for (dwarf in dwarfs) {
      if (depth >= dwarf.depth) {
        dwarf.depth = depth + 1
        dwarf.updateDepths()
      }
    }
  }

  override fun equals(other: Any?): Boolean {
    if (this === other) return true
    if (javaClass != other?.javaClass) return false

    other as Person

    if (number != other.number) return false

    return true
  }

  override fun hashCode(): Int {
    return number
  }
}
