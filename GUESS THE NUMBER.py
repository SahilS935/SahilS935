import random

# intro logic
print("Welcome to the game!\n"
      "Be ready to guess the correct number")

# get the input from user
number = int(input("Please enter a number between 0 to 9: "))

# computer generated value
computer_number = random.randint(0, 9)

# comparing and deciding
if number == computer_number:
    print("You guessed the correct number!", computer_number)
else:
    print("Oh no, you didn't win this time!\n"
          "The correct number was", computer_number)