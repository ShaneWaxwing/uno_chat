import random

# def in_bounds(num):
#     if num == 3:
#         num -= 3
#     elif num < 3:
#         num += 1
#     return num

# def create_deck():
#     value = ['1','2','3','4','5','6','7','8','9', 'Reverse!', 'Skip!', 'Draw two!']
#     color = ['Green ','Blue ','Red ','Yellow ']
#     left_overs = ['Green 0', 'Blue 0', 'Red 0', 'Yellow 0', 'Wild Draw Four!', 'Wild Draw Four!', 'Wild Draw Four!', 'Wild Draw Four!', 'Wild!', 'Wild!', 'Wild!', 'Wild!']
#     deck = []
#     index = 0
#     multiplyer = 12

#     while len(deck) < 96:
    
#         for i in value:
#             card = color[index] + i
#             deck.append(card)
#             if len(deck) == multiplyer:
#                 index = in_bounds(index)
#                 multiplyer += 12
#     for i in left_overs:
#         deck.append(i)
#         random.shuffle(deck)
#         random.shuffle(deck)
#         random.shuffle(deck)

#     return deck

deck = ['Green 0', 'Green 1', 'Green 1', 'Green 2', 'Green 2', 'Green 3', 'Green 3', 'Green 4', 'Green 4', 'Green 5', 'Green 5', 'Green 6', 'Green 6', 'Green 7', 'Green 7', 'Green 8', 'Green 8', 'Green 9', 'Green 9', 'Green Reverse!', 'Green Reverse!', 'Green Skip!', 'Green Skip!', 'Green Draw Two!', 'Green Draw Two!',
'Blue 0', 'Blue 1', 'Blue 1', 'Blue 2', 'Blue 2', 'Blue 3', 'Blue 3', 'Blue 4', 'Blue 4', 'Blue 5', 'Blue 5', 'Blue 6', 'Blue 6', 'Blue 7', 'Blue 7', 'Blue 8', 'Blue 8', 'Blue 9', 'Blue 9', 'Blue Reverse!', 'Blue Reverse!', 'Blue Skip!', 'Blue Skip!', 'Blue Draw Two!', 'Blue Draw Two!',
'Yellow 0', 'Yellow 1', 'Yellow 1', 'Yellow 2', 'Yellow 2', 'Yellow 3', 'Yellow 3', 'Yellow 4', 'Yellow 4', 'Yellow 5', 'Yellow 5', 'Yellow 6', 'Yellow 6', 'Yellow 7', 'Yellow 7', 'Yellow 8', 'Yellow 8', 'Yellow 9', 'Yellow 9', 'Yellow Reverse!', 'Yellow Reverse!', 'Yellow Skip!', 'Yellow Skip!', 'Yellow Draw Two!', 'Yellow Draw Two!',
'Red 0', 'Red 1', 'Red 1', 'Red 2', 'Red 2', 'Red 3', 'Red 3', 'Red 4', 'Red 4', 'Red 5', 'Red 5', 'Red 6', 'Red 6', 'Red 7', 'Red 7', 'Red 8', 'Red 8', 'Red 9', 'Red 9', 'Red Reverse!', 'Red Reverse!', 'Red Skip!', 'Red Skip!', 'Red Draw Two!', 'Red Draw Two!',
'Wild!', 'Wild!', 'Wild!', 'Wild!', 'Wild Draw Four!', 'Wild Draw Four!', 'Wild Draw Four!', 'Wild Draw Four!']
random.shuffle(deck)
random.shuffle(deck)


player2_hand = []
player1_hand = []
discard_pile = []


while len(player1_hand) < 7 and len(player2_hand) < 7: #--------------------------------------------------> Deals the cards one at a time alternating between players
    card = deck.pop(0)
    player1_hand.append(card)
    card = deck.pop(0)
    player2_hand.append(card)


def action_card(played_card):
    if played_card.__contains__('Skip'):
        return "SKIP"
    elif played_card.__contains__('Reverse'):
        return 'REVERSE'
    elif played_card.__contains__('Draw'):
        return 'DRAW TWO'
    else:
        return 'WILD'
    

        

#     Card      |  Index   |  Value
#________________________________
# Red Reverse       4           R
# Red Skip          4           S
# Red Draw Two      4           D

# Green Reverse     6           R
# Green Skip        6           S
# Green Draw Two    6           D

# Yellow Reverse    7           R
# Yellow Skip       7           S
# Yellow Draw Two   7           D

# Blue Reverse      5           R
# Blue Skip         5           S
# Blue Draw Two     5           D


def action_check(played_card): #-------------------------------------------------------------------------> Evaluates played card to determine whether or not it's an action card
     if played_card[-1] != '!':
         return
     else:
         return action_card(played_card)
        


def check_play(top_card, played_card): #----------------------------------------------------------------> Checks that you can play that card
    if top_card[0] == played_card[0]:
        return True
    elif top_card[-1] == played_card[-1]:
        return True
    elif played_card[0] == 'W':
        return True
    else:
        return False
    
def top_card_checker(deck): #---------------------------------------> Ensures that the top card at the begining of the game is a number card.
    top_card = deck[0]
    status = False
    for char in top_card:
        num = ord(char)
        if num != 33:
            status = False
        else:
            status = True
    return status


while top_card_checker(deck):
    card = deck.pop(0)
    deck.append(card)        

discard_pile.append(deck[0])

top_card = discard_pile[0]

game_on = True

print("\nWelcome to UNO Classic!\n")
player1 = input("Player 1, enter your name: \n")
player2 = input("Player 2, enter your name: \n")
player1_turn_complete = False
player2_turn_complete = True

while game_on == True: # --------------------------------------------------------------------------------------> Game Starts here 
    
    if player2_turn_complete == True:
    
        top_card = discard_pile[0]
        print('___________________________________________________________________________________')
        print(f'{player1.title()}:')
        print(f"The top card is: {top_card}")
        print(player1_hand)
        move = input("Choose a card by it's index: ") # --------------------------------------------------------> Player 1's Turn
        print(f'You selected {player1_hand[int(move)]}')#---------------------------------------------------------------------->       Test

        # Put function here to pass 'move' to to evaluate for action cards #


        if check_play(top_card, player1_hand[int(move)]) == True: # ------------------------------------(If this card is playable)
            card = player1_hand.pop(int(move))
            discard_pile.insert(0, card)
            player1_turn_complete = True
            player2_turn_complete = False

        else:
            print(' ')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('Invalid move, pick again.')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print(f"{player2.title()}'s cards: {player2_hand}")
            


    if player1_turn_complete == True:

        top_card = discard_pile[0] #---------------------------------------------------------------------------------> Player 2's Turn
        print('___________________________________________________________________________________')
        print(f'{player2.title()}:')
        print(f"The top card is: {top_card}")
        print(player2_hand)
        move = input(f"{player2.title()}, choose a card by it's index: ")
        print(f'You selected {player2_hand[int(move)]}')#---------------------------------------------------------------------->       Test

        if check_play(top_card, player2_hand[int(move)]) == True:
            card = player2_hand.pop(int(move))
            discard_pile.insert(0, card)
            player2_turn_complete = True
            player1_turn_complete = False
        else:
            print(' ')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('Invalid move, pick again.')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
            player2_turn_complete = False