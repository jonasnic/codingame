from typing import List


if __name__ == "__main__":
    original: int = int(input())
    line_number: int = int(input())
    conway_sequence: List[int] = [original]

    for line in range(1, line_number):
        temp_sequence: List[int] = []
        count: int = 0
        previous: int = conway_sequence[0]
        for number in conway_sequence:
            if number == previous:
                count += 1
            else:
                temp_sequence.append(count)
                temp_sequence.append(previous)
                previous = number
                count = 1

        temp_sequence.append(count)
        temp_sequence.append(previous)
        conway_sequence = temp_sequence  # update

    print(" ".join(map(str, conway_sequence)))
