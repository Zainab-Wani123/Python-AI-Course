#create function to shuffe cards
def shuffle_cards():
    import random
    # Create a standard deck of 52 playing cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]
    # Shuffle the deck
    random.shuffle(deck)
    return deck

# Function call
shuffled_deck = shuffle_cards()
# Print the shuffled deck
print("Shuffled Deck of Cards:")
for card in shuffled_deck:
 print(card)


