class Link {
  constructor(node1, node2) {
    this.node1 = node1;
    this.node2 = node2;
  }

  // sever the link between two nodes
  slice() {
    print(this.node1 + ' ' + this.node2);
  }

  equals(link) {
    return ((this.node1 === link.node1) && (this.node2 === link.node2)) ||
           (((this.node1 === link.node2) && (this.node2 === link.node1)));
  }
}

let graph = [];
let gateways = [];

const inputs = readline().split(' ');
const nbNodes = parseInt(inputs[0]); // the total number of nodes in the level, including the gateways
const nbLinks = parseInt(inputs[1]); // the number of links
const nbExits = parseInt(inputs[2]); // the number of exit gateways

for (let i = 0; i < nbLinks; ++i) {
  let inputs = readline().split(' ');
  let N1 = parseInt(inputs[0]); // N1 and N2 defines a link between these nodes
  let N2 = parseInt(inputs[1]);
  graph.push(new Link(N1, N2));
  printErr(graph[i].node1 + ' ' + graph[i].node2);
}

for (let i = 0; i < nbExits; ++i) {
  let gateway = parseInt(readline()); // the index of a gateway node
  gateways.push(gateway);
  printErr(gateways[i]);
}

// game loop
while (true) {
  let agentNode = parseInt(readline()); // node index on which the Skynet agent is positioned this turn
  blockAgent(agentNode);
}

function blockAgent(agentNode) {
  let link = new Link();
  for (let i = 0; i < gateways.length; ++i) {
    let gateway = gateways[i];
    link.node1 = agentNode;
    link.node2 = gateway;
    // Check if there is a link between the agent and the gateway nodes
    for (let j = 0; j < graph.length; ++j) {
      let current = graph[j];
      if (link.equals(current)) {
        link.slice();
        graph.splice(j, 1);
        return;
      } // if
    } // for
  } // for
  blockFirstLink();
} // blockAgent()

function blockFirstLink() {
  graph[0].slice();
  graph.splice(0, 1);
}
