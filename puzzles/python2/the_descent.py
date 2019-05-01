# game loop
while True:
    index_mountain_to_fire = 0
    max_mountain_height = -1
    for i in range(8):
        mountain_height = int(raw_input())
        if mountain_height > max_mountain_height:
            max_mountain_height = mountain_height
            index_mountain_to_fire = i

    print(index_mountain_to_fire)
