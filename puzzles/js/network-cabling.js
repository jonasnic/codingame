let minX = Math.pow(2, 30);
let maxX = 0;
let cableSize = 0; // main horizontal cable length
let coordinates = [];

const NB_BUILDINGS = parseInt(readline());
for (let i = 0; i < NB_BUILDINGS; i++) {
  let inputs = readline().split(' ');
  let x = parseInt(inputs[0]);
  let y = parseInt(inputs[1]);
  coordinates.push(y);
  if (x < minX) {
    minX = x
  }
  if (x > maxX) {
    maxX = x
  }
}

coordinates.sort(function(a, b) {
  return a - b;
});
cableSize = maxX - minX;

// To minimize the total vertical length of the cables,
// the y value of the main cable must be the median of all the y values.
index = Math.floor(NB_BUILDINGS / 2);
median = coordinates[index];
for (let i = 0; i < NB_BUILDINGS; i++) {
  cableSize += Math.abs(median - coordinates[i]);
}

print(cableSize);
