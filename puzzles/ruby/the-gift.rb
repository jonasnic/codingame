@creatures = gets.to_i # number of participants
@price = gets.to_i
budgets = Array.new()
total_budget = 0

@creatures.times do
  budget = gets.to_i
  budgets.push(budget)
  total_budget += budget
end

if total_budget < @price
  puts "IMPOSSIBLE"
else
  budgets = budgets.sort
  for i in 0..(@creatures - 1)
    contribution = (budgets[i] >= @price/(@creatures - i)) ? @price/(@creatures - i) : budgets[i]
    puts "#{contribution}"
    @price -= contribution
  end
end