import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val nbPlaces = input.nextInt()
  val nbRides = input.nextInt()
  val nbGroups = input.nextInt()
  val groups = ArrayList<Long>()
  for (i in 0 until nbGroups) {
    val nbPeople = input.nextInt()
    groups.add(nbPeople.toLong())
  }

  // Calculate earnings starting from each group (1 ride)
  // Save the result (dynamic programming)
  val results = ArrayList<Pair<Long, Int>>()
  for (i in 0 until nbGroups) {
    var index = i
    var nbPeople = groups[index]
    var nbPeopleRiding = 0L
    while (nbPeopleRiding + nbPeople <= nbPlaces) {
      nbPeopleRiding += nbPeople
      if (index < nbGroups - 1) {
        index++
      } else {
        index = 0
      }
      // all groups are riding already?
      if (index == i) {
        break
      }
      nbPeople = groups[index]
    }
    results.add(Pair(nbPeopleRiding, index))
  }

  // Calculate the total earnings starting from the first group (all rides)
  var totalMoney = 0L
  var currentGroup = 0
  for (i in 0 until nbRides) {
    val (money, nextGroup) = results[currentGroup]
    totalMoney += money
    currentGroup = nextGroup
  }

  println(totalMoney)
}
