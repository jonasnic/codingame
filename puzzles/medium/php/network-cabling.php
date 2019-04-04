<?php
$minX = PHP_INT_MAX;
$maxX = 0;
$cableSize = 0;
$coordinates = [];

fscanf(STDIN, "%d", $nbBuildings);
for ($i = 0; $i < $nbBuildings; ++$i) {
  fscanf(STDIN, "%d %d", $x, $y);
  $coordinates[$i] = $y;
  if ($x < $minX)
    $minX = $x;
  if ($x > $maxX)
    $maxX = $x;
}

sort($coordinates);
$cableSize = $maxX - $minX; // main horizontal cable length
// To minimize the total vertical length of the cables,
// the y value of the main cable must be the median of all the y values.
$median = $coordinates[$nbBuildings / 2];
for ($i = 0; $i < count($coordinates); ++$i)
  $cableSize += abs($median - $coordinates[$i]);

echo("$cableSize\n");
?>
