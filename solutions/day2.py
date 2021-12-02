def import_data():
    with open("inputs/day2.csv") as file:
        lines = file.readlines()
    data = [tuple(line.rstrip().split(" ")) for line in lines]
    return data


class Submarine:
    def __init__(self, data):
        self.data = data
        self.forward = 0
        self.depth = 0
        self._process_data()

        self.aim_part2 = 0
        self.depth_part2 = 0
        self._calculate_aim()

    def _process_data(self):
        for element in self.data:
            if element[0] == "forward":
                self.forward += int(element[1])
            elif element[0] == "up":
                self.depth -= int(element[1])
            elif element[0] == "down":
                self.depth += int(element[1])

    def _calculate_aim(self):
        for element in self.data:
            if element[0] == "forward":
                self.depth_part2 += self.aim_part2 * int(element[1])
            elif element[0] == "up":
                self.aim_part2 -= int(element[1])
            elif element[0] == "down":
                self.aim_part2 += int(element[1])


def part_1():
    data = import_data()
    submarine = Submarine(data=data)
    return submarine.forward * submarine.depth


def part_2():
    data = import_data()
    submarine = Submarine(data=data)
    return submarine.depth_part2 * submarine.forward


if __name__ == "__main__":
    solution1 = part_1()
    print(solution1)
    solution2 = part_2()
    print(solution2)
