import utils
from typing import List, Tuple
import pandas as pd


def get_values(instructions: List) -> Tuple:
    df = pd.DataFrame(instructions, columns=["Direction"])
    df_split = df["Direction"].str.split(" ", n=1, expand=True)
    df_split[1] = df_split[1].astype("int")
    df_grouped = df_split.groupby(0).sum()
    down = df_grouped.loc["down"][1]
    forward = df_grouped.loc["forward"][1]
    up = df_grouped.loc["up"][1]
    return down, up, forward


def multiply_positions(directions: Tuple) -> int:
    return (directions[0] - directions[1]) * directions[2]


def multiply_positions_with_aim(instructions: List) -> int:
    aim, depth, horizontal_pos = 0, 0, 0
    commands = []
    for instruction in instructions:
        direction, value = instruction.split(" ")
        commands.append((direction, int(value)))
    for direction, value in commands:
        if direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        elif direction == "forward":
            horizontal_pos += value
            depth += aim * value
    return horizontal_pos * depth


if __name__ == "__main__":
    commands = [line for line in utils.read_file("tests/day_02.txt")]
    values = get_values(commands)
    assert multiply_positions(values) == 150
    assert multiply_positions_with_aim(commands) == 900

    commands = [line for line in utils.read_file("inputs/day_02.txt")]
    values = get_values(commands)
    print(
        f"Horizontal position multiplied by final depth: {multiply_positions(values)}"
    )
    print(
        f"Horizontal position multiplied by final depth with aim: {multiply_positions_with_aim(commands)}"
    )
