import java.util.*

fun main(args : Array<String>) {
  val XP_GAIN = 300
  val input = Scanner(System.`in`)
  var level = input.nextInt()
  var xpNeeded = input.nextInt()
  val nbPuzzles = input.nextInt()

  var xpGained = (nbPuzzles * XP_GAIN) + (xpForLevelUp(level) - xpNeeded)

  while (xpGained >= xpForLevelUp(level)) {
    xpGained -= xpForLevelUp(level)
    level++
  }

  xpNeeded = xpForLevelUp(level) - xpGained

  println(level)
  println(xpNeeded)
}

fun xpForLevelUp(level: Int): Int {
  return (Math.floor(level * Math.sqrt(level.toDouble()) * 10)).toInt()
}
