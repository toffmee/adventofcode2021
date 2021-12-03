from typing import List
import utils
import pandas as pd


def calculate_power_consumption(bits: List) -> int:
    df = pd.DataFrame(bits, columns=["Bits"])
    df_split = df["Bits"].astype(str).str.join(" ").str.split(" ", expand=True)
    gamma_rate_binary = []
    epsilon_rate_binary = []
    for column in df_split:
        indexes = df_split[column].value_counts().index
        gamma_rate_binary.append(indexes[0])
        epsilon_rate_binary.append(indexes[1])
    gamma_rate = int("".join(gamma_rate_binary), 2)
    epsilon_rate = int("".join(epsilon_rate_binary), 2)
    return gamma_rate * epsilon_rate


def get_oxygen_generator_rating(bits: List) -> int:
    oxygen_generator_rating = bits.copy()
    i = 0
    while len(oxygen_generator_rating) != 1:
        ones = [row[i] for row in oxygen_generator_rating].count("1")
        zeros = len(oxygen_generator_rating) - ones
        if ones >= zeros:
            keep = "1"
        else:
            keep = "0"
        oxygen_generator_rating = [
            line for line in oxygen_generator_rating if line[i] == keep
        ]
        i += 1
    return int("".join(oxygen_generator_rating), 2)


def get_co_scrubber_rating(bits: List) -> int:
    co_scrubber_rating = bits.copy()
    i = 0
    while len(co_scrubber_rating) != 1:
        ones = [row[i] for row in co_scrubber_rating].count("1")
        zeros = len(co_scrubber_rating) - ones
        if zeros > ones:
            keep = "1"
        else:
            keep = "0"
        co_scrubber_rating = [line for line in co_scrubber_rating if line[i] == keep]
        i += 1
    return int("".join(co_scrubber_rating), 2)


if __name__ == "__main__":
    test_bits = [line for line in utils.read_file("tests/day_03.txt")]
    assert calculate_power_consumption(test_bits) == 198
    assert (
        get_oxygen_generator_rating(test_bits) * get_co_scrubber_rating(test_bits)
    ) == 230

    puzzle_bits = [line for line in utils.read_file("inputs/day_03.txt")]
    print(
        f"Power consumption of the submarine: {calculate_power_consumption(puzzle_bits)}"
    )
    print(
        f"Life support rating of the submarine: {get_oxygen_generator_rating(puzzle_bits) * get_co_scrubber_rating(puzzle_bits)}"
    )
