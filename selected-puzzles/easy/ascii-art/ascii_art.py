width = int(input())
height = int(input())
text = input().upper()
for i in range(height):
    row = input()
    output = ""
    for char in text:
        position = ord(char) - ord("A")
        if (position < 0 or position > 25):
            position = 26
        start = position * width
        end = start + width
        output += row[start:end]
    print(output)
