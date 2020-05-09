def print_next_room(room_type, x, y, entrance):
    if room_type in [2, 6]:
        if entrance == "LEFT":
            x += 1
        else:
            x -= 1
    elif room_type == 4:
        if entrance == "TOP":
            x -= 1
        else:
            y += 1
    elif room_type == 5:
        if entrance == "TOP":
            x += 1
        else:
            y += 1
    elif room_type == 10:
        x -= 1
    elif room_type == 11:
        x += 1
    else:
        y += 1
    print("{} {}".format(x, y))


if __name__ == "__main__":
    rooms = []
    nbColumns, nbRows = [int(i) for i in input().split()]
    for i in range(nbRows):
        line = [int(i) for i in input().split()]
        rooms.append(line)
    ex = int(input())

    # game loop
    while True:
        x, y, entrance = input().split()
        x = int(x)
        y = int(y)
        print_next_room(rooms[y][x], x, y, entrance)
