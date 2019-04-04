scores = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1,
    'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

best_word = ""
high_score = 0
words = []
nb_words = int(input())
for i in range(nb_words):
    words.append(input())
letters = input()

for word in words:
    letters2 = list(letters)
    is_valid = True
    current_score = 0

    # calculate the total score for one word
    for char in word:
        try:
            index = letters2.index(char)
        except ValueError:
            is_valid = False
            break
        else:
            del letters2[index]
            current_score += scores[char]

    if is_valid and current_score > high_score:
        high_score = current_score
        best_word = word

print(best_word)
