from replit import clear
from art import logo
import random
 
def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

player_hand = []
computer_hand = []

def calculated_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)



def compare(player_score, computer_score):
  if player_score == computer_score:
    return "DRAW."
  elif computer_score == 0:
    return "Lose, opponent has Blackjack."
  elif player_score == 0:
    return "Win with a Blackjack."
  elif player_score > 21:
    return "You overpass 21. You lose."
  elif computer_score > 21:
    return "Computer overpass 21. You win."
  elif player_score > computer_score:
    return "You win."
  else:
    return "You lose."
  
  
def play_game():
  print(logo)
  player_hand = []
  computer_hand = []
  game_over = False
    
  for i in range(2):
   player_hand.append(deal_cards())
  
  while not game_over:  
    computer_hand.append(deal_cards())
    
    player_score = calculated_score(player_hand)
    
    computer_score = calculated_score(computer_hand)
    
    print(f"Your cards: {player_hand}. Your score: {player_score}")
    print(f"Computer's first card: {computer_hand[0]}")
    
    if player_score == 0 or computer_score == 0 or player_score > 21:
      game_over = True
    else:
      draw_card = input("Type 'y' to get another card, or 'n' to pass.  ")
      if draw_card =='y':
        player_hand.append(deal_cards())
      else:
        game_over = True
  
     
  while computer_score != 0  and computer_score < 17:
    computer_hand.append(deal_cards())
    computer_score = calculated_score(computer_hand)
      
  
  print(f" Your final hand: {player_hand}, final score: {player_score}. ")
  print(f" Computer's final hand: {computer_hand}, final score: {computer_score}.")
  
  print(compare(player_score, computer_score))

while input("Do you wanna play a game of Blackjack? Type 'y' or 'n'. ") == 'y':
  clear()
  play_game()
