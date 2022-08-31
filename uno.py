import random


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

def action_card(played_card):
    global player1_turn_complete
    global player2_turn_complete
    
    if played_card.__contains__('Draw Two'):
        if player2_turn_complete == True and player1_turn_complete == False:
            card = deck.pop(0)
            player1_hand.append(card)
            card = deck.pop(0)
            player1_hand.append(card)
        elif player1_turn_complete == True and player2_turn_complete == False:
            card = deck.pop(0)
            player2_hand.append(card)
            card = deck.pop(0)
            player2_hand.append(card)


def action_check(played_card): #-------------------------------------------------------------------------> Evaluates played card to determine whether or not it's an action card
     if played_card[-1] != '!':
         return
     else:
         return action_card(played_card)


while game_on == True: # --------------------------------------------------------------------------------------> Game Starts here 
    
    if player2_turn_complete == True:
    
        top_card = discard_pile[0]
        action_card(top_card)#--------------------------------------------------> Handles draw two Cards Only
        ###################
        print('___________________________________________________________________________________')
        print(f'{player1.title()}:')
        print(f"The top card is: {top_card}")
        print(player1_hand)
        move = input("Choose a card by it's index: ") # --------------------------------------------------------> Player 1's Turn
        print(f'You selected {player1_hand[int(move)]}')#---------------------------------------------------------------------->       Test
        # Evaluate played card to check for wilds and wild draw fours here
        


        if check_play(top_card, player1_hand[int(move)]) == True: # ------------------------------------(If this card is playable)
            card = player1_hand.pop(int(move))
            discard_pile.insert(0, card)
            if discard_pile[0].__contains__('Skip'):
                if player2_turn_complete == True and player1_turn_complete == False:
                    player1_turn_complete = True
                    player2_turn_complete = False
                elif player2_turn_complete == False and player1_turn_complete == True:
                    player1_turn_complete = False
                    player2_turn_complete = True
            else:
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
        action_card(top_card)
        ##########
        print('___________________________________________________________________________________')
        print(f'{player2.title()}:')
        print(f"The top card is: {top_card}")
        print(player2_hand)
        move = input(f"{player2.title()}, choose a card by it's index: ")
        print(f'You selected {player2_hand[int(move)]}')#---------------------------------------------------------------------->       Test
        print(f'Player 1 turn complete: {player1_turn_complete}')
        print(f'Player 2 turn complete: {player2_turn_complete}')
        
        # Evaluate played card to check for wilds and wild draw fours here
        if check_play(top_card, player2_hand[int(move)]) == True:
            card = player2_hand.pop(int(move))
            discard_pile.insert(0, card)
            if discard_pile[0].__contains__('Skip'):
                if player2_turn_complete == True and player1_turn_complete == False:
                    player1_turn_complete = True
                    player2_turn_complete = False
                elif player2_turn_complete == False and player1_turn_complete == True:
                    player1_turn_complete = False
                    player2_turn_complete = True
        else:
            player1_turn_complete = True
            player2_turn_complete = False
        print(' ')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('Invalid move, pick again.')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        player2_turn_complete = False