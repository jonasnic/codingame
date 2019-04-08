@nb_values = gets.to_i
inputs = gets.split(" ")
max_value = -1
max_loss = 0

for i in 0..(@nb_values-1)
  value = inputs[i].to_i
  if value > max_value
    max_value = value
  else
    loss = max_value - value
    if loss > max_loss
      max_loss = loss
    end
  end
end

puts "#{-max_loss}"