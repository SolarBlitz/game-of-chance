import random as ran

money = 100

#Write your game of chance functions here
def coin_flip(bet, guess):
  side_of_coin = ran.randint(1,2)
  if guess == "Heads" or "heads" or "Heads!" or "heads!":
    guess = 1
  if guess == "Tails" or "tails" or "Tails!" or "tails!":
    guess = 2
  if guess == side_of_coin:
    print("You win the Coin Flip!")
    if guess == 1:
      print("Thanks for picking Heads, it makes you a winner")
    elif guess == 2:
      print("Thanks for picking Tails, it makes you a winner")
    return bet + 5
  else:
    print("You Lose! Flip some more coins soon")
    return - 5

def cho_han(bet, guess):
  dice1= ran.randint(1,6)
  dice2= ran.randint(1,6)
  sum_of_dice = dice1 + dice2
  guess_list = [guess]
  if guess_list[0] == "odd!" or "Odd!" or "odd" or "Odd":
    guess = "Odd"
  if guess_list[0] == "Even" or "even" or "even!" or "Even!":
    guess = "Even"
  mod_sum_of_dice = sum_of_dice % 2
  if mod_sum_of_dice > 0:
    sum_of_dice = "Odd"
  else:
    sum_of_dice = "Even"
  
  if guess == sum_of_dice:
    print("You win! You guessed the right sum!")
    return bet + 5
  else:
    print("You Lose! Try again at guessing the right sum")
    return - 5

def high_card(bet, guess):
  user_card = ran.randint(1, 13)
  computer_card = ran.randint(1, 13)
  guess = user_card
  if guess > computer_card:
    print("You Win! You have the high card!")
    return bet + 5
  elif guess == computer_card:
    print("It is a Tie! You had the same card!")
    return bet
  else:
    print("You Lose! You got the lower card")
    return - 5
  
def roulette(bet, guess):
  table_number = ran.randint(0,37)
  table_number_mod = 0
  guess_list = [guess]
  if guess_list[0] == "odd!" or "Odd!" or "odd" or "Odd":
    guess = "Odd"
  if guess_list[0] == "Even" or "even" or "even!" or "Even!":
    guess = "Even"
  if table_number % 2 > 0:
    table_number_mod = "Odd"
  else:
    table_number_mod = "Even"

  if guess == table_number_mod:
    print("You guessed right. The roullette table stopped on a " + guess + " number.")
    return bet + bet
  elif guess == table_number:
    if guess == 0 or guess == 37:
      print("You won it big!")
      return bet * 10
    print("You picked the right number! The roullette number " + guess + " was the right one.")
    return bet + table_number
  else:
    print("You Lost! Try the roullette table soon again soon.")
    return - bet
if money < 10:
  print("You are about to run out of money, you should stop")
elif money == 0:
  print("You are all out of money, you can no longer play.")
  quit


#Call your game of chance functions here
money += coin_flip(10, "Heads")
print(money)
money += cho_han(10, "Odd")
print(money)
money += high_card(10, "higher")
print(money)
money += roulette(10, "Odd")
print(money)