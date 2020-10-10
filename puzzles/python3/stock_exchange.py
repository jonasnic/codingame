if __name__ == "__main__":
    max_value: int = 0
    max_loss: int = 0

    n: int = int(input())
    for v in input().split():
        value: int = int(v)
        if value > max_value:
            max_value = value
        elif value < max_value:
            loss: int = max_value - value
            if loss > max_loss:
                max_loss = loss

    print(-max_loss)
