import random
import math

lower=int(input("Enter your lower bound: "))
upper=int(input("Enter your upper bound: "))

random_number=random.randint(lower, upper)

count=0

print("~You have only 5 chances to guess the number.~")
i=5
while count<5:
    count+=1
    i-=1
    guess = int(input("Guess a number: "))
    if random_number==guess:
        print("Congratulations! You guessing correnct number!")
        break
    elif random_number>guess:
        print("You guessed too small! Try again!(Guess Changes:",i,")")
    elif random_number<guess:
        print("You guessed too high! Try again!(Guess Changes:",i,")")

if count==5:
    print("\nThe number was %d" %random_number)
