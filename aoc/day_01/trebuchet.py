digit_strs= [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]
sorted_digit_strs = sorted(digit_strs, key=lambda pair: len(pair[0]))

def match_digit_str_start_idx(start_idx, s):
    for digit_str, digit_val in sorted_digit_strs:
        l = len(digit_str)

        potential_start_idx = start_idx
        potential_end_idx = start_idx + l

        if potential_end_idx > len(s):
            return -1

        potential_digit_str = s[potential_start_idx:potential_end_idx]

        if potential_digit_str == digit_str:
            return digit_val

    return -1

def match_digit_str_end_idx(end_idx, s):
    for digit_str, digit_val in sorted_digit_strs:
        l = len(digit_str)

        potential_start_idx = end_idx + 1 - l
        potential_end_idx = end_idx + 1

        if potential_start_idx < 0:
            return -1

        potential_digit_str = s[potential_start_idx:potential_end_idx]

        if potential_digit_str == digit_str:
            return digit_val

    return -1


def main():
    f = open("in.txt", "r")
    lines = f.readlines()
    acc = 0
    for line in lines:
        digit_1 = 0
        digit_2 = 0

        for i, c in enumerate(line):
            if c.isdigit():
                digit_1 = int(c)
                break
            
            matched_str_digit = match_digit_str_start_idx(i, line)
            if matched_str_digit != -1:
                digit_1 = matched_str_digit
                break

        for j, c in enumerate(reversed(line)):
            i = len(line) - 1 - j
            print(i, end=",")

            if c.isdigit():
                digit_2 = int(c)
                break

            matched_str_digit = match_digit_str_end_idx(i, line)
            if matched_str_digit != -1:
                digit_2 = matched_str_digit
                break
        print()
        
        val = digit_1 * 10 + digit_2
        print(val, "|", line)
        acc += val
    return acc

if __name__ == "__main__":
    print(main())