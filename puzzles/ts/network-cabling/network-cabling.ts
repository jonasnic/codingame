const nbBuildings: number = Number(readline());
let cableLength = 0;
let minX = Infinity;
let maxX = -Infinity;
let yCoordinates: number[] = [];

for (let i: number = 0; i < nbBuildings; i++) {
  const inputs: string[] = readline().split(' ');
  const x = Number(inputs[0]);
  const y = Number(inputs[1]);
  maxX = Math.max(maxX, x);
  minX = Math.min(minX, x);
  yCoordinates.push(y);
}

let mainCableLength = maxX - minX;
cableLength += mainCableLength;

yCoordinates.sort((y1, y2) => y1 - y2);
let yMedian = yCoordinates[Math.ceil(yCoordinates.length / 2) - 1];
for (let y of yCoordinates) {
  let dedicatedCableLength = Math.abs(yMedian - y);
  cableLength += dedicatedCableLength;
}

console.log(cableLength);
