import inspect
import re
from pprint import pprint

def dbv(var, tb=0):
    # print a variable name var and its value
    # with tb num of tabs
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    tab_pfx = "".join('\t'*tb)
    print(f"{tab_pfx}{r}={var}")


def dbd(div_char="=", size=100):
    div = "".join(div_char*size)
    print(div)

def main(use_test_input=True):
    if use_test_input:
        f = open("test.txt", "r")
    else:
        f = open("input.txt", "r")

    res = 0
    lines = f.readlines()
    seed_rgs = [] # (start, len)
    conversions = []
    conversion_idx = -1
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        print(f"line: {i}")
        print(f"{line=}")

        if not seed_rgs:
            seeds = [ int(m.group(0)) for m in re.finditer(r"\d+", line) ]
            for i in range(0, len(seeds), 2):
                seed_rgs.append((seeds[i], seeds[i+1]))
            dbv(seed_rgs, tb=1)
            
            continue
        
        if line.endswith(":"):
            print("new conversion")
            conversions.append([])
            conversion_idx += 1
            continue

        conversion_nums = [ int(m.group(0)) for m in re.finditer(r"\d+", line) ]
        dbv(conversion_nums, tb=1)

        conversion_parms = {}
        conversion_parms["DST"] = conversion_nums[0]
        conversion_parms["SRC"] = conversion_nums[1]
        conversion_parms["RG"] = conversion_nums[2]
        dbv(conversion_parms, tb=1)
        conversions[conversion_idx].append(conversion_parms)
    dbd()
    pprint(conversions)
    dbd()

    seed_loc_nums = []
    for seed in seeds:
        dbd()
        dbv(seed)
        processed_val = seed
        for conv_idx, conversion in enumerate(conversions):
            dbv(conv_idx, tb=1)
            for conversion_parms in conversion:
                dst = conversion_parms["DST"]
                src = conversion_parms["SRC"]
                rg_len = conversion_parms["RG"]
                if src <= processed_val < src + rg_len:
                    dbv(conversion_parms, tb=2)
                    diff = processed_val - src
                    processed_val = dst + diff
                    break
            dbv(processed_val, tb=2)

        seed_loc_nums.append(processed_val)

    res = min(seed_loc_nums)
    return res

if __name__ == "__main__":
    use_test_input = False
    res = main(use_test_input)
    print(res)