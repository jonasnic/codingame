from typing import List


if __name__ == "__main__":
    strengths: List[int] = []
    min_diff: int = 10000000
    n: int = int(input())
    for _ in range(n):
        strengths.append(int(input()))

    strengths.sort()

    for i in range(n - 1):
        diff: int = strengths[i + 1] - strengths[i]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)
