budgets = []
total_budget = 0

nb_participants = int(input())
gift_price = int(input())
for i in range(nb_participants):
    budget = int(input())
    budgets.append(budget)
    total_budget += budget

if (total_budget < gift_price):
    print("IMPOSSIBLE")
else:
    budgets.sort()
    for i in range(nb_participants):
        contribution = budgets[i]
        max_contribution = gift_price // (nb_participants - i)
        if contribution >= max_contribution:
            contribution = max_contribution
        print(contribution)
        gift_price -= contribution
