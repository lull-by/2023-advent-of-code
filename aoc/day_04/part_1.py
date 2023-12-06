import inspect
import re

def dbv(var, tb=0):
    # print a variable name var and its value
    # with tb num of tabs
    frame = inspect.currentframe().f_back
    s = inspect.getframeinfo(frame).code_context[0]
    r = re.search(r"\((.*)\)", s).group(1)
    tab_pfx = "".join('\t'*tb)
    print(f"{tab_pfx}{r} = {var}")


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
    for i, line in enumerate(lines):
        print(i)
        _, nums_str = line.split(":")
        win_nums_str, my_nums_str = nums_str.split("|")

        win_nums =  { int(m.group()) for m in re.finditer(r"\d+", win_nums_str) }
        my_nums = [ int(m.group()) for m in re.finditer(r"\d+", my_nums_str) ]

        dbv(win_nums, tb=1)
        dbv(my_nums, tb=1)

        score = 0
        for my_num in my_nums:
            if my_num in win_nums:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        res += score


    return res

if __name__ == "__main__":
    use_test_input = False
    res = main(use_test_input)
    print(res)