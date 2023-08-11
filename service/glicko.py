"""
The Glicko system was created by Dr. Mark E. Glickman.
This implementation utilizes several variable naming structures found in the
Glicko system paper: http://www.glicko.net/glicko/glicko.pdf.

Calculations performed by this system are done with a 'context player'.
In other words, the first-person perspective.
This means that similarly, the same calculations will need to be called for the opponent
as the 'context player'.

This implementation makes the following variable naming assertions:
    - 'User' refers to the context player that the calculations are being done for
    - '_j' refers to the context opponent of the player that the calculations are being done for
"""

from math import *
from popo import Player
from popo import Match

NEW_RATING: int = 1500
NEW_DEVIATION: int = 350
Q: float = log(10) / 400


def calculate_new_rating(context_player: Player, opponent: Player, match: Match) -> int:
    r: int = context_player.rating  # User's rating
    rd: int = context_player.deviation  # User's deviation
    g_of_rd: float = context_player.g_of_rd  # User's g(deviation) value

    r_j: int = opponent.rating  # Opponent's rating
    rd_j: int = opponent.deviation  # Opponent's deviation
    g_of_rd_j: int = opponent.g_of_rd  # Opponent's g(deviation) value

    e_o: float = match.expected_outcome[opponent.user_id]  # Expected outcome of the match relative to the opponent
    s: int = match.outcome[context_player.user_id]  # Outcome of the match tied to user's id

    d: float = calculate_d(g_of_rd_j=g_of_rd_j, e_o=calculate_expected_outcome(g_of_rd_j, r, r_j))

    new_r: int = r + ((Q / ((1 / rd ** 2) + (1 / d ** 2))) * (g_of_rd * (s - e_o)))

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


def calculate_d(g_of_rd_j: float, e_o: float) -> float:
    """
    :param g_of_rd_j: g(RD) of the opponent
    :param e_o: Expected Outcome of the match
    """
    d = (Q ** 2) * ((g_of_rd_j ** 2) * e_o * (1 - e_o)) ** -1

    return d


def get_new_player_stats() -> dict[str, int | float]:
    return {
        "rating": NEW_RATING,
        "deviation": NEW_DEVIATION,
        "g_of_rd": calculate_g_of_rd(NEW_RATING)
    }
