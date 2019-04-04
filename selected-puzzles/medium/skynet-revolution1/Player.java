import java.util.*;

class Player {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    Graph graph = readGraph(in);
    graph.setTargetExit();

    // game loop
    while (true) {
      int agentIndex = in.nextInt();
      if (!blockNearbyAgent(graph, agentIndex)) {
        if (!blockTargetGateway(graph)) {
          blockGateway(graph, agentIndex);
        }
      }
    }
  }

  static Graph readGraph(Scanner in) {
    int nbNodes = in.nextInt(); // total number of nodes in the level, including the gateways
    int nbLinks = in.nextInt(); // number of links
    int nbGateways = in.nextInt(); // number of exit gateways
    Graph graph = new Graph();
    graph.nodes = new ArrayList<>(nbNodes);

    for (int i = 0; i < nbNodes; ++i) {
      graph.nodes.add(new Node(i));
    }

    for (int i = 0; i < nbLinks; ++i) {
      int n1 = in.nextInt(); // n1 and n2 defines a link between these nodes
      int n2 = in.nextInt();
      Node node1 = graph.nodes.get(n1);
      Node node2 = graph.nodes.get(n2);
      node1.links.add(node2);
      node2.links.add(node1);
    }

    for (int i = 0; i < nbGateways; ++i) {
      int index = in.nextInt(); // index of a gateway node
      Node exit = graph.nodes.get(index);
      exit.isGateway = true;
      graph.gateways.add(exit);
    }

    graph.targetGateways.addAll(graph.gateways);
    return graph;
  }

  /** If the agent is linked to an exit, sever the link and return <code>true</code>.*/
  static boolean blockNearbyAgent(Graph graph, int agentIndex) {
    Node agentNode = new Node(agentIndex);
    for (Node exitNode : graph.gateways) {
      if (exitNode.links.contains(agentNode)) {
        slice(agentIndex, exitNode.n);
        exitNode.links.remove(agentNode);
        graph.nodes.get(agentIndex).links.remove(exitNode);
        return true;
      }
    }
    return false;
  }

  /** Sever a link to block the biggest star */
  static boolean blockTargetGateway(Graph graph) {
    if (graph.targetLinks.isEmpty()) {
      return false;
    } // if
    Link target = graph.targetLinks.removeFirst();
    slice(target.outerNode.n, target.innerNode.n);
    target.outerNode.links.remove(target.innerNode);
    target.innerNode.links.remove(target.outerNode);
    graph.setTargetExit();
    return true;
  }

  /** Slice the last link on the shortest path between the virus and an exit using BFS. */
  static void blockGateway(Graph graph, int agentIndex) {
    Node agentNode = graph.nodes.get(agentIndex); // start
    Node current, node;
    LinkedList<Node> queue = new LinkedList<>();
    graph.resetGraph();
    agentNode.isMarked = true;
    queue.addLast(agentNode);

    while (!queue.isEmpty()) {
      current = queue.removeFirst();
      for (Node neighbor : current.links) {
        if (!neighbor.isMarked) {
          neighbor.isMarked = true;
          neighbor.parent = current;
          // check if a gateway was found
          if (neighbor.isGateway) {
            node = neighbor.parent;
            slice(neighbor.n, node.n);
            neighbor.links.remove(node);
            node.links.remove(neighbor);
            return;
          } else {
            queue.addLast(neighbor);
          }
        }
      }
    }
  }

  /** n1, n2: the indices of the nodes you wish to sever the link between */
  static void slice(int n1, int n2) {
    System.out.println(String.valueOf(n1) + " " + String.valueOf(n2));
  }
}

class Graph {
  ArrayList<Node> nodes;
  List<Node> gateways = new LinkedList<>();
  List<Node> targetGateways = new LinkedList<>();
  LinkedList<Link> targetLinks = new LinkedList<>();
  Node targetExit; // gateway with the biggest star

  /** Determine the targetExit and targetLinks. */
  void setTargetExit() {
    if (targetLinks.isEmpty()) {
      int max = 0;
      for (Node exitNode : targetGateways) {
        int size = exitNode.links.size();
        if (size > max) {
          max = size;
          targetExit = exitNode;
        }
      }
      targetGateways.remove(targetExit);

      targetExit.links.stream().filter(node -> node.links.size() >= 4).forEach(outerNode -> {
        Optional<Node> innerOption = outerNode.links.stream()
            .filter(node -> node.links.size() <= 3).findFirst();
        if (innerOption.isPresent()) {
          Node innerNode = innerOption.get();
          targetLinks.add(new Link(outerNode, innerNode));
        }
      });
    }
  }

  void resetGraph() {
    nodes.forEach(node -> {
      node.parent = null;
      node.isMarked = false;
    });
  }
}

class Link {
  Node outerNode, innerNode;

  public Link(Node outerNode, Node innerNode) {
    this.outerNode = outerNode;
    this.innerNode = innerNode;
  }
}

class Node {
  int n; // index
  LinkedList<Node> links = new LinkedList<>();
  boolean isGateway;
  Node parent;
  boolean isMarked;

  Node(int n) {
    this.n = n;
  }

  @Override
  public boolean equals(Object obj) {
    if (obj instanceof Node) {
      Node node = (Node) obj;
      return this.n == node.n;
    }
    return false;
  }
}
