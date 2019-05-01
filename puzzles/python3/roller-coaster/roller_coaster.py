# read game input
groups = []
nb_places, nb_rides, nb_groups = map(int, input().split())
for i in range(nb_groups):
    group_size = int(input())
    groups.append(group_size)

# cache the results starting to fill the ride from each of the groups
results = []
for i in range(nb_groups):
    group_index = i
    nb_places_left = nb_places
    while nb_places_left >= groups[group_index]:
        nb_places_left -= groups[group_index]
        group_index += 1
        if group_index == nb_groups:
            group_index = 0
        if group_index == i:
            break
    money = nb_places - nb_places_left
    results.append((money, group_index))

# calculate the total money earned during the day
total_money = 0
group_index = 0
for _ in range(nb_rides):
    money, next_group_index = results[group_index]
    total_money += money
    group_index = next_group_index

print(total_money)
