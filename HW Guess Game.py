import random




    

# if guess == random_number:
#     print("Congrats you won!")
# else:
#     while guess != random_number:
                # guess == input("What is your next guess?  ")
                # guess == int(guess)
                # if guess == random_number:
                #     break
                # else:
                #     print("Congrats!")

# Get input from the suer
# while the user's gess != random number, continue asking for input, 10 times total
# if guess is correct,m display a message
# if guess is incorrect prompt again or end game if it is the 10th time



def start_game():
    random_number = random.randrange (0,100)

    print(random_number)

    guess = input("What is your guess?    ")

    guess == int(guess)
    for numbers in range(0, 10):
           check_guess(guess, random_number)
        
       
def check_guess(num1, num2):
        if num1 == num2:
            print("Congrats you won!")
        else:
            input("Try again: ")
       
start_game()
