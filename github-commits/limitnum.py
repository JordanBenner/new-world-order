import random
my_random_number = random.randint(1,10)
print("I am thinking of a number between 1 and 10.")
print("you have 5 guess left.")
guess_count = 0
while guess_count <5:
    guess = int(input("What is the number?"))
    if guess == my_random_number:
      print("Yes you win!")
      break

    elif guess > my_random_number:
      guess_count +=1
      print("{} is too high".format(guess))
      print("you have {} guess left.".format(guess))
    else:
      guess += 1
      print("{} is too low.".format(guess))
      print("you have {} guess left.".format(guess))

print("you ran out of guesses!")
