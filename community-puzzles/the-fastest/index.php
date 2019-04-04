<?php
$minText = "";
$minSeconds = 86518;

fscanf(STDIN, "%d", $N);
for ($i = 0; $i < $N; $i++) {
  fscanf(STDIN, "%s", $text);
  $array = explode(":", $text);
  $hours = intval($array[0]);
  $minutes = intval($array[1]);
  $seconds = intval($array[2]);
  $totalSeconds = $hours * 60 * 60 + $minutes * 60 + $seconds;
  if ($totalSeconds < $minSeconds) {
    $minSeconds = $totalSeconds;
    $minText = $text;  
  }
}

echo("$minText\n");
?>
