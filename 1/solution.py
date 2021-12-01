import pandas as pd


def solve():
    with open("input.txt", "r") as input_file:
        input_from_file = input_file.read()

    _input = [int(line) for line in input_from_file.splitlines()]

    df = pd.DataFrame(list(_input), columns=["Measurement"])
    df["Shifted"] = df["Measurement"].shift(-1)
    _filter = (df["Shifted"] - df["Measurement"]) > 0
    print(f"The number of times the measurement increased was: {_filter.sum()}")

    df_two = pd.DataFrame(list(_input), columns=["Measurement"])
    df_two["Sum of next three"] = df_two["Measurement"].rolling(3).sum().shift(-2)
    df_two["Shifted sum of next three"] = df_two["Sum of next three"].shift(-1)
    _filter_two = (df_two["Shifted sum of next three"] - df_two["Sum of next three"]) > 0
    print(f"The number of times the three-measurement sliding window increased was: {_filter_two.sum()}")

if __name__ == "__main__":
    solve()
