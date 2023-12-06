import re

def main():
    #f = open("input.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()
    res = 0
    prev_syms = None
    cur_syms = None
    next_syms = None

    prev_nums = None
    cur_nums = None
    next_nums = None
    n = len(lines)
    for i in range(n+1):
        print(i)
        if i < n:
            line = lines[i].strip()
            print(line)
            next_nums = {(m.start(), m.end()): int(m.group()) for m in re.finditer(r'\d+', line)}
            next_syms = {i: c for i, c in enumerate(line) if c == "*"}

        print(f"\t{prev_nums=}")
        print(f"\t{prev_syms=}")
        print()
        print(f"\t{cur_nums=}")
        print(f"\t{cur_syms=}")
        print()
        print(f"\t{next_nums=}")
        print(f"\t{next_syms=}")

        print("\t==============================================================")
        def get_gear_ratio(gear_idx, rg_to_num_list):
            ratios = []
            for rg_to_num in rg_to_num_list:
                for rg, num in rg_to_num.items():
                    start, end = rg
                    if start - 1 <= gear_idx < end + 1:
                        ratios.append(num)
                        if len(ratios) == 2: return ratios[0] * ratios[1]
            return None
        if cur_syms is not None:
            for gear_idx, _ in cur_syms.items():
                rg_to_num_list = []
                if prev_nums: rg_to_num_list.append(prev_nums)
                if cur_nums: rg_to_num_list.append(cur_nums)
                if next_nums: rg_to_num_list.append(next_nums)
                ratio = get_gear_ratio(gear_idx, rg_to_num_list)
                if ratio is not None:
                    print(f"\t{gear_idx=}")
                    res += ratio
        print("\t==============================================================")

        prev_nums = cur_nums
        cur_nums = next_nums
        next_nums = None

        prev_syms = cur_syms
        cur_syms = next_syms
        next_syms = None

    return res


if __name__ == "__main__":
    print(main())