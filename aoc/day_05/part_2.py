from dataclasses import dataclass
import inspect
import re
from pprint import pprint

def dbv(var, tb=0):
    return
    # print a variable name var and its value
    # with tb num of tabs
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    tab_pfx = "".join('\t'*tb)
    print(f"{tab_pfx}{r}={var}")


def dbd(div_char="=", size=100):
    return
    div = "".join(div_char*size)
    print(div)

@dataclass
class SeedRange:
    start: int
    len: int

@dataclass
class ConvRange:
    dst: int
    src: int
    len: int

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
                seed_rgs.append(SeedRange(seeds[i], seeds[i+1]))
            dbv(seed_rgs, tb=1)
            
            continue
        
        if line.endswith(":"):
            print("new conversion")
            conversions.append([])
            conversion_idx += 1
            continue

        conversion_nums = [ int(m.group(0)) for m in re.finditer(r"\d+", line) ]
        dbv(conversion_nums, tb=1)

        conversion_parms = ConvRange(
            conversion_nums[0],
            conversion_nums[1],
            conversion_nums[2],
        )
        dbv(conversion_parms, tb=1)
        conversions[conversion_idx].append(conversion_parms)
    dbd()
    pprint(conversions)
    dbd()

    proc_rgs = seed_rgs
    for conv_idx, conv_rgs in enumerate(conversions):
        dbv(conv_idx, tb=1)
        output_rgs = []

        conv_rgs.sort(key=lambda rg: rg.src)
        proc_rgs.sort(key=lambda rg: rg.start)

        conv_rgs_idx = 0
        proc_rgs_idx = 0
        while True:
            if conv_rgs_idx > len(conv_rgs): break
            if proc_rgs_idx > len(proc_rgs): break

            conv_rg = conv_rgs[conv_rgs_idx]
            proc_rg = proc_rgs[proc_rgs_idx]

            # no overlap proc < conv
            if proc_rg.start + proc_rg.len < conv_rg.src:
                proc_rgs_idx += 1
                continue
            # no overlap proc > conv
            if proc_rg.start >= conv_rg.src + conv_rg.len:
                conv_rgs_idx += 1
                continue

            # get overlap
            overlap_start = max(proc_rg.start, conv_rg.src)
            overlap_end = min(proc_rg.start + proc_rg.len, conv_rg.src + conv_rg.len)
            overlap_len = overlap_end - overlap_start
            overlap_rg = SeedRange(overlap_start, overlap_len)
            output_rgs.append(overlap_rg)

        proc_rgs = output_rgs
        dbv(proc_rgs, tb=2)
    
    # extract min from rgs
    res = min(output_rgs, key=output_rgs.start)

    return res

if __name__ == "__main__":
    use_test_input = True
    res = main(use_test_input)
    print(res)