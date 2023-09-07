import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Define a function to create a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f'{rank} of {suit}'
            deck.append(card)
    return deck

# Define a function to calculate the total value of a hand
def calculate_hand_value(hand):
    total_value = sum(values[card.split()[0]] for card in hand)
    num_aces = hand.count('Ace of Hearts') + hand.count('Ace of Diamonds') + hand.count('Ace of Clubs') + hand.count(
        'Ace of Spades')

    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

# Define a function to display a player's hand
def display_hand(hand):
    for card in hand:
        print(card)

# Initialize the game
deck = create_deck()
random.shuffle(deck)

player_hand = []
dealer_hand = []

# Deal the initial two cards to the player and dealer
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Main game loop
while True:
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    # Display hands
    print("Player's Hand:")
    display_hand(player_hand)
    print(f"Player's Hand Value: {player_total}\n")

    print("Dealer's Hand:")
    display_hand(dealer_hand[:1])
    print("\n")

    # Check for player bust
    if player_total > 21:
        print("Player busts! Dealer wins.")
        break

    # Ask the player for their move
    player_move = input("Do you want to 'hit' (h) or 'stand' (s)? ").lower()

    if player_move == 'h':
        player_hand.append(deck.pop())
    elif player_move == 's':
        # Dealer's turn
        while dealer_total < 17:
            dealer_hand.append(deck.pop())
            dealer_total = calculate_hand_value(dealer_hand)

        # Display final hands
        print("Player's Hand:")
        display_hand(player_hand)
        print(f"Player's Hand Value: {player_total}\n")

        print("Dealer's Hand:")
        display_hand(dealer_hand)
        print(f"Dealer's Hand Value: {dealer_total}\n")

        # Determine the winner
        if dealer_total > 21:
            print("Dealer busts! Player wins.")
        elif player_total > dealer_total:
            print("Player wins!")
        elif player_total < dealer_total:
            print("Dealer wins.")
        else:
            print("It's a tie!")
        break
    else:
        print("Invalid input. Please enter 'hit' (h) or 'stand' (s).")

