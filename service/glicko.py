from math import *

NEW_RATING: int = 1500
NEW_DEVIATION: int = 350


def calculate_rating(ratings: int) -> int:
    q: float = calculate_q()
    g_rd: float = calculate_g_rd()
    rd: int = 0
    d: float = calculate_d()
    sum_r: float = calculate_sum_r()
    r: int = ratings + ((q / ((1 / rd ** 2) + (1 / d ** 2))) * sum_r)

    return r


def calculate_deviation() -> int:
    pass


def calculate_q() -> float:
    q: float = log(10) / 400

    return q


def calculate_g_rd(q: float, rd: int) -> float:
    g_rd: float = 1 / sqrt(1 + (3 * (q ** 2)) * (rd ** 2) / (pi ** 2))

    return g_rd


def calculate_d() -> float:
    pass


def calculate_sum_r() -> float:
    pass


def get_new_player_stats() -> tuple[int, int]:
    return NEW_RATING, NEW_DEVIATION
