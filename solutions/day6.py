from typing import Dict


def import_data():
    with open("inputs/day6.csv") as file:
        data = file.read()
    data = [int(num) for num in data.rstrip().split(",")]
    return data

def convert_to_dict(data: list):
    keys = set(data)
    dict_of_ages = {key:data.count(key) for key in keys }
    return dict_of_ages

def change_timers(dict_of_ages: Dict):
    new_dict = {}
    for key, value in dict_of_ages.items():
        new_dict[key-1] = value
    if -1 in new_dict.keys():
        if 6 in new_dict.keys():
            new_dict[6] += new_dict[-1]
        else:
             new_dict[6] = new_dict[-1]
        new_dict[8] =  new_dict[-1]
        new_dict.pop(-1)
    return new_dict

def count_fish(dict_of_ages: Dict):
    return sum(dict_of_ages.values())

def part_1():
    data = import_data()
    dict_of_ages = convert_to_dict(data)
    for _ in range(0,80):
        dict_of_ages = change_timers(dict_of_ages)
    return count_fish(dict_of_ages)
def part_2():
    data = import_data()
    dict_of_ages = convert_to_dict(data)
    for _ in range(0,256):
        dict_of_ages = change_timers(dict_of_ages)
    return count_fish(dict_of_ages)

if __name__ == "__main__":
    fish1 = part_1()
    print(fish1)
    fish2 = part_2()
    print(fish2)