from math import*

NEW_RATING: int = 1500
NEW_DEVIATION: int = 350


class Glicko:
    @staticmethod
    def calculate_rating(self, ratings: int) -> int:
        q: float = 0
        rd: int = 0
        d: float = 0
        sum_r: float = 0
        r: int = ratings + ((q / ((1 / rd ** 2) + (1 / d ** 2))) * sum_r)

        return r

    def calculate_deviation(self) -> int:
        pass

    @staticmethod
    def get_new_player_stats() -> tuple[int, int]:
        return NEW_RATING, NEW_DEVIATION

    # static methods to calculate variables
