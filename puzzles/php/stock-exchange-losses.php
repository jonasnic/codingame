<?php
$maxValue = -1;
$maxLoss = 0;

fscanf(STDIN, "%d", $nbValues);
$inputs = fgets(STDIN);
$inputs = explode(" ", $inputs);

for ($i = 0; $i < $nbValues; $i++) {
  $value = intval($inputs[$i]);
  if ($value > $maxValue) {
    $maxValue = $value;
  } else {
    $loss = $maxValue - $value;
    $maxLoss = max($maxLoss, $loss);
  }
}

echo(-$maxLoss . "\n");
?>
