const n: number = Number(readline());
const values: number[] = readline().split(' ').map(Number);
let maxLoss: number = 0;
let maxValue: number = values[0];
for (let i: number = 1; i < n; i++) {
  const value: number = values[i];
  if (value > maxValue) {
    maxValue = value;
  } else {
    const loss: number = maxValue - value;
    maxLoss = -Math.max(loss, maxLoss);
  }
}

console.log(maxLoss);
