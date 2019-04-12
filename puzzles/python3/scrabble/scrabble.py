POINTS = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1,
    'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}


def is_valid_word(word, letters):
    for c in word: 
        if c not in letters:
            return False
        else:
            letters.remove(c)
    return True


def score(word):
    total = 0
    for c in word:
        total += POINTS[c]
    return total


# read game input
words = []
nb_words = int(input())
for i in range(nb_words):
    words.append(input())
letters = input()

# compute solution
best_score = 0
best_word = ""
for word in words:
    lettersCopy = list(letters)
    if is_valid_word(word, lettersCopy):
        current_score = score(word)
        if current_score > best_score:
            best_score = current_score
            best_word = word

print(best_word)
