const ORIGINAL = parseInt(readline());
const LINE_NUMBER = parseInt(readline());

let conwaySequence = [ORIGINAL];

for (let i = 1; i < LINE_NUMBER; i++) {
  let tempSequence = [];
  let count = 0;
  let previous = conwaySequence[0];
  for (let j = 0; j < conwaySequence.length; j++) {
    let number = conwaySequence[j];
    if (number === previous) {
      count += 1;
    } else {
      tempSequence.push(count);
      tempSequence.push(previous);
      previous = number;
      count = 1;
    }
  }

  tempSequence.push(count);
  tempSequence.push(previous);
  conwaySequence = tempSequence;
}

print(conwaySequence.join(" "));
