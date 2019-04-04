import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val n = input.nextInt()
  var price = input.nextInt()
  val budgets = ArrayList<Int>(n)
  var totalBudget = 0

  for (i in 0 until n) {
    val budget = input.nextInt()
    budgets.add(budget)
    totalBudget += budget
  }

  if (totalBudget < price) {
    println("IMPOSSIBLE")
  } else {
    budgets.sort()
    for (i in 0 until n) {
      var contribution = budgets[i]
      val maxContribution = price / (n - i)
      if (contribution >= maxContribution) {
        contribution = maxContribution
      }
      println(contribution)
      price -= contribution
    }
  }
}
