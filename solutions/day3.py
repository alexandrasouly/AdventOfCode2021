def import_data():
    with open("inputs/day3.csv") as file:
        lines = file.readlines()
    data = [tuple(line.rstrip()) for line in lines]
    return data


def invert_data(data):
    # COLLECTS THE NUMBERS BY BIT POSITION, EG FIRST ELEMENT THE FIRST BITS IN ORDER
    inverted_data = [
        [data[i][place] for i in range(len(data))] for place in range(len(data[0]))
    ]
    return inverted_data


def part_1():
    data = import_data()
    inverted_data = invert_data(data)
    gamma_list = [
        max(set(inverted_data[i]), key=inverted_data[i].count)
        for i in range(len(inverted_data))
    ]
    gamma = int("".join(gamma_list), 2)
    epsilon_list = [
        min(set(inverted_data[i]), key=inverted_data[i].count)
        for i in range(len(inverted_data))
    ]
    epsilon = int("".join(epsilon_list), 2)

    return epsilon * gamma


def part_2():
    data = import_data()
    inverted_data = invert_data(data)
    oxygen_list = data.copy()
    co2_list = data.copy()

    # DEALING WITH OXYGEN
    for considered_bit in range(len(data[0])):
        if len(oxygen_list) == 1:
            break
        inverted_data = invert_data(oxygen_list)
        oxy_count1 = inverted_data[considered_bit].count("1")
        oxy_count0 = inverted_data[considered_bit].count("0")
        oxy_copy = oxygen_list.copy()
        if oxy_count0 == oxy_count1:
            for element in oxy_copy:
                if element[considered_bit] == "0":
                    oxygen_list.remove(element)
        else:
            for element in oxy_copy:
                if element[considered_bit] == ("0" if oxy_count0 < oxy_count1 else "1"):
                    oxygen_list.remove(element)

    # DEALING WITH CO2
    for considered_bit in range(len(data[0])):
        if len(co2_list) == 1:
            break
        inverted_data = invert_data(co2_list)
        co2_count0 = inverted_data[considered_bit].count("0")
        co2_count1 = inverted_data[considered_bit].count("1")
        co2_copy = co2_list.copy()

        if co2_count0 == co2_count1:
            for element in co2_copy:

                if element[considered_bit] == "1":
                    co2_list.remove(element)
        else:
            for element in co2_copy:
                if element[considered_bit] == ("0" if co2_count0 > co2_count1 else "1"):
                    co2_list.remove(element)

    oxygen = int("".join(oxygen_list[0]), 2)
    co2 = int("".join(co2_list[0]), 2)

    return oxygen * co2


if __name__ == "__main__":
    solution1 = part_1()
    print(solution1)
    solution2 = part_2()
    print(solution2)
