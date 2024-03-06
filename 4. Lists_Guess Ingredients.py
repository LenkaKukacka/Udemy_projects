import time

recipe_ingredients = ["flour", "butter", "eggs", "milk", "sugar", "baking powder", "chocolate", "salt"]
score = 0
print("Hello! Let´s play a game. We will make a chocolate cookies together. Guess what are the ingredients? You have got 3 guesses and must get 3 ingredients right to win the game.")
time.sleep(8)
print()
first_guess = input("What is the first ingredient you guess?")
if first_guess in recipe_ingredients:
  print("Well done, this is right.")
  score = score + 1 # or score += 1 ...je to same
else:
  print("Sorry, it is not right.")
print()
second_guess = input("Try the second guess.")
if second_guess in recipe_ingredients and second_guess != first_guess:
  print("Well done, this is right.")
  score = score + 1
else:
  print("Sorry, it is not right.")
print()
third_guess = input("And the third guess is? ")
if third_guess in recipe_ingredients and third_guess != second_guess and third_guess != first_guess:
  print("Well done, this is right.")
  score = score + 1
else:
 print("Sorry, it is not right.")
print()
print("We are at the end of the game.")
print()
print("You have got: " + str(score) + " points.")
time.sleep(3)
print()
print("The recipe ingredients are as following:")
print (recipe_ingredients)