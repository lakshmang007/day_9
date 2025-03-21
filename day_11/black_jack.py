import random as r

def random_card():
    deck = [ 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    return r.choice(deck)

def black_jack():
    deck = [ 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    player = []
    dealer = []
    player_score = 0
    dealer_score = 0
    player.append(random_card())
    player.append(random_card())
    dealer.append(random_card())
    dealer.append(random_card())
    print("Player: ", player)
    print("Dealer: ", dealer)
    player_score = sum(player)
    dealer_score = sum(dealer)
    print("Player score: ", player_score)
    print("Dealer score: ", dealer_score)
    if player_score > 21:
        print("Player busted")
    elif dealer_score > 21:
        print("Dealer busted")
    elif player_score == 21:
        print("Player wins")
    elif dealer_score == 21:
        print("Dealer wins")
    elif player_score > dealer_score:
        print("Player wins")
    elif dealer_score > player_score:
        print("Dealer wins")
    else:
        print("Draw")

black_jack()