import sys

PLAYER1 = "PLAYER1"
PLAYER2 = "PLAYER2"
WAR = "WAR"

CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __int__(self):
        return CARD_VALUES[self.value]

    def __lt__(self, other):
        return int(self) < int(other)

    def __repr__(self):
        return "{}{}".format(self.value, self.suit)


class Game:
    def __init__(self):
        self.deck1 = self.read_game_input()
        self.deck2 = self.read_game_input()
        self.nb_rounds = 0

    def read_game_input(self):
        cards = []
        nb_cards_player = int(input())
        for i in range(nb_cards_player):
            value_suit = input()
            card = Card(value_suit[:len(value_suit) - 1], value_suit[-1])
            cards.append(card)
        return cards

    def play(self):
        index = 0
        while True:
            result = self.play_turn(index)
            rotate_index = index + 1
            if result == PLAYER1:
                self.nb_rounds += 1
                self.deck1 = self.rotate(self.deck1, rotate_index)
                # take other player's cards
                self.deck1 += self.deck2[:rotate_index]
                # remove other player's cards
                del self.deck2[:rotate_index]
                index = 0
            elif result == PLAYER2:
                self.nb_rounds += 1
                # take other player's cards
                self.deck2 += self.deck1[:rotate_index]
                # remove other player's cards
                del self.deck1[:rotate_index]
                self.deck2 = self.rotate(self.deck2, rotate_index)
                index = 0
            else:  # WAR
                index += 4

    def rotate(self, deck, index):
        return deck[index:] + deck[:index]

    def play_turn(self, index):
        """ Returns the result of one game turn. """
        if index > len(self.deck1) or index > len(self.deck2):
            print("PAT")
            exit()

        self.check_game_over()

        card1 = self.deck1[index]
        card2 = self.deck2[index]
        if card2 < card1:
            return PLAYER1
        elif card1 < card2:
            return PLAYER2
        else:
            return WAR

    def check_game_over(self):
        if len(self.deck1) == 0:
            print("2 {}".format(self.nb_rounds))
            exit()
        if len(self.deck2) == 0:
            print("1 {}".format(self.nb_rounds))
            exit()

    def show_decks(self):
        print(self.nb_rounds, file=sys.stderr)
        print(self.deck1, file=sys.stderr)
        print(self.deck2, file=sys.stderr)


game = Game()
game.play()
