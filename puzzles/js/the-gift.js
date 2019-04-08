let budgets = [];
let totalBudget = 0;

const NB_PARTICIPANTS = parseInt(readline());
let giftPrice = parseInt(readline());
for (let i = 0; i < NB_PARTICIPANTS; i++) {
  let budget = parseInt(readline());
  budgets.push(budget);
  totalBudget += budget;
}

if (totalBudget < giftPrice) {
  print("IMPOSSIBLE");
} else {
  budgets.sort(function(x, y) {
    return x - y;
  });
  for (let i = 0; i < NB_PARTICIPANTS; i++) {
    let contribution = budgets[i];
    let maxContribution = giftPrice / (NB_PARTICIPANTS - i);
    if (contribution >= maxContribution)
      contribution = Math.floor(maxContribution);
    print(contribution);
    giftPrice -= contribution;
  }
}
