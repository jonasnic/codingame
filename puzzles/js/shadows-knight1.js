let inputs = readline().split(' ');
const WIDTH = parseInt(inputs[0]); // width of the building.
const HEIGHT = parseInt(inputs[1]); // height of the building.
let nbTurns = parseInt(readline()); // maximum number of turns before game over.
inputs = readline().split(' ');
let x = parseInt(inputs[0]);
let y = parseInt(inputs[1]);

let minX = 0;
let maxX = WIDTH - 1;
let minY = 0;
let maxY = HEIGHT - 1;

// game loop
while (true) {
  let bombDir = readline();

  if (bombDir === "U") {
    maxY = y - 1;
    minX = maxX = x;
  } else if (bombDir === "UR") {
    minX = x + 1;
    maxY = y - 1;
  } else if (bombDir === "R") {
    minX = x + 1;
    minY = maxY = y;
  } else if (bombDir === "DR") {
    minX = x + 1;
    minY = y + 1;
  } else if (bombDir === "D") {
    minY = y + 1;
    minX = maxX = x;
  } else if (bombDir === "DL") {
    maxX = x - 1;
    minY = y + 1;
  } else if (bombDir === "L") {
    maxX = x - 1;
    minY = maxY = y;
  } else { // UL
    maxX = x - 1;
    maxY = y - 1;
  }

  x = Math.floor((minX + maxX) / 2)
  y = Math.floor((minY + maxY) / 2)
  print(x + " " + y) // the location of the next window Batman should jump to.
}
