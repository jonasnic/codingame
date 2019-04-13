const nbParticipants: number = Number(readline());
let giftPrice = Number(readline());
let budgets: number[] = [];
let totalBudget = 0;

for (let i: number = 0; i < nbParticipants; i++) {
  const budget = Number(readline());
  budgets.push(budget);
  totalBudget += budget;
}

if (totalBudget < giftPrice) {
  console.log("IMPOSSIBLE");
} else {
  budgets.sort((b1, b2) => (b1 - b2));
  for (let i: number = 0; i < nbParticipants; i++) {
    let contribution = budgets[i];
    const maxContribution = Math.floor(giftPrice / (nbParticipants - i));
    if (contribution > maxContribution) {
      contribution = maxContribution;
    }
    console.log(contribution);
    giftPrice -= contribution;
  }
}
