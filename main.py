
import random
import copy
import argparse


def generate(length, capital=False,  letters=False, numbers=False, symbols=False):
    if length < 1 or not (capital or letters or numbers or symbols):
        raise AssertionError(
            "Unable to generete password, specified length too short or no character sets chosen")
    password = ""

    cap = [(65, 90)]
    smal = [(97, 122)]
    num = [(48, 57)]
    sym = [(33, 47), (58, 64), (91, 96), (123, 126)]

    character_list = {"cap": (capital, cap), "smal": (
        letters, smal), "num": (numbers, num), "sym": (symbols, sym)}
    allowed_list = {}

    for key, value in character_list.items():
        is_allowed, interval_list = value
        if is_allowed:
            allowed_list[key] = interval_list

    obligatory_list = allowed_list.copy()
    for i in range(length):
        if bool(obligatory_list):
            key = random.SystemRandom().choice(list(obligatory_list.keys()))
            low_index, top_index = random.SystemRandom().choice(
                obligatory_list[key])
            obligatory_list.pop(key)
        else:
            key = random.SystemRandom().choice(list(allowed_list.keys()))
            low_index, top_index = random.SystemRandom().choice(
                allowed_list[key])

        password += chr(random.SystemRandom().randint(low_index, top_index))

    str_temp = list(password)
    random.shuffle(str_temp)
    password = ''.join(str_temp)
    return password

    # Capital letters: 65-90
    # Small letters: 97-122
    # Numbers: 48-57
    # Symbols: 33-47, 58-64, 91-96, 123-126


def check_strength(string):
    string = string.strip()
    categories = [0, 0, 0, 0]

    for i in range(len(string)):
        letter = ord(string[i])
        if 65 <= letter <= 90:  # Capital letters
            categories[0] = 1
        if 97 <= letter <= 122:  # Small letters
            categories[1] = 1
        if 48 <= letter <= 57:  # Numbers
            categories[2] = 1
        if 33 <= letter <= 47 or 58 <= letter <= 64 or 91 <= letter <= 96 or 123 <= letter <= 126:  # Symbols
            categories[3] = 1

    strength = len(string) * categories.count(1)
    # print(strength, len(string), categories.count(1))
    if strength > 32:
        return "Very strong"
    if strength >= 24:
        return "Strong"
    if strength > 16:
        return "Moderate"
    return "Weak"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', help="Specifies the length of the generated password",
                        default=15, choices=range(8, 50), type=int)
    parser.add_argument('--capital', help="Password contains capital letters",
                        default=False, choices=[1, 0], type=bool)
    parser.add_argument('--small', help="Password contains small letters",
                        default=False, choices=[1, 0], type=bool)
    parser.add_argument('--numbers', help="Password contains numbers",
                        default=False, choices=[1, 0], type=bool)
    parser.add_argument('--symbols', help="Password contains special symbols",
                        default=False, choices=[1, 0], type=bool)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = vars(parse_arguments())
    password = generate(args["length"], args["capital"],
                        args["small"], args["numbers"], args["symbols"])
    print(password)
    
