from typing import List

SEGMENT_DICT_KEYS = ["top", "top_left", "top_right", "middle", "bottom_left", "bottom_right", "bottom"]

def import_data():
    with open("inputs/day8.csv") as file:
        lines = file.readlines()
    lines = [line.rstrip().split(" | ") for line in lines]
    patterns = [ patters.split(" ") for (patters,digits) in lines]
    patterns = [[''.join(sorted(pattern)) for pattern in pattern_line] for pattern_line in patterns]
    digits = [ digits.split(" ") for (patters,digits) in lines]
    digits = [[''.join(sorted(digit)) for digit in digit_line] for digit_line in digits]
    return digits,patterns

    
def part1():
    digits,patterns=import_data()
    counter = 0
    for line in digits:
        for digit in line:
            if len(digit) in [2,3,4,7]:
                counter += 1
    return counter

def find_nums(number_dict, pattern_line):
    print(pattern_line)
    for pattern in pattern_line:
        if len(pattern) == 2:
            number_dict[1] = pattern
            pattern_line.remove(pattern)
            print(number_dict[1])
        elif len(pattern) == 3:
            number_dict[7] = pattern
            pattern_line.remove(pattern)
        elif len(pattern) == 4:
            number_dict[4] = pattern
            pattern_line.remove(pattern)
        elif len(pattern) == 7:
            number_dict[8] = pattern
            pattern_line.remove(pattern)
    print(number_dict)
    print(pattern_line)
    for pattern in pattern_line:
        print(number_dict[1])
        if len(pattern)==6 and not all([(num in pattern) for num in number_dict[1]]):
            number_dict[6] = pattern
            pattern_line.remove(pattern)
            break
    print(pattern_line)

    for pattern in pattern_line:
        if len(pattern)==5 and all([(pattern_num in number_dict[6]) for pattern_num in pattern]):
            number_dict[5] = pattern
            pattern_line.remove(pattern)
            break
    print(pattern_line)

    for pattern in pattern_line:
        if len(pattern)==5 and sum([(pattern_num in number_dict[5]) for pattern_num in pattern])==3:
            number_dict[2] = pattern
            pattern_line.remove(pattern)
            break
    print(pattern_line)

    for pattern in pattern_line:
        if len(pattern)==5 and sum([(pattern_num in number_dict[5]) for pattern_num in pattern])==4:
            number_dict[3] = pattern
            pattern_line.remove(pattern)
            break
    print(pattern_line)

    for pattern in pattern_line:
        if len(pattern)==6 and sum([(pattern_num in number_dict[3]) for pattern_num in pattern])==4:
            number_dict[0] = pattern
            pattern_line.remove(pattern)
            break
    print(pattern_line)

    for pattern in pattern_line:
        if len(pattern)==6 and sum([(pattern_num in number_dict[3]) for pattern_num in pattern])==5:
            number_dict[9] = pattern
            pattern_line.remove(pattern)
            break
    return number_dict


def determine_number(digit_line:List[str], pattern_line:List[str]):
    number_dict = {num:None for num in range(0,10)}
    number_dict = find_nums(number_dict, pattern_line)
    print("This is number dict")
    print(number_dict)
    pattern_dict = {v: k for k, v in number_dict.items()}
    print("This is pattern dict")
    print(pattern_dict)
    print(digit_line)
    number = int(''.join([str(pattern_dict[digit]) for digit in digit_line]))
    print(number)
    return number


def part2():
    sum_of_input = 0
    digits,patterns=import_data()
    for digit_line, pattern_line in zip(digits, patterns):
        number = determine_number(digit_line, pattern_line)
        sum_of_input += number
    return sum_of_input
if __name__ == "__main__":
   counter =part1()
   print(counter)
   sum_of_input = part2()