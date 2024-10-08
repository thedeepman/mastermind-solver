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


my_possibilities = []
generate_all_possibilities(True,3, 3, my_possibilities)
# generate_all_possibilities(3,2, my_possibilities)
print(my_possibilities)
