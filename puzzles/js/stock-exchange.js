let maxValue = -1
let maxLoss = 0

const NB_VALUES = parseInt(readline());
let inputs = readline().split(' ');
for (let i = 0; i < NB_VALUES; i++) {
    let value = parseInt(inputs[i]);
    if (value > maxValue) {
      maxValue = value;
    } else {
      let loss = maxValue - value;
      maxLoss = Math.max(maxLoss, loss);
    }
}

print(-maxLoss);
