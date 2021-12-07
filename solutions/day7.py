from math import floor, ceil
def import_data():
    with open("inputs/day7.csv") as file:
        data = file.read()
    data = [int(num) for num in data.rstrip().split(",")]
    return data

def part1():
    data = sorted(import_data())
    median = data[int((len(data))/2)]
    fuel = sum([abs(num-median) for num in data ])
    return fuel

def part2():
    data = sorted(import_data())
    mean = sum(data)/len(data)
    fuel = min(sum([abs(num-m)*(abs(num-m)+1)/2 for num in data ]) for m in [int(floor(mean)), int(ceil(mean))])
    return int(fuel)


if __name__ == "__main__":

    fuel = part1()
    print(fuel)
    fuel = part2()
    print(fuel)
