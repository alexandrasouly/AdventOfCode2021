def import_data():
    with open("inputs/day1.csv") as file:
        lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]
    return lines


def part_1():
    data = import_data()
    growing_mask = [(data[i] < data[i + 1]) for i in range(len(data) - 1)]
    return sum(growing_mask)


def part_2():
    data = import_data()
    growing_mask = [
        (data[i] + data[i + 1] + data[i + 2] < data[i + 1] + data[i + 2] + data[i + 3])
        for i in range(len(data) - 3)
    ]
    return sum(growing_mask)


if __name__ == "__main__":
    solution1 = part_1()
    print(solution1)
    solution2 = part_2()
    print(solution2)
