#

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
print('\033c') #clean screen

#comp cards
comp=[]
#user cards
user=[]

def random_card():
    '''
    picks a random card from the list
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #pick a random element from the list
    random_element = random.randint(0,(len(cards)-1))
    #get the number inside that element
    random_card = cards[random_element]
    #print(random_card) #QC
    return random_card

def check_if_blacjack(list):
    '''
    checks if blackJack happened
    '''
    total = sum(list)
    if total == 21:
        return True
    else:
        return False

#pick random card via random_card() and save in the list for comp
comp.append(random_card())
comp.append(random_card())
print(f"comp: {comp}") #QC

#pick random card via random_card() and save in the list for user
user.append(random_card())
user.append(random_card())
print(f"user: {user}") #QC

if check_if_blacjack(comp) == True:
    print('*computer WON*')
    #END GAME
else:
    if check_if_blacjack(user) == True:
        print('*user WON*')
        #END GAME
    #else: #QC
    #    print('keep playing') #QC

#calc score
total_comp = sum(comp)
print(total_comp)
total_user = sum(user)
print(total_user)

#pick random card via random_card() and save in the list for comp
comp.append(random_card())
print(f"comp: {comp}") #QC
#pick random card via random_card() and save in the list for user
user.append(random_card())
print(f"user: {user}") #QC

