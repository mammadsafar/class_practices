import random

number = random.randrange(1, 100)

# print(number)

guess = int(input("Enter any number: "))

while number!= guess:
    
    if guess < number:
        print("Too low! :)")
        guess = int(input("عدد وارد کن: "))
    elif guess > number:
        print("Too High! :)")
        guess = int(input("Enter any number: "))
    else:
        break

print('You guessed it right :D')