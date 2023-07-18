import random

answer = random.randint(0, 10)


def tryfornumber():  # gets input from user and prompts user to enter an integer if incorrect data type input
    val = None
    while val is None:
        try:
            val = int(input("Please enter a number between 1 and 10: "))
            return val
        except ValueError:
            print("I'm sorry, that wasn't a number.")


def retry():  # counts up tries taken counts down tries remaining and calls function to get input from user
    global triesRemaining
    global triesTaken
    global guess
    triesRemaining -= 1
    triesTaken += 1
    guess = tryfornumber()


triesRemaining = 2
triesTaken = 0

guess = tryfornumber()

while triesRemaining >= 0:
    if guess < answer:
        print(f"Your guess was too low. You have {triesRemaining} tries left! Please guess again: ")
        retry()
    elif guess > answer:
        print(f"Your guess was too high. You have {triesRemaining} tries left! Please guess again: ")
        retry()
    elif guess == answer and triesTaken == 0:
        triesTaken += 1
        print(f"You got it in {triesTaken} try! The number was {answer}!")
        break
    elif guess == answer and triesTaken > 1:
        print(f"You got it in {triesTaken + 1} tries! The number was {answer}!")
        break
    else:
        print(f"I'm sorry, you ran out of tries. The correct number was {answer}.")
        break
