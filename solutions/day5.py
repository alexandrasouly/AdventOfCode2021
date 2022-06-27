"""
Solution to day 05 with no imports
"""


def interpret_line(line: str):
    items = line.rstrip().replace(" -> ", ",").split(",")
    return [int(x) for x in items]


def filter_straight_lines(line_list):
    # x1,y1 -> x2,y2 --> (x1, y1, x2, y2)
    # filter straight lines, ie. where either x1 = x2 or y1 = y2.

    for array in line_list:
        if array[0] == array[2] or array[1] == array[3]:
            yield array


def read_all_data():
    with open("inputs/day5.csv", mode="r") as file:
        return file.readlines()


def allocate_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([0] * size)

    return matrix


def part1_fill_map(array, lines, diagonal=False):
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                array[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                array[x][y1] += 1
        else:
            if diagonal:
                x_sign = 1 if (x1 - x2) < 0 else -1
                y_sign = 1 if (y1 - y2) < 0 else -1

                for i in range(abs(x1 - x2) + 1):
                    array[x1 + i * x_sign][y1 + i * y_sign] += 1


def count_gte(array, value=2):
    count = 0
    for sub_arr in array:
        for x in sub_arr:
            if x >= value:
                count += 1

    return count


def part1():
    # read data
    lines = read_all_data()
    line_list = [interpret_line(x) for x in lines]
    straight_lines = list(filter_straight_lines(line_list))

    # find size of map
    size = max([max(x) for x in straight_lines])
    map_matrix = allocate_matrix(size + 1)

    # fill in the map
    part1_fill_map(map_matrix, straight_lines)

    print("part1:", count_gte(map_matrix, 2))


def part2():
    # read data
    lines = read_all_data()
    line_list = [interpret_line(x) for x in lines]

    # find size of map
    size = max([max(x) for x in line_list])
    map_matrix = allocate_matrix(size + 1)

    # fill in the map
    part1_fill_map(map_matrix, line_list, diagonal=True)

    print("part2:", count_gte(map_matrix, 2))


if __name__ == "__main__":
    part1()
    part2()