import math


def to_radians(distance):
    """ Convert distance in degrees to radians. """
    return float(distance.replace(",", ".", 1)) * math.pi / 180


min_dist = float("inf")
name = ""
lon = to_radians(input())
lat = to_radians(input())
n = int(input())

# Determine the name of the defib closest to the user’s position.
for i in range(n):
    defib = input().split(";")
    defib_lon = to_radians(defib[4])
    defib_lat = to_radians(defib[5])
    x = (defib_lon - lon) * math.cos((lat + defib_lat) / 2)
    y = defib_lat - lat
    distance = math.hypot(x, y) * 6371
    if distance < min_dist:
        min_dist = distance
        name = defib[1]

print(name)
