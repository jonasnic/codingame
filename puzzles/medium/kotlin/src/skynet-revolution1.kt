import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val nbNodes = input.nextInt() // the total number of nodes in the level, including the gateways
  val nbLinks = input.nextInt() // the number of links
  val nbGateways = input.nextInt() // the number of exit gateways

  val links = ArrayList<Link>(nbLinks)
  val gateways = ArrayList<Int>(nbGateways)

  for (i in 0 until nbLinks) {
    val n1 = input.nextInt() // n1 and n2 defines a link between these nodes
    val n2 = input.nextInt()
    val link = Link(n1, n2)
    links.add(link)
  }

  for (i in 0 until nbGateways) {
    val gateway = input.nextInt() // the index of a gateway node
    gateways.add(gateway)
  }

  // game loop
  while (true) {
    val agentNode = input.nextInt() // The index of the node on which the Skynet agent is positioned this turn
    block(agentNode, links, gateways)
  }
}

data class Link(val n1: Int, val n2: Int)

fun sever(link: Link) {
  println("${link.n1} ${link.n2}")
}

fun blockFirstLink(links: ArrayList<Link>) {
  sever(links[0])
  links.removeAt(0)
}

fun block(agentNode: Int, links: ArrayList<Link>, gateways: ArrayList<Int>) {
  for (gateway in gateways) {
    // Check for a direct link between the agent and a gateway
    for ((i, link) in links.withIndex()) {
      val agentLink = Link(agentNode, gateway)
      val agentLink2 = Link(gateway, agentNode)
      if (link == agentLink || link == agentLink2) {
        sever(link)
        links.removeAt(i)
        return
      }
    }
  }
  blockFirstLink(links)
}
