if __name__ == "__main__":
    original = int(input())
    line_number = int(input())
    conway_sequence = [original]

    for line in range(1, line_number):
        temp_sequence = []
        count = 0
        previous = conway_sequence[0]
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
