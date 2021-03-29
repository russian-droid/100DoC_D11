#
#BlackJack
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

#-------------------------myTry

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

total_user = sum(user)
print(f'total_comp {total_user}') #QC
#pick a random card
choice = input("\nWish to play another card? Enter 'y' for yes, or 'n' for no\n")
if choice == 'y':
    temp_card3=pull_random_card()
print(f'random_card NEW:{temp_card3}')
#if ACE decide 11 or 1
if temp_card3 == 11:
    temp_card3=ace_check(total_user)
#add to the list
user.append(temp_card3)
#print(f"user: {temp_card2}\n") #QC
print(user) #QC
if check_if_over21(user):
    print('user is LOST')
