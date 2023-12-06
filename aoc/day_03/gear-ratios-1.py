import re

def main():
    f = open("input.txt", "r")
    #f = open("test.txt", "r")
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
            next_syms = {i: c for i, c in enumerate(line) if not c.isdigit() and c != "."}

        print(f"\t{prev_nums=}")
        print(f"\t{prev_syms=}")
        print()
        print(f"\t{cur_nums=}")
        print(f"\t{cur_syms=}")
        print()
        print(f"\t{next_nums=}")
        print(f"\t{next_syms=}")

        print("\t==============================================================")
        def is_adj(rg, syms):
            start, end = rg
            for idx in syms.keys():
                if start - 1 <= idx < end + 1:
                    return True
            return False
        if cur_nums is not None:
            for rg, num in cur_nums.items():
                if (
                    (prev_syms is not None and is_adj(rg, prev_syms)) or
                    is_adj(rg, cur_syms) or
                    (next_syms is not None and is_adj(rg, next_syms))
                ):
                    print(f"\t{num=}")
                    res += num
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