import random 
random_number= random.randint(1,1000)
guess_count=0
for i in range(1000):
    guess=int(input("Guess a number between 1 and 1000:"))
    guess_count +=1
    if guess< random_number:
        print("Too low")
    elif guess> random_number: 
        print("Too high")
    else:
        print("Correct! You guessed the number in",guess_count,"times")
        break

    