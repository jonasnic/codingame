import java.util.*

fun main(args: Array<String>) {
  val `in` = Scanner(System.`in`)
  // Candidates info
  val nbCandidates = `in`.nextInt()
  `in`.nextLine()
  val candidates = HashMap<Int, String>()
  for (i in 1..nbCandidates) {
    val name = `in`.nextLine()
    candidates.put(i, name)
  }

  // Voters info
  val nbVoters = `in`.nextInt()
  `in`.nextLine()
  val voters = ArrayList<ArrayList<Int>>()
  for (i in 0 until nbVoters) {
    val votes = `in`.nextLine()
    val array = votes.split(" ")
    val list = ArrayList<Int>()
    for (s in array) {
      list.add(Integer.parseInt(s))
    }
    voters.add(list)
  }

  // Eliminate candidates
  while (candidates.size > 1) {
    // Count the number of votes
    val voteCount = ArrayList<Int>()
    for (i in 0..nbCandidates) {
      voteCount.add(0)
    }
    for (voter in voters) {
      val vote = voter.get(0)
      voteCount.set(vote, voteCount.get(vote) + 1)
    }

    // Determine the loser
    var minVotes = Integer.MAX_VALUE
    var loser = 0
    for (candidate in candidates.keys) {
      val nbVotes = voteCount.get(candidate)
      if (nbVotes < minVotes) {
        minVotes = nbVotes
        loser = candidate.toInt()
      }
    }

    // Announce the loser of this round
    System.out.println(candidates.get(loser))
    candidates.remove(loser)
    // Remove all the votes for the loser
    for (voter in voters) {
      val loserCopy = loser
      voter.removeIf({ vote -> vote.equals(loserCopy) })
    }
    // Reset the voteCount
    for (i in 0..nbCandidates) {
      voteCount.set(i, 0)
    }
  }

  val winnnerKey = candidates.keys.firstOrNull()
  System.out.println("winner:" + candidates.get(winnnerKey))
}
