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

def pull_random_card():
    '''
    picks a random card from the list
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #pick a random element from the list
    random_element = random.randint(0,(len(cards)-1))
    #get the number inside that element
    card = cards[random_element]
    #print(f'random card from function {card}') #QC
    return card

def check_if_blacjack(list):
    '''
    checks if blackJack happened
    '''
    total = sum(list)
    if total == 21:
        return True
    else:
        return False

def check_if_over21(list):
    '''
    checks if total is over 21
    '''
    total = sum(list)
    if total > 21:
        return True
    else:
        return False    

def ace_check(total):
    '''
    check if ACE has to count as 11 point or 1 point
    '''
    if total + 11 > 21:
        ace = 1
        #print('ACE = 1') #QC
        return ace
    else:
        ace = 11
        #print('ACE = 11') #QC
        return ace

#pick random cards via pull_random_card() and save in the list for comp
comp.append(pull_random_card())
comp.append(pull_random_card())
print(f"comp: {comp}") #QC

#pick random cards via pull_random_card() and save in the list for user
user.append(pull_random_card())
user.append(pull_random_card())
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


#calc score comp
total_comp = sum(comp)
print(f'total_comp {total_comp}') #QC
#pick a random card
temp_card1=pull_random_card()
print(f'random_card NEW:{temp_card1}')
#if ACE decide 11 or 1
if temp_card1 == 11:
    temp_card1=ace_check(total_comp)
#add to the list
comp.append(temp_card1)
#print(f"comp: {temp_card1}\n") #QC
print(comp) #QC
if check_if_over21(comp):
    print('comp is LOST')

#calc score user
total_user = sum(user)
print(f'total_comp {total_user}') #QC
#pick a random card
temp_card2=pull_random_card()
print(f'random_card NEW:{temp_card2}')
#if ACE decide 11 or 1
if temp_card2 == 11:
    temp_card2=ace_check(total_user)
#add to the list
user.append(temp_card2)
#print(f"user: {temp_card2}\n") #QC
print(user) #QC
if check_if_over21(user):
    print('user is LOST')
