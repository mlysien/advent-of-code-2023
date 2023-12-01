def open_puzzle():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


puzzle = open_puzzle()
calibration_values = 0

for line in puzzle:
    first_digit = last_digit = 0
    for c in line:
        if c.isdigit():
            first_digit = int(c)
            break

    for c in line[::-1]:
        if c.isdigit():
            last_digit = int(c)
            break

    calibration_values += int(f'{first_digit}{last_digit}')

print(f'Sum of all of the calibration values is {calibration_values}')

