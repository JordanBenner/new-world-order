print("I am thinking of a number between 1 and 10")
secret_number = 5
while True:
    guess = int(input("whats the number?"))
    if guess == 5:
        print("Yes You Win!")
        break

    elif guess > 5:
        print("{} is too high.".format(guess))
    else:
        ("{} is too low.".format(guess))
