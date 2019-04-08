const EMPTY = ".";
const NODE = "0";
let grid = [];
const WIDTH = parseInt(readline()); // the number of cells on the X axis
const HEIGHT = parseInt(readline()); // the number of cells on the Y axis
for (let y = 0; y < HEIGHT; y++) {
  grid.push(readline());
}

for (let y = 0; y < HEIGHT; y++) {
  for (let x = 0; x < WIDTH; x++) {
    if (grid[y].charAt(x) === NODE) {
      // node
      let output = x + " " + y + " ";

      // right neighbor
      let neighbor = EMPTY;
      for (let neighborX = x + 1; neighborX < WIDTH; neighborX++) {
        neighbor = grid[y].charAt(neighborX);
        if (neighbor === NODE) {
          output += neighborX + " " + y + " ";
          break;
        }
      }

      if (neighbor === EMPTY)
        output += "-1 -1 ";

      // bottom neighbor
      neighbor = EMPTY
      for (let neighborY = y + 1; neighborY < HEIGHT; neighborY++) {
        neighbor = grid[neighborY].charAt(x);
        if (neighbor === NODE) {
          output += x + " " + neighborY + " ";
          break;
        }
      }

      if (neighbor === EMPTY)
        output += "-1 -1 ";

      print(output);
    }
  }
}
