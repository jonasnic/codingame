import sys

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    index_mountain_to_fire = 0
    max_mountain_height = -1
    for i in range(8):
        mountain_height = int(input())
        if mountain_height > max_mountain_height:
            max_mountain_height = mountain_height
            index_mountain_to_fire = i

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(index_mountain_to_fire)
