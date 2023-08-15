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

Additionally, the system uses variables in the calculation denoted by a letter.
What each letter signifies is quite advanced statistics that I do not understand.
Hence, they are simply copied with no explanation as to what they refer.
These are the variables:
    - 'g' of rating deviation
    - 'd'
"""

from math import *
from popo import Player
from popo import Match

NEW_RATING: int = 1500
MAX_DEVIATION: int = 350
MIN_DEVIATION: int = 30
Q: float = log(10) / 400


def calculate_new_rating(context_player: Player, opponent: Player, match: Match) -> int:
    """
    Calculate a new rating for a single context player.
    :param context_player: The player who's new rating will be calculated
    :param opponent: The opponent the context player played against
    :param match: The overall data of the match between the context player and the opponent
    :return: A new rating value for the context player
    """
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


def calculate_rd_time(rd_old: int) -> int:
    """
    Calculates a rating deviation value after a rating period
    :param rd_old: The current rating deviation of the player
    :return: A new rating deviation value with a maximum possible value of 350 and minimum possible value of 30
    """
    c = calculate_c(rd_old)

    rd = sqrt((rd_old ** 2) + (c ** 2))

    rd = __clamp_rd(rd)

    return rd


def calculate_rd_prime(rd_old: int, g_rd: float, e_o: float) -> int:
    """
    Calculates a rating deviation value based on the result of a match
    :param rd_old: The current rating deviation of the player
    :param g_rd: The g(RD) value of the player
    :param e_o: The expected outcome of the played match
    :return: A new rating deviation value with a maximum possible value of 350 and minimum possible value of 30
    """
    d: float = calculate_d(g_rd, e_o)

    rd = sqrt(((1 / (rd_old ** 2)) + (1 / (d ** 2))) ** -1)

    rd = __clamp_rd(rd)

    return rd


def calculate_g_of_rd(rd: int) -> float:
    """
    Calculates the g value of the player's rating deviation
    :param rd: The player's rating deviation
    :return: The g value of rating deviation
    """
    g_rd: float = 1 / sqrt(1 + (3 * (Q ** 2)) * (rd ** 2) / (pi ** 2))

    return g_rd


def calculate_expected_outcome(r: int, r_j: int, g_of_rd_j: float) -> float:
    """
    Calculates the expected outcome of a match for the context player
    :param r: Player's rating to calculate the expected outcome for
    :param g_of_rd_j: g(RD) of the opponent
    :param r_j: Opponent's rating
    :return: Expected Outcome of the match
    """
    e_o = 1 / (1 + (10 ** (-g_of_rd_j * (r - r_j) / 400)))

    return e_o


def calculate_d(g_of_rd_j: float, e_o: float) -> float:
    """
    Calculate the d value
    :param g_of_rd_j: g(RD) of the opponent
    :param e_o: Expected Outcome of the match
    """
    d = (Q ** 2) * ((g_of_rd_j ** 2) * e_o * (1 - e_o)) ** -1

    return d


def calculate_c(rd: int) -> any:
    c = sqrt((MAX_DEVIATION ** 2) - (rd ** 2)) / sqrt(30)

    return c


def get_new_player_stats() -> dict[str, int | float]:
    """
    Get the starting default rating values
    :return: A dictionary containing the default rating, rating deviation, and g(RD)
    """
    return {
        "rating": NEW_RATING,
        "deviation": MAX_DEVIATION,
        "g_of_rd": calculate_g_of_rd(NEW_RATING)
    }


def __clamp_rd(rd: int | float) -> int:
    """
    Clamps the rd value between a maximum value of 350 and a minimum value of 30.
    Also casts the data type of rd to an int
    :param rd: The rating deviation to be clamped
    :return: The clamped rating deviation casted to an int
    """

    # RD is either new value or 350 if the new value is greater than 350
    clamped = min(rd, MAX_DEVIATION)

    # RD is either new value or 30 if the new value is less than 30
    clamped = max(clamped, MIN_DEVIATION)

    return int(clamped)
