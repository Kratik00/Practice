# import random
# print("WELCOME TO DICE ROLLING GAME")
# #dice = [1, 2, 3, 4, 5, 6]
# def dice_rolling(response):
#   if response == "Y":
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     #print(random.choices(dice, k=2))
#     print((dice1,dice2))
#   elif response == "N":
#     print("Thanks for playing")
#   else:
#     print("Wrong Input")
# response = input("Choose you want to play or not choosing Y or N: ").strip().upper()
# dice_rolling(response)

#-------FOR REAPEATING TILL RUNNING CODE------
# import random
# import time
# print("WELCOME TO DICE ROLLING GAME")
# while True:
#   response = input("Roll Dice? Y FOR YES AND N FOR NO: ").strip().upper()
#   if response == "Y":
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     print("Rolling", end="")
#     for _ in range(5):
#       print(".", end="", flush=True)
#       time.sleep(0.5)
#     print((dice1, dice2))
#   elif response == "N":
#     print("Thanks for playing")
#     break
#   else:
#     print("Wrong input choose only Y or N")
#--------Like casino style animation-------
import random
import time
print("Welcome to the Dice rolling game")
while True:
  response = input("----Roll dice----\nChoose Y for yes and N for No: ").strip().upper()
  if response == "Y":
    print("Rolling.", end="", flush=True)
    for _ in range(5):
      fake1 = random.randint(1, 6)
      fake2 = random.randint(1, 6)
      print("\r☆Rolling..", (fake1, fake2), end="", flush=True)
      time.sleep(0.6)
    print("\nFinal result: ", (fake1, fake2))
  elif response == "N":
    time.sleep(0.4)
    print("Thanks for playing")
    break
  else:
    time.sleep(0.4)
    print("Wrong input choose only in Y or N")
  