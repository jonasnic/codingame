if __name__ == "__main__":
    elevators = {}

    _, _, _, exit_floor, exit_pos, _, _, n5 = map(int, input().split())
    for _ in range(n5):
        elevator_floor, elevator_pos = map(int, input().split())
        elevators[elevator_floor] = elevator_pos
    # For the last floor, we use the exit instead of an elevator.
    elevators[exit_floor] = exit_pos

    # game loop
    while True:
        clone_floor, clone_pos, direction = input().split()
        clone_floor = int(clone_floor)
        clone_pos = int(clone_pos)
        if clone_floor == -1:
            print("WAIT")
        elif direction == "LEFT" and clone_pos < elevators[clone_floor]:
            print("BLOCK")
        elif direction == "RIGHT" and clone_pos > elevators[clone_floor]:
            print("BLOCK")
        else:
            print("WAIT")
