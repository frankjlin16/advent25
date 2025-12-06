sample = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
    "824824821-824824827,2121212118-2121212124"
)
input = (
    "492410748-492568208,246-390,49-90,16-33,142410-276301,54304-107961,"
    "12792-24543,3434259704-3434457648,848156-886303,152-223,1303-1870,"
    "8400386-8519049,89742532-89811632,535853-567216,6608885-6724046,"
    "1985013826-1985207678,585591-731454,1-13,12067202-12233567,6533-10235,"
    "6259999-6321337,908315-972306,831-1296,406-824,769293-785465,3862-5652,"
    "26439-45395,95-136,747698990-747770821,984992-1022864,34-47,"
    "360832-469125,277865-333851,2281-3344,2841977-2953689,29330524-29523460"
)
ans = 0


def is_odd(num):
    """Check if number is odd.

    Args:
        num (int): input number.

    Returns:
        boolean: returns True if `num` is odd, False if even.
    """
    if num % 2 == 0:
        return False

    return True


def add_to_answer(num: int):
    global ans
    ans += num


def find_invalid_id(first, last):
    # If the length of first and last ID are odd, there are no
    # solutions in range; therefore, returns
    if is_odd(len(first)) and is_odd(len(last)):
        print("None")  # NOTE: For DEBUG only
        return
    elif is_odd(len(first)):
        print("First is odd")  # NOTE: DEBUG
        # TODO: Implement
        pass
    elif is_odd(len(last)):
        print("Last is odd")  # NOTE: DEBUG
        # TODO: Implement
        pass
    else:
        half_len = int(len(first) / 2)
        lhalf_first = int(first[:half_len])
        rhalf_first = int(first[half_len:])
        lhalf_last = int(last[:half_len])
        rhalf_last = int(last[half_len:])

        # If left half of first ID is greater than right half of
        # last ID, there are no solutions in range.
        if lhalf_first > rhalf_last:
            return

        # If right half of first ID is greater than left half of
        # last ID, there are no solutions in range.
        if rhalf_first > lhalf_last:
            return

        start: int = rhalf_first if rhalf_first > lhalf_first else lhalf_first
        end: int = rhalf_last

        print("Good range")
        print(lhalf_first, rhalf_first, lhalf_last, rhalf_last)
        print(start, end)


def gift_shop(input):
    ranges = input.split(",")

    for i in ranges:
        firstID = i.split("-")[0]
        lastID = i.split("-")[1]
        print("______________________")
        print("Ranges:", firstID, lastID)  # NOTE: For DEBUG only
        find_invalid_id(firstID, lastID)


gift_shop(sample)
print("\n\n##################\nAnswer:", ans)
