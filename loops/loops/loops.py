secret = 64 
guess = int(input("Enter a number 1-100: "))

while guess != secret:
    if guess > secret:
        print("too high")
    else:
        print("too low")
    guess = int(input("Enter a number 1-100: "))

print(" congrats " + str(count) + " guesses")

