import numpy as np
import utils
from typing import List
import numpy.typing as npt


def get_bingo_boards(bingo: List) -> npt.ArrayLike:
    bingo_copy = [
        bingo_board.split() for bingo_board in bingo.copy()[2:] if bingo_board
    ]
    bingo_boards = np.array(bingo_copy).reshape(-1, 5, 5)
    return bingo_boards


def get_called_numbers(bingo: List) -> List:
    return [int(number) for number in bingo[0].split(",")]


def check_for_bingo(bingo_board: npt.ArrayLike) -> bool:
    for i in range(5):
        row_x = np.sum(bingo_board[i, :] == "X")
        col_x = np.sum(bingo_board[:, i] == "X")
        if row_x == 5 or col_x == 5:
            return True


def calculate_bingo_score(bingo_boards: npt.ArrayLike, called_numbers: List) -> int:
    for number in called_numbers:
        for x in range(len(bingo_boards)):
            bingo_boards[x] = np.where(
                bingo_boards[x] == str(number), "X", bingo_boards[x]
            )
            if check_for_bingo(bingo_boards[x]) is True:
                not_marked_numbers_sum = np.sum(
                    bingo_boards[x]
                    .flatten()[bingo_boards[x].flatten() != "X"]
                    .astype(int)
                )
                return not_marked_numbers_sum * number


def calculate_last_board_score(
    bingo_boards: npt.ArrayLike, called_numbers: List
) -> int:
    winning_boards = []
    for number in called_numbers:
        for x in range(len(bingo_boards)):
            bingo_boards[x] = np.where(
                bingo_boards[x] == str(number), "X", bingo_boards[x]
            )
            if check_for_bingo(bingo_boards[x]) is True and x not in winning_boards:
                winning_boards.append(x)
                if len(winning_boards) == len(bingo_boards):
                    not_marked_numbers_sum = np.sum(
                        bingo_boards[x]
                        .flatten()[bingo_boards[x].flatten() != "X"]
                        .astype(int)
                    )
                    return not_marked_numbers_sum * number


if __name__ == "__main__":
    bingo = [line for line in utils.read_file("tests/day_04.txt")]
    called_numbers = get_called_numbers(bingo)
    bingo_boards = get_bingo_boards(bingo)
    assert calculate_bingo_score(bingo_boards, called_numbers) == 4512
    assert calculate_last_board_score(bingo_boards, called_numbers) == 1924

    bingo = [line for line in utils.read_file("inputs/day_04.txt")]
    called_numbers = get_called_numbers(bingo)
    bingo_boards = get_bingo_boards(bingo)
    print(
        f"Final score be if you choose that board: {calculate_bingo_score(bingo_boards, called_numbers)}"
    )
    print(
        f"Final score for last board: {calculate_last_board_score(bingo_boards, called_numbers)}"
    )
