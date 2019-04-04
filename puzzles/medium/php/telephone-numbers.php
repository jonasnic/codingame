<?php
class Node {
  public $digit;
  public $children = [];

  public function __construct($digit) {
    $this->digit = $digit;
  }

  public function indexOf($digit) {
    for ($i = 0; $i < count($this->children); ++$i) {
      $child = $this->children[$i];
      if ($child->digit == $digit)
        return $i;
    }
    return -1;
  }

  public function addChild($digit) {
    $child = new Node($digit);
    $this->children[] = $child;
    return count($this->children) - 1;
  }
}

$answer = 0; // The number of elements (referencing a number) stored in the structure.
$root = new Node(-1);

fscanf(STDIN, "%d", $count);
for ($i = 0; $i < $count; ++$i) {
  fscanf(STDIN, "%s", $telephone);
  $current = $root;
  for ($j = 0; $j < strlen($telephone); ++$j) {
    $digit = $telephone[$j];
    $index = $current->indexOf($digit);
    if ($index == -1) {
      $index = $current->addChild($digit);
      ++$answer;
    }
    $current = $current->children[$index];
  }
}

echo("$answer\n");
?>
