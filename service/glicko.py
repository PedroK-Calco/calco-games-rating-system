from math import *

NEW_RATING: int = 1500
NEW_DEVIATION: int = 350


def calculate_rating(ratings: int) -> int:
    q: float = calculate_q()
    rd: int = 0
    d: float = calculate_d()
    sum_r: float = calculate_sum_r()
    r: int = ratings + ((q / ((1 / rd ** 2) + (1 / d ** 2))) * sum_r)

    return r


def calculate_deviation() -> int:
    pass


def calculate_q() -> float:
    pass


def calculate_d() -> float:
    pass


def calculate_sum_r() -> float:
    pass


def get_new_player_stats() -> tuple[int, int]:
    return NEW_RATING, NEW_DEVIATION
