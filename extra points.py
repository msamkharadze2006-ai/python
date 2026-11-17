import random
from collections import Counter

# cards

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


# card deck

class Deck:
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in self.suits
                      for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


# players

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0

    def place_bet(self, amount):
        self.bet += amount

    def clear_hand(self):
        self.hand = []
        self.bet = 0


#poker game

class PokerGame:
    rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12,
        'K': 13, 'A': 14
    }

    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.community_cards = []

    # There should be a method to deal 2 cards for n amounts of players.
    def deal_hole_cards(self):
        for _ in range(2):
            for player in self.players:
                player.hand.append(self.deck.draw())

    # A method that reveals 5 on table with burns.
    def reveal_community_cards(self):

        # Burn + Flop
        self.deck.draw()
        for _ in range(3):
            self.community_cards.append(self.deck.draw())

        # Burn + Turn
        self.deck.draw()
        self.community_cards.append(self.deck.draw())

        # Burn + River
        self.deck.draw()
        self.community_cards.append(self.deck.draw())

    # A method that evaluates the winning hand.
    # (highest card only)
    def evaluate_winner(self):

        best_player = None
        best_score = 0

        for player in self.players:

            all_cards = player.hand + self.community_cards

            values = [
                self.rank_values[card.rank]
                for card in all_cards
            ]

            score = max(values)

            if score > best_score:
                best_score = score
                best_player = player

        return best_player

    # Reset game
    def reset_game(self):

        self.deck = Deck()
        self.community_cards = []

        for player in self.players:
            player.clear_hand()

    # Display helper
    def show_table(self):

        print("\nCommunity Cards:")
        print(" ".join(str(card) for card in self.community_cards))

        print("\nPlayers:")

        for player in self.players:
            hand = " ".join(str(card) for card in player.hand)
            print(f"{player.name}: {hand} | Bet: {player.bet}")


#test(i wanted to make sure everything works)

game = PokerGame(["Alice", "Bob", "Charlie"])

game.deal_hole_cards()

game.players[0].place_bet(50)
game.players[1].place_bet(75)

game.reveal_community_cards()

game.show_table()

winner = game.evaluate_winner()

print(f"\nWinner: {winner.name}")

game.reset_game()

print("\nGame reset complete.")