max_value = -1
max_loss = 0

nb_values = int(input())
for i in input().split():
    value = int(i)
    if (value > max_value):
        max_value = value
    else:
        loss = max_value - value
        max_loss = max(max_loss, loss)

print(-max_loss)
