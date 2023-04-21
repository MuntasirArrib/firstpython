import random

# def printingpress(x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"guess a number between 1 and {x}: "))
#         if guess > random_number:
#             print("Too high, guess again: ")
#         elif guess < random_number:
#             print("Too low, guess again: ")
#     print("You did it")

# printingpress(10)


# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ""

#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low,high)
#         else:
#             guess = low # could also be high b/c low = high

#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
#         if feedback == 'h':
#             high = guess - 1
#         if feedback == 'l':
#             low = guess + 1
        
#         print('Yay! The computer guessed your number, {guess}, correctly!')

# computer_guess(10)

def machine_guess(x):
    low = 1
    high = x
    GuessingNumber = random.randint(low, high)
    print(f'Player 1 number is {GuessingNumber}')
    guess = 0

    while guess != GuessingNumber:
        if low != high:
            guess = random.randint(low,high)
            print(f'Player 2 guessed {guess}')
        else: 
            guess = high  
        if guess > GuessingNumber:
            high = guess - 1
            print(f"Too high, player2, now guess a number between {high} and {low}")
        elif guess < GuessingNumber:
            low = guess + 1
            print(f"too low, player2, now guess a number between {high} and {low}")
    print("Yay the game is over!")

        
machine_guess(10)
        


