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
    print(f'random card from function {random_card}') #QC
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

def ace_check(total):
    '''
    check if ACE has to count as 11 point or 1 point
    '''
    if total + 11 > 21:
        random_card = 1
        print('ACE = 1')
        return random_card
    else:
        random_card = 11
        print('ACE = 11')
        return random_card
'''
#pick random cards via random_card() and save in the list for comp
comp.append(random_card())
comp.append(random_card())
print(f"comp: {comp}") #QC

#pick random cards via random_card() and save in the list for user
user.append(random_card())
user.append(random_card())
print(f"user: {user}\n") #QC


if check_if_blacjack(comp) == True:
    print('*computer WON*')
    #END GAME
else:
    if check_if_blacjack(user) == True:
        print('*user WON*')
        #END GAME
    #else: #QC
    #    print('keep playing') #QC
'''

#calc score comp
total_comp = sum(comp)
print(f'total_comp {total_comp}')
#pick a random card
random_card()
print(f'random_card NEW:{random_card}')
#if ACE decide 11 or 1
if random_card == 11:
    ace_check(total_comp)
#add to the list
comp.append(random_card)
print(f"comp: {comp}") #QC

#calc score user
total_user = sum(user)
print(f'total_user {total_user}')
random_card()
print(f'random_card NEW:{random_card}')
if random_card == 11:
    ace_check(total_user)
user.append(random_card)
print(f"user: {user}") #QC
