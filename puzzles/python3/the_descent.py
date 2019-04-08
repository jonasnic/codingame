# game loop
while True:
    max_index = 0
    max_height = 0
    for i in range(8):
        height = int(input())  # represents the height of one mountain.
        if height >= max_height:
            max_height = height
            max_index = i  
    print(max_index)
