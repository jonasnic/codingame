if __name__ == "__main__":
    width: int = int(input())
    height: int = int(input())
    text: str = input().upper()
    for _ in range(height):
        row: str = input()
        output: str = ""
        for character in text:
            position: int = ord(character) - ord('A')
            if position < 0 or position > 25:
                position = 26
            start: int = position * width
            end: int = start + width
            output += row[start:end]
        print(output)
