import java.util.*

fun main(args : Array<String>) {
  var maxValue = -1
  var maxLoss = 0

  val input = Scanner(System.`in`)
  val n = input.nextInt()
  for (i in 0 until n) {
    val value = input.nextInt()
    if (value > maxValue) {
      maxValue = value
    } else {
      val loss = maxValue - value
      if (loss > maxLoss) {
        maxLoss = loss
      }
    }
  }

  println(-maxLoss)
}
