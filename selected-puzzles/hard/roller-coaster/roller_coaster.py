nb_places, nb_rides, nb_groups = [int(i) for i in input().split()]
groups = []
for i in range(nb_groups):
    nb_people = int(input())
    groups.append(nb_people)

# Calculate earnings starting from each group (1 ride)
# Save the result (dynamic programming)
results = []
for i in range(nb_groups):
    index = i
    nb_people = groups[index]
    nb_people_riding = 0
    while nb_people_riding + nb_people <= nb_places:
        nb_people_riding += nb_people
        if index < nb_groups - 1:
            index += 1
        else:
            index = 0
        # all groups are riding already?
        if index == i:
            break
        nb_people = groups[index]
    results.append((nb_people_riding, index))

# Calculate the total earnings starting from the first group (all rides)
total_money = 0
current_group = 0
for i in range(nb_rides):
    money, next_group = results[current_group]
    total_money += money
    current_group = next_group

print(total_money)
