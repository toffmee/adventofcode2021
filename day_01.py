import pandas as pd
import utils
from typing import List


def count_depth_increases(measurements: List):
    df = pd.DataFrame(list(measurements), columns=["Measurement"])
    df["Shifted"] = df["Measurement"].shift(-1)
    _filter = (df["Shifted"] - df["Measurement"]) > 0
    return _filter.sum()


def count_sliding_window_sum(measurements: List):
    df_two = pd.DataFrame(list(measurements), columns=["Measurement"])
    df_two["Sum of next three"] = df_two["Measurement"].rolling(3).sum().shift(-2)
    df_two["Shifted sum of next three"] = df_two["Sum of next three"].shift(-1)
    _filter_two = (
        df_two["Shifted sum of next three"] - df_two["Sum of next three"]
    ) > 0
    return _filter_two.sum()


if __name__ == "__main__":
    depths = [int(line) for line in utils.read_file("tests/day_01.txt")]
    assert count_depth_increases(depths) == 7
    assert count_sliding_window_sum(depths) == 5

    depths = [int(line) for line in utils.read_file("inputs/day_01.txt")]
    print(
        f"The number of times the measurement increased was: {count_depth_increases(depths)}"
    )
    print(
        f"The number of times the three-measurement sliding window increased was: {count_sliding_window_sum(depths)}"
    )
