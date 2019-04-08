import sys
import itertools

n = int(input())
subsequences = []
for i in range(n):
    subsequences.append(input())

permutations = list(itertools.permutations(subsequences))

min_length = 60
for permutation in permutations:
    sequence = permutation[0]
    for i in range(1, len(permutation)):
        j = 0
        while (j < len(sequence)):
            # if subseq is contained within the sequence
            if (sequence.find(permutation[i]) != -1):
                break
            # if there is a partial match
            end_index = len(sequence) - j
            if (sequence[j:] == permutation[i][:end_index]):
                sequence += permutation[i][end_index:]
            j += 1
        # if there is no match
        if (j == len(sequence)):
            sequence += permutation[i]
    min_length = min(min_length, len(sequence))

print(min_length)
