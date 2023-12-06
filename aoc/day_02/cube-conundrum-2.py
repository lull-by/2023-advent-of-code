from math import prod
RED, GREEN, BLUE = 0, 1, 2

str_to_color = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
}

color_to_str = {
    RED: "red",
    GREEN: "green",
    BLUE: "blue",
}

def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    sum_of_powers = 0
    for game_idx, line in enumerate(lines, start=1):
        print(f"{game_idx=}")
        _, game_str = line.split(": ")
        draw_strs = game_str.split("; ")
        min_color_counts = {
            RED: 0,
            GREEN: 0,
            BLUE: 0,
        }
        for draw_str in draw_strs:
            color_count_strs = draw_str.strip().split(", ")
            color_counts = {
                RED: 0,
                GREEN: 0,
                BLUE: 0,
            }
            for color_count_str in color_count_strs:
                color_count, color = color_count_str.split(" ")
                color_count = int(color_count)
                color = str_to_color[color]
                color_counts[color] += color_count
            
            for color in (RED, GREEN, BLUE):
                min_color_counts[color] = max(min_color_counts[color], color_counts[color])
        
        power = prod(min_color_counts.values())
        sum_of_powers += power
        print(f"\t{power=}")

    return sum_of_powers


if __name__ == "__main__":
    print(main())