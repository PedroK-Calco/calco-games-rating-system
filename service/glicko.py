from math import *

NEW_RATING: int = 1500
NEW_DEVIATION: int = 350
Q: float = log(10) / 400


def calculate_new_rating(r: int, rd: int, r_j: int, rd_j: int, s: int, e_o: float) -> int:
    """
    Calculate the new rating of the context player
    :param r: Player's rating
    :param rd: Player's rating deviation
    :param r_j: Opponent's rating
    :param rd_j: Opponnt's rating deviation
    :param s: Outcome of the match (1 = win, 0 = loss)
    :param e_o: The expected outcome of the match before it was played
    :return: Post rating period player rating
    """
    g_rd: float = calculate_g_of_rd(rd)
    g_j: float = calculate_g_of_rd(rd_j)
    d: float = calculate_d(g_j=g_j, e_o=calculate_expected_outcome(g_j, r, r_j))
    new_r: int = r + ((Q / ((1 / rd ** 2) + (1 / d ** 2))) * (g_rd * (s - e_o)))

    return new_r


def calculate_deviation(rd: int, g_rd: float, e_o: float):
    d: float = calculate_d(g_rd, e_o)

    new_rd = (sqrt((1 / (rd ** 2)) + (1 / (d ** 2)))) ** -1

    # RD is either new value or 350 if the new value is greater than 350
    new_rd = min(new_rd, NEW_DEVIATION)

    return new_rd


def calculate_g_of_rd(rd: int) -> float:
    # G is a function that takes RD
    g_rd: float = 1 / sqrt(1 + (3 * (Q ** 2)) * (rd ** 2) / (pi ** 2))

    return g_rd


def calculate_expected_outcome(g_j: float, r: int, r_j: int) -> float:
    """
    :param g_j: g(RD) of the opponent
    :param r: Player's rating
    :param r_j: Opponent's rating
    :return: Expected Outcome of the match
    """
    e_o = 1 / (1 + (10 ** (-g_j * (r - r_j) / 400)))

    return e_o


def calculate_d(g_j: float, e_o: float) -> float:
    """
    :param g_j: g(RD) of the opponent
    :param e_o: Expected Outcome of the match
    """
    d = (Q ** 2) * ((g_j ** 2) * e_o * (1 - e_o)) ** -1

    return d


def get_new_player_stats() -> dict[str, int | float]:
    return {
        "rating": NEW_RATING,
        "deviation": NEW_DEVIATION,
        "g_rd": calculate_g_of_rd(NEW_RATING)
    }
