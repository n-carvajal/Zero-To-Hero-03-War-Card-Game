# Import random module.
import random

# Game Constants
# Tuple of card suits.
SUITS = (
    "Hearts",
    "Diamonds",
    "Spades",
    "Clubs",
)
# Tuple of card faces.
RANKS = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
# Dictionary of faces : value pairs.
VALUES = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}


# Card class.
class Card:
    """
    Creates Card objects that represent a playing card.
    """
    def __init__(self, suit, rank):
        """
        Upon instantiation Card object attributes suit, face, and value are created.
        """
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        """
        Returns a string that represents the Card object for the print function.
        """
        return f"{self.rank.title()} of {self.suit.title()}"


# Deck class.
class Deck:
    """
    Creates Deck objects to hold 52 instances Card objects.
    """
    def __init__(self):
        """
        Upon instantiation of a Deck object 52 Card objects are created and appended to attribute all_cards.
        """
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.all_cards.append(card)

    def shuffle_cards(self):
        """
        Method that shuffles the Card objects inside self.all_cards.
        """
        random.shuffle(self.all_cards)

    def deal_card(self):
        """
        Method that simulates removing a single Card object from the top of the deck object by popping a card
        object from self.all_cards.
        """
        return self.all_cards.pop()


# Player class.
class Player:
    """
    Creates Player objects that can hold Card objects.
    """
    def __init__(self, name):
        """
        Upon instantiation the Player object is assigned a name attribute and all_cards attribute.
        Where all_cards is an empty list.
        """
        self.name = name
        self.all_cards = []

    def play_card(self):
        """
        Method that simulates removing a single Card object from the top of the Player object's all_cards by popping
        a card object from self.all_cards.
        """
        return self.all_cards.pop(0)

    def pick_up_card(self, pick_up):
        """
        Method that simulates picking up Card objects and placing at the bottom of a Player object's all_cards.
        If the card object to pick up is a list with multiple values, the .extend() method will be used.
        If the card object is a single item, the .append() method will be used.
        """
        if isinstance(pick_up, list):
            return self.all_cards.extend(pick_up)
        else:
            return self.all_cards.append(pick_up)

    def __str__(self):
        """
        Returns a custom print string for the print function.
        """
        return f"{self.name} has {len(self.all_cards)} cards."


# Create game variables
cards_played = []
war_cards = []
stake_cards = 5

# Instantiate the players and deck.
deck = Deck()
player_1 = Player("Player 1")
player_2 = Player("Player 2")

# Shuffle the deck.
deck.shuffle_cards()

# Deal out half the deck to player_1.
for _ in range(26):
    player_1.all_cards.append(deck.deal_card())
    player_2.all_cards.append(deck.deal_card())

# Create match counter:
counter = 0

# Create while loop that ends game when either player has the whole deck in their possession.
game_over = False
while not game_over:

    # Start match counter:
    counter += 1
    print(f"Match Number: {counter}")

    # Have each player play a card and append to cards_played:
    player_1_played_card = player_1.play_card()
    cards_played.append(player_1_played_card)
    player_2_played_card = player_2.play_card()
    cards_played.append(player_2_played_card)

    # Print each player's played card.
    print(f"Player 1 played the {player_1_played_card.rank} of {player_1_played_card.suit}.")
    print(f"Player 2 played the {player_2_played_card.rank} of {player_2_played_card.suit}.")

    # If player_1's card is greater than player_2's card.
    if player_1_played_card.value > player_2_played_card.value:
        # player_1 take cards_played.
        player_1.pick_up_card(cards_played)
        # Clear cards_played list.
        cards_played = []
        # Print player_1 winner.
        print("Player 1 wins")
        # Print player_1  and player 2 status.
        print(player_1)
        print(player_2)
        print("\n")

    # Else if player_2's card is greater than player_1's card.
    elif player_2_played_card.value > player_1_played_card.value:
        # player_2 pick up cards_played.
        player_2.pick_up_card(cards_played)
        # Clear cards_played list.
        cards_played = []
        # Print player_2 winner.
        print("Player 2 wins")
        # Print player_2 and player_1 status.
        print(player_2)
        print(player_1)
        print("\n")

    # Else if both players played a card of equal value.
    elif player_2_played_card.value == player_1_played_card.value:
        war = True
        while war:
            print("War Declared")

            # If player_1 does not have enough cards to wage war.
            if len(player_1.all_cards) < stake_cards + 1:
                # Give all player_1 cards to player_2.
                player_2.pick_up_card(player_1.all_cards)
                # Set player_1 cards to zero.
                player_1.all_cards = []
                # Have player_2 pick up cards_played.
                player_2.pick_up_card(cards_played)
                # Set cards_played to zero.
                cards_played = []
                # Have player_2 pick up any war_cards from previous war in any.
                player_2.pick_up_card(war_cards)
                # Set war_cards to zero.
                war_cards = 0
                # Print player_2 winner.
                print("Player 2 wins")
                # Print player_2 and player_1 status.
                print(player_2)
                print(player_1)
                print("\n")
                # Set game_over to True.
                game_over = True
                # Set war to False.
                war = False

            # Else if player_2 does not have enough cards to wage war.
            elif len(player_2.all_cards) < stake_cards + 1:
                # Give all player_2 cards to player_1.
                player_1.pick_up_card(player_2.all_cards)
                # Set player_2 cards to zero.
                player_2.all_cards = []
                # Have player_1 pick up cards_played.
                player_1.pick_up_card(cards_played)
                # Set cards_played to zero.
                cards_played = []
                # Have player_1 pick up previous war_cards if any.
                player_1.pick_up_card(war_cards)
                # Set war_cards to zero.
                war_cards = []
                # Print player_1 winner.
                print("Player 1 wins")
                # Print player_1  and player 2 status.
                print(player_1)
                print(player_2)
                print("\n")
                # Set game_over to True.
                game_over = True
                # Set war to False.
                war = False

            # Else
            else:
                # Have each player append stake_cards to war_cards.
                for _ in range(stake_cards):
                    war_cards.append(player_1.play_card())
                    war_cards.append(player_2.play_card())

                # Have each player play additional card and append to played cards.
                player_1_played_card = player_1.play_card()
                cards_played.append(player_1_played_card)
                player_2_played_card = player_2.play_card()
                cards_played.append(player_2_played_card)

                # If player_1's card is greater than player_2's card.
                if player_1_played_card.value > player_2_played_card.value:
                    # player_1 take cards_played.
                    player_1.pick_up_card(cards_played)
                    # Clear cards_played list.
                    cards_played = []
                    # Player_1 takes war_cards.
                    player_1.pick_up_card(war_cards)
                    # Clear war_cards.
                    war_cards = []
                    # Print player_1 winner.
                    print("Player 1 wins")
                    # Print player_1  and player 2 status.
                    print(player_1)
                    print(player_2)
                    print("\n")
                    # Set war to False.
                    war = False

                # Else if player_2's card is greater than player_1's card.
                elif player_2_played_card.value > player_1_played_card.value:
                    # player_2 pick up cards_played.
                    player_2.pick_up_card(cards_played)
                    # Clear cards_played list.
                    cards_played = []
                    # Player_2 takes war_cards.
                    player_2.pick_up_card(war_cards)
                    # Clear war_cards.
                    war_cards = []
                    # Print player_2 winner.
                    print("Player 2 wins")
                    # Print player_2 and player_1 status.
                    print(player_2)
                    print(player_1)
                    print("\n")
                    # Set war to False.
                    war = False

                # Else if both players played a card of equal value.
                elif player_2_played_card.value == player_1_played_card.value:
                    continue

    # If more than 500 rounds played shuffle player hands.
    # To avoid cards sometimes stacking and getting into 100000s of iterations with no winner.
    if counter > 500:
        random.shuffle(player_1.all_cards)
        random.shuffle(player_2.all_cards)

    # Check if player_1 or player_2 have an empty hand.
    if len(player_1.all_cards) == 0 or len(player_2.all_cards) == 0:
        game_over = True

print("Game Over")
print(player_1)
print(player_2)
