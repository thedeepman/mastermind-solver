import copy

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


def check_if_valid(result:Result, perm):
    if result.reds != get_number_of_position_matches(result.permutation, perm):
        print("reds didn't match")
        return False
    elif result.whites != (get_number_of_color_matches(result.permutation, perm)-result.reds):
        print("whites didn't match")
        return False
    return True