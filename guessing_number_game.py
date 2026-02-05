import random

print("Welcome to the terminal♡")
number = random.randint(1, 100)
while True:
  user_input = input("Enter your guessed number between 1 to 100: ")
  if user_input.isdigit():
    guess = int(user_input)
    difference = abs(number - guess)
    if difference == 0:
      print("Congratulation You won the game. ")
      break
    elif difference <= 5:
      print("too close")
    elif difference <= 10:
      print("little close")
    elif difference <= 20:
      print("little far")
    else:
      print("Too far")
  else:
    print("Please enter only integer")
  
    


