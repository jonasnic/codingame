if __name__ == "__main__":
    # the number of temperatures to analyse
    n: int = int(input())
    min_temperature: int = 5526

    for t in input().split():
        temperature: int = int(t)
        if any([
            abs(temperature) < abs(min_temperature),
            abs(temperature) == abs(min_temperature) and temperature > min_temperature
        ]):
            min_temperature = temperature

    print(0 if n == 0 else min_temperature)
