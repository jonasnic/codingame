<?php
fscanf(STDIN, "%d",$nbPeople);
fscanf(STDIN, "%d",$price);

$budgets = [];
$totalBudget = 0;

for ($i = 0; $i < $nbPeople; $i++) {
  fscanf(STDIN, "%d", $budget);
  $budgets[] = $budget;
  $totalBudget += $budget;
}

if ($totalBudget < $price) {
  echo("IMPOSSIBLE\n");
} else {
  sort($budgets);
  for ($i = 0; $i < $nbPeople; $i++) {
    if ($budgets[$i] >= $price/($nbPeople - $i)) {
      $contribution =  intval($price/($nbPeople - $i));
    } else {
      $contribution = $budgets[$i];
    }
    echo($contribution . "\n");
    $price -= $contribution;
  }
}
?>