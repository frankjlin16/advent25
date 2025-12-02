sample = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

ans = 0
curr = 50

with open("01/input.txt") as f:
    for i in f:
        instr = i[0]
        num = int(i[1:])
        prev = curr
        # print(instr, num)

        if instr.__eq__("L"):
            diff = curr - num
            curr = (100 + curr - num) % 100
            if diff.__le__(0) and prev.__ne__(0):
                clicks = (abs(diff) + curr) / 100
                if diff.__eq__(0):
                    clicks += 1
                ans += clicks
                # print(ans)
        else:
            sum = curr + num
            curr = (curr + num) % 100
            if sum.__ge__(100) and prev.__ne__(0):
                clicks = (sum - curr) / 100
                ans += clicks
                # print(ans)

        # if curr.__eq__(0):
        #     ans += 1

        # print(curr)

print(f"ANS: {ans}")
