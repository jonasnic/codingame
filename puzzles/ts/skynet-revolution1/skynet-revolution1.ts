function sever(n1: number, n2: number): void {
  console.log(`${n1} ${n2}`);
}

function deleteLink(graph: object, n1: number, n2: number): void {
  graph[n1].splice(graph[n1].indexOf(n2), 1);
  graph[n2].splice(graph[n2].indexOf(n1), 1);
}

function blockDirectLink(graph: object, gateways: number[], agentNodeId: string): boolean {
  // check if the current agent node is linked to a gateway
  let gateway: number = -1;
  for (let neighbor of graph[agentNodeId]) {
    if (gateways.indexOf(neighbor) != -1) {
      sever(Number(agentNodeId), neighbor);
      gateway = neighbor;
    }
  }
  if (gateway !== -1) {
    deleteLink(graph, Number(agentNodeId), gateway);
  }
  return gateway !== -1;
}

function blockRandomLink(graph: object, gateways: number[]): void {
  for (let id in graph) {
    if (graph[id].length > 0) {
      sever(Number(id), graph[id][0]);
      deleteLink(graph, Number(id), graph[id][0]);
      return;
    }
  }
}

const inputs: string = readline().split(' ');
const nbNodes = Number(inputs[0]); // the total number of nodes in the level, including the gateways
const nbLinks = Number(inputs[1]); // the number of links
const nbGateways = Number(inputs[2]); // the number of exit gateways

let graph: object = {}; // map node id => node links set
let gateways: number[] = [];

for (let i: number = 0; i < nbLinks; i++) {
  const inputs: string = readline().split(' ');
  const n1 = Number(inputs[0]); // n1 and n2 defines a link between these nodes
  const n2 = Number(inputs[1]);
  
  if (! (n1 in graph)) {
    graph[n1] = []
  }
  graph[n1].push(n2);

  if (! (n2 in graph)) {
    graph[n2] = []
  }
  graph[n2].push(n1);
}

for (let i: number = 0; i < nbGateways; i++) {
  const gateway = Number(readline()); // the id of a gateway node
  gateways.push(gateway);
}

// game loop
while (true) {
  const agentNodeId:string = readline();
  if (!blockDirectLink(graph, gateways, agentNodeId)) {
    blockRandomLink(graph, gateways);
  };
}
