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

target_color_counts = {
    RED: 12,
    GREEN: 13,
    BLUE: 14,
}

def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    feasible_game_idx_sum = 0
    for game_idx, line in enumerate(lines, start=1):
        print(f"{game_idx=}")
        _, game_str = line.split(": ")
        draw_strs = game_str.split("; ")
        is_target_count_possible = True
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
            
            for color_count, target_color_count in zip(color_counts.values(), target_color_counts.values()):
                if color_count > target_color_count:
                    break
            if color_count > target_color_count:
                is_target_count_possible = False
                break
            print(f"\t{color_count=} {color_to_str[color]=}")

        if is_target_count_possible:
            feasible_game_idx_sum += game_idx
            print("\tinvalid!")
        else:
            print("\tvalid!")
    return feasible_game_idx_sum


if __name__ == "__main__":
    print(main())