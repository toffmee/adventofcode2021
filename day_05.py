import itertools

import numpy as np
from collections import Counter
import utils
from typing import List
import numpy.typing as npt
import re


def calculate_overlapping_count(
    lines: List, calculate_diagonals=False
) -> npt.ArrayLike:
    lines = [re.split("[ ,\->!?:]+", line) for line in lines]
    points = [[int(coord) for coord in coords] for coords in lines]
    line_coordinates = []
    for x1, y1, x2, y2 in points:
        if x1 == x2:
            max_x, min_x = max(y2, y1), min(y2, y1)
            coords = [(x1, y) for y in range(min_x, max_x + 1)]
            line_coordinates.append(coords)
        if y1 == y2:
            max_y, min_y = max(x2, x1), min(x2, x1)
            coords = [(x, y1) for x in range(min_y, max_y + 1)]
            line_coordinates.append(coords)
        if calculate_diagonals and x1 != x2 and y1 != y2:
            line_coordinates.append(
                list(
                    zip(
                        np.linspace(x1, x2, max(x1 - x2, x2 - x1) + 1, dtype=int),
                        np.linspace(y1, y2, max(y1 - y2, y2 - y1) + 1, dtype=int),
                    )
                )
            )
    flatten_coordinates = list(itertools.chain(*line_coordinates))
    common_points = [
        coordinate
        for coordinate, count in Counter(flatten_coordinates).items()
        if count > 1
    ]
    return len(common_points)


if __name__ == "__main__":
    lines = [line for line in utils.read_file("tests/day_05.txt")]
    assert calculate_overlapping_count(lines) == 5
    assert calculate_overlapping_count(lines, calculate_diagonals=True) == 12

    lines = [line for line in utils.read_file("inputs/day_05.txt")]
    print(f"Two lines overlap in at least: {calculate_overlapping_count(lines)} points")
    print(
        f"While counting diagonals at least two lines overlap in: {calculate_overlapping_count(lines, calculate_diagonals=True)} points"
    )
