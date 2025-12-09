banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def find_largest_joltage(bank):
    j1 = 0
    j2 = 0
    # Find the first highest, then the second highest
    for i in range(len(bank)):
        joltage = int(bank[i])
        if joltage > j1:
            if i != len(bank) - 1:
                j1 = joltage
                j2 = 0
            else:
                j2 = joltage
            if i == len(bank) - 2:
                j2 = int(bank[-1])
                break
        else:
            if joltage > j2:
                j2 = joltage

    return j1 * 10 + j2


def main():
    sum = 0
    with open("03/input.txt") as banks:
        for bank in banks:
            joltage = find_largest_joltage(bank.rstrip())
            sum += joltage

    print(sum)


if __name__ == "__main__":
    main()
