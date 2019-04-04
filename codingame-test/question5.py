# https://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/

from collections import Counter

book = input()

counter = Counter()
for word in book.split():
    counter[word] += 1

print(counter.most_common(3))

