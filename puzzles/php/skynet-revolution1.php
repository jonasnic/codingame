<?php
class Link {
  public $n1, $n2;

  public function __construct($n1, $n2) {
    $this->n1 = $n1;
    $this->n2 = $n2;
  }

  // sever the link
  public function slice() {
    echo("$this->n1 $this->n2\n");
  }

  public function equals($link) {
    return (($this->n1 == $link->n1) && ($this->n2 == $link->n2)) ||
           (($this->n1 == $link->n2) && ($this->n2 == $link->n1));
  }
}

$graph = [];
$gateways = [];

fscanf(STDIN, "%d %d %d", $nbNodes, $nbLinks, $nbExits);
for ($i = 0; $i < $nbLinks; ++$i) {
  fscanf(STDIN, "%d %d", $n1, $n2); // n1 and n2 defines a link between these nodes
  $link = new Link($n1, $n2);
  $graph[] = $link;
}

for ($i = 0; $i < $nbExits; ++$i) {
  fscanf(STDIN, "%d", $gateway); // the index of a gateway node
  $gateways[] = $gateway;
}

// game loop
while (true) {
  fscanf(STDIN, "%d", $agentNode); // The index of the node on which the Skynet agent is positioned this turn
  block($agentNode, $graph, $gateways);
}

function block($agentNode, $graph, $gateways) {
  for ($i = 0; $i < sizeof($gateways); ++$i) {
    $link = new Link($agentNode, $gateways[$i]);
    // Check if there is a link between the agent and the gateway nodes
    for ($j = 0; $j < sizeof($graph); ++$j) {
      if ($link->equals($graph[$j])) {
        $link->slice();
        array_splice($graph, $j, 1);
        return;
      }
    }
  }
  blockFirstLink($graph, $gateways);
}

function blockFirstLink($graph, $gateways) {
  $graph[0]->slice();
  array_shift($graph);
}
?>
