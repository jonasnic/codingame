import math

min_x = 2 ** 30
max_x = 0
cable_size = 0  # main horizontal cable length
coordinates = []

nb_buildings = int(input())
for i in range(nb_buildings):
    x, y = [int(j) for j in input().split()]
    coordinates.append(y)
    if (x < min_x):
        min_x = x
    if (x > max_x):
        max_x = x

coordinates.sort()
cable_size = max_x - min_x

# To minimize the total vertical length of the cables,
# the y value of the main cable must be the median of all the y values.
median = coordinates[nb_buildings // 2]
for i in range(nb_buildings):
    cable_size += math.fabs(median - coordinates[i])

print(int(cable_size))
