import random

print("LET'S PLAY A GUESSING GAME!")
print("I'm thinking of a number from 1 to 100")
print("If you've guessed it correctly you win")
print("You only have 10 guesses, Goodluck!")

#The function that creates a range from 1 - 100 
num = random.randint(1,100) 
for n in range(10):
    guess = int(input("Enter any number from 1-100: "))
    if guess > num:
        print("Your Guess is Too High")
    elif guess < num:
        print("Your Guess is Too Low")
    elif guess == num:
       print("Congratulations, You Guessed it Right!")
       print("Total Number of Guesses:", n+1)
       quit()
print("Oh no! You ran out of guesses, The number was", num)
    
    
        

