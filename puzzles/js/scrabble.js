function getScore(letter) {
  let map = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
  };

  return map[letter];
}

let bestWord = "";
let highScore = 0;

// read input
let dictionary = [];
let nbWords = parseInt(readline());
for (let i = 0; i < nbWords; ++i) {
  let word = readline();
  dictionary.push(word);
}
let letters = readline();

// Determine the best word
for (let i = 0; i < nbWords; ++i) {
  let letters2 = letters; // available letters
  let entry = dictionary[i];
  let isValid = true;
  let currentScore = 0;

  // calculate the total score for one word
  for (let j = 0; j < entry.length; ++j) {
    let character = entry[j];
    let includes = letters2.includes(character);
    if (includes) {
      letters2 = letters2.replace(character, ""); // remove the letter
      currentScore += getScore(character);
    } else {
      isValid = false; // unavailable letter
    } // else
  } // for

  if (isValid && (currentScore > highScore)) {
    highScore = currentScore;
    bestWord = entry;
  } // if
} // for

print(bestWord);
