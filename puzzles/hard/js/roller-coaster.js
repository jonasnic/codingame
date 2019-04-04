let inputs = readline().split(' ');
const NB_PLACES = parseInt(inputs[0]);
const NB_RIDES = parseInt(inputs[1]);
const NB_GROUPS = parseInt(inputs[2]);

let groups = [];
for (let i = 0; i < NB_GROUPS; ++i) {
  let nbPeople = parseInt(readline());
  groups.push(nbPeople);
}

// Calculate earnings starting from each group (1 ride)
// Save the result (dynamic programming)
let results = [];
for (let i = 0; i < NB_GROUPS; ++i) {
  let index = i;
  let nbPeople = groups[index];
  let nbPeopleRiding = 0;
  while (nbPeopleRiding + nbPeople <= NB_PLACES) {
    nbPeopleRiding += nbPeople;
    if (index < NB_GROUPS - 1) {
      index += 1
    } else {
      index = 0
    }
    // all groups are riding already?
    if (index == i) {
      break;
    }
    nbPeople = groups[index];
  }
  results.push({
    "nbPeopleRiding": nbPeopleRiding,
    "nextGroup" : index
  });
}

// Calculate the total earnings starting from the first group (all rides)
let totalMoney = 0;
let currentGroup = 0;
for (let i = 0; i < NB_RIDES; ++i) {
  let result = results[currentGroup];
  totalMoney += result.nbPeopleRiding;
  currentGroup = result.nextGroup;
}

print(totalMoney)
