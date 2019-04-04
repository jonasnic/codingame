<?php
function printNextRoom($type, $x, $y, $entrance) {
  switch ($type) {
    case 2:
    case 6: $entrance == "LEFT" ? ++$x : --$x; break;
    case 4: $entrance == "TOP" ? --$x : ++$y; break;
    case 5: $entrance == "TOP" ? ++$x : ++$y; break;
    case 10: --$x; break;
    case 11:
      ++$x;
      break;
    default: ++$y;
  }

  // coordinates of the room in which you believe Indy will be on the next turn.
  echo("$x $y\n");
}

$rooms = [[]];

fscanf(STDIN, "%d %d", $nbColumns, $nbRows);
for ($i = 0; $i < $nbRows; ++$i) {
  // represents a line in the grid. Each integer represents one room of a given type.
  $line = stream_get_line(STDIN, 201, "\n");
  $rooms[$i] = explode(" ", $line);
}

// the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
fscanf(STDIN, "%d", $exit);

// game loop
while (true) {
  fscanf(STDIN, "%d %d %s", $x, $y, $entrance);
  printNextRoom($rooms[$y][$x], $x, $y, $entrance);
}
?>
