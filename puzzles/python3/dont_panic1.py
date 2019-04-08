elevators = {}

n1, w, n2, exit_floor, exit_pos, n3, n4, n5 = [int(i) for i in input().split()]
for i in range(n5):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos
# For the last floor, we use the exit instead of an elevator.
elevators[exit_floor] = exit_pos

# game loop
while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    if (clone_floor == -1):
        print("WAIT")
    elif direction == "LEFT" and clone_pos < elevators[clone_floor]:
        print("BLOCK")
    elif direction == "RIGHT" and clone_pos > elevators[clone_floor]:
        print("BLOCK")
    else:
        print("WAIT")
