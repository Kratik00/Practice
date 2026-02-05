import random

lst = ['rock', 'paper', 'scissors']

print("☆Welcome to the terminal☆")
while True:
  choice = input("Want to play or not? (Y/N): ").strip().upper()
  if choice == "Y":
    computer_option = random.randint(1, 3)
    computer_choice = lst[computer_option-1]
    while True:
      x = input("Enter your choice like\n 1 for rock,\n 2 for paper,\n 3 for scissors\n ")
      try:
        user_option = int(x)
        if 1 <= user_option <= 3:
          break
        else:
          print("Choose only between 1 to 3")
      except ValueError:
        print("Enter Numbers only")
    user_choice = lst[user_option-1]
    print(f'You chose : {user_choice}')
    print(f'Computer chose : {computer_choice}')
    if user_option == computer_option:
      print("Match Draw")
    elif (user_option - computer_option)%3 == 1:
      print("You won")
    else:
      print("Computer Wins")
  elif choice == "N":
    print("Thanks for playing")
    break
  else:
    print("Make sure to choose only in Y Or N")
  print("\n---------------------\n")
          
        
        
      