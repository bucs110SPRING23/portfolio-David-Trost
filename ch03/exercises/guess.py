import random 
random_number= random.randint(1,10)
for i in range(3):
    guess=int(input("Guess a number between 1 and 10:"))
    if guess< random_number:
        print("Too low")
    elif guess> random_number: 
        print("Too high")
    else:
        print("Correct!")
        break
else:
    print("Sorry, the number was {}. Better luck next time!".format(random_number))