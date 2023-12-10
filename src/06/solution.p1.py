import re


def read_puzzle():
    file = open("puzzle.txt", "r")
    times = re.findall(r'\d+', file.readline())
    distances = re.findall(r'\d+', file.readline())
    return times, distances


def main():
    time, distance = read_puzzle()


if __name__ == "__main__":
    main()
