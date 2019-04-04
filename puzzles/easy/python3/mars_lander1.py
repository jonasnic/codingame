import sys

surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # v_speed: the vertical speed (in m/s), can be negative.
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, f, rot, power = [int(i) for i in input().split()]

    output = ""
    if v_speed <= -40:
        output = str(min(4, power + 1))
    else:
        output = str(max(0, power - 1))

    # 2 integers: rotate power.
    print("0 " + output)
