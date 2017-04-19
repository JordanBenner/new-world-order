import random
my_random_number = random.randint(1,10)
print("whats my random number between 1 and 10?")
while True:
    guess = int(input("whats the number?"))
    if guess == my_random_number:
        print("Yes You Win!")
        break

    elif guess > my_random_number:
        print("{} is too high.".format(guess))
    else:
        print("{} is too low.".format(guess))
