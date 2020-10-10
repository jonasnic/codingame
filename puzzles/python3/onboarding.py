if __name__ == "__main__":
    # game loop
    while True:
        enemy_1: str = input()  # name of enemy 1
        dist_1: int = int(input())  # distance to enemy 1
        enemy_2: str = input()  # name of enemy 2
        dist_2: int = int(input())  # distance to enemy 2

        # Display enemy1 name when enemy1 is the closest, enemy2 otherwise
        if dist_1 < dist_2:
            print(enemy_1)
        else:
            print(enemy_2)
