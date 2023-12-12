from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
#2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
  hand_value = 0#user's value
  run_time = 0#
  while run_time < 2:
    player = randint(1, 13)
    card_name = draw(player)
    print(f"{card_name}")
    hand_value += card_value(player)
    run_time +=1
  while hand_value <21:
    user = input(f"You have {hand_value}. Hit (y/n)? ")
    if user =='y':
      player = randint(1,13)
      card_name = draw(player)
      print(f"{card_name}")
      hand_value += card_value(player)
    elif user =='n':
      print(f"Final hand: {hand_value}.")
      break
    else:
      print(f"Sorry I didn't get that.")
  



  

  
  
  

play_human_turn()
