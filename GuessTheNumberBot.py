import random
import math

def int_input(text):
    while True:
        entry = input(text)
        try:
            entry = int(entry)
            return entry
        except ValueError:
            print("The entry contains an invalid character.")


def int_input_in_range(text, minimum_limit, maximum_limit):
    while True:
        entry = int_input(text)
        if minimum_limit <= entry <= maximum_limit:
            return entry
        else:
            print("The entry is not between {} and {}.".format(minimum, maximum))


def define_range():
    while True:
        min = int_input("What limit is the minimum :")
        max = int_input("What limit is the maximum :")
        if min < max:
            return min, max
        else:
            print("The maximum has to be greater than the minimum.")


def human_chooses_mystery_number():
    number = int_input_in_range("Choose the mystery number between {} and {} :".format(minimum, maximum), minimum,
                                maximum)
    return number


def bot_chooses_mystery_number():
    number = random.randint(minimum, maximum)
    print("ROBOT has chosen the mystery number.")
    return number


def human_plays_a_turn():
    global number, turn_count, victory, maximum, minimum
    while not victory:
        guess = int_input_in_range("Guess the mystery number between {} and {} :".format(minimum, maximum), minimum,
                                   maximum)
        win_check(guess)


def bot_plays_a_turn():
    global number, turn_count, victory, maximum, minimum
    while not victory:
        guess = math.ceil((minimum+maximum)/2)
        print('ROBOT : "Is the mystery number {}?"'.format(guess))
        win_check(guess)


def superbot_plays_a_turn():
    global number, turn_count, victory, maximum, minimum
    while True:
        guess = number
        print('SUPERBOT : "Is the mystery number {}?"'.format(guess))
        win_check(guess)
        if victory:
            print('SUPERBOT : "I can read your mind like an open book."')
            break


def win_check(guess):
    global number, turn_count, victory, maximum, minimum
    if number < guess:
        print("Too high.")
        turn_count += 1
        maximum = guess-1
    elif guess < number:
        print("Too low.")
        turn_count += 1
        minimum = guess+1
    elif guess == number and turn_count == 0:
        turn_count += 1
        print("Won in {} turn!!!".format(turn_count))
        victory = True
    else:
        turn_count += 1
        print("Won in {} turns!".format(turn_count))
        victory = True


# To make the player chose a number and the bot guess it
def human_vs_bot():
    global victory, turn_count, minimum, maximum, number
    victory = False
    turn_count = 0
    minimum, maximum = define_range()
    number = human_chooses_mystery_number()
    bot_plays_a_turn()


# To make the bot chose a number and the player guess it
def bot_vs_human():
    global victory, turn_count, minimum, maximum, number
    victory = False
    turn_count = 0
    minimum, maximum = define_range()
    number = bot_chooses_mystery_number()
    human_plays_a_turn()


# To make the bot play against itself
def bot_vs_bot():
    global victory, turn_count, minimum, maximum, number
    victory = False
    turn_count = 0
    minimum, maximum = 0, 1000000000
    print("ROBOT will chose a mystery number between {} and {}...".format(minimum, maximum))
    number = bot_chooses_mystery_number()
    bot_plays_a_turn()


# To make two players play together
def human_vs_human():
    global victory, turn_count, minimum, maximum, number
    victory = False
    turn_count = 0
    print("\nPlayer 1, it's your turn !\n")
    minimum, maximum = define_range()
    number = human_chooses_mystery_number()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2, it's your turn !\n")
    human_plays_a_turn()


def human_vs_superbot():
    global victory, turn_count, minimum, maximum, number
    victory = False
    turn_count = 0
    minimum, maximum = define_range()
    number = human_chooses_mystery_number()
    superbot_plays_a_turn()


"Chose one of these game modes"

# bot_vs_human()        # Bot picks the number, human guesses it
# human_vs_bot()        # Human picks the number, bot guesses it
# bot_vs_bot()          # Bot plays against itself
# human_vs_human()      # Two players play against each other
# human_vs_superbot()   # SUPERBOT is the World Champion in number guessing!

bot_vs_human()


