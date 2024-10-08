import copy, random
from logging import exception

from Result import Result


def get_number_of_position_matches(result, possible_option):
    matches = 0
    for i in range(len(result)):
        if result[i] == possible_option[i]:
            matches += 1
    return matches


def get_number_of_color_matches(result, possible_option):
    colors_left = copy.deepcopy(possible_option)
    for color_r in result:
        for color_o in colors_left:
            if color_r == color_o:
                colors_left.remove(color_o)
                break
    return len(result) - len(colors_left)


def check_if_valid(result: Result, perm):
    if result.reds != get_number_of_position_matches(result.permutation, perm):
        print("reds didn't match")
        return False
    elif result.whites != (get_number_of_color_matches(result.permutation, perm) - result.reds):
        print("whites didn't match")
        return False
    return True


def generate_all_possibilities(repeats: bool, possible_colors: int, slots: int, possibilities=None, current_slot=0,
                               current_possibility=None):
    if current_possibility is None:
        current_possibility = []
    if possibilities is None:
        possibilities = []
    if current_slot < slots:
        current_slot += 1
        for i in range(possible_colors):
            this_possibility = copy.deepcopy(current_possibility)
            should_add = True
            if not repeats:
                for j in this_possibility:
                    if j == i:
                        should_add = False
                        break
            if should_add:
                this_possibility.append(i)
                generate_all_possibilities(repeats, possible_colors, slots, possibilities, current_slot, this_possibility)
    else:
        possibilities.append(current_possibility)

def get_result(answer, guess):
    if answer == guess:
        return Result(guess, len(guess), 0)
    reds = get_number_of_position_matches(answer, guess)
    return Result(guess, reds, get_number_of_color_matches(answer, guess) - reds)


def play_game(repeats: bool, possible_colors: int, slots: int, answer):
    if len(answer) != slots:
        exception("Answer does not match number of slots")
    possibilities = []
    generate_all_possibilities(repeats, possible_colors, slots, possibilities)
    guess = 0
    match = False
    while not match:
        guess_index = random.randint(0,len(possibilities)-1)
        guess += 1
        if possibilities[guess_index] == answer:
            print("Found a match in " + str(guess) + " guesses!")
            print(len(possibilities))
            match = True
        else:
            possibilities.pop(guess_index)


play_game(False, 6, 4, [2,3,1,0])
