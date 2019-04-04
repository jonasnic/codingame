import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  var minX = Long.MAX_VALUE
  var maxX = 0L
  var cableSize: Long // main horizontal cable length
  val coordinates = ArrayList<Int>(n)

  for (i in 0 until n) {
    val x = input.nextInt()
    val y = input.nextInt()
    coordinates.add(y)
    if (x < minX) {
      minX = x.toLong()
    }
    if (x > maxX) {
      maxX = x.toLong()
    }
  }

  coordinates.sort()
  cableSize = maxX - minX

  // To minimize the total vertical length of the cables,
  // the y value of the main cable must be the median of all the y values.

  val median = coordinates[n / 2]
  for (i in 0 until n) {
    cableSize += Math.abs(median - coordinates[i])
  }

  println(cableSize)
}
