from popo import Player
from popo import Match

from data import MatchRepository

from service import glicko


class MatchService:
    def __init__(self, repo: MatchRepository):
        self._match_repository: MatchRepository = repo

        self._match_repository.load()

    def get_match(self, match_id: int) -> Match:
        return self._match_repository.retrieve(match_id)

    def find_match_opponent(self, player_1: Player):
        pass

    def create_match(self, player_1: Player, player_2: Player):
        expected_outcomes: dict[int, float] = {
            player_1.user_id: glicko.calculate_expected_outcome(player_1.rating, player_2.rating, player_2.g_of_rd),
            player_2.user_id: glicko.calculate_expected_outcome(player_2.rating, player_1.rating, player_1.g_of_rd)
        }

        self._match_repository.create(player_1, player_2, expected_outcomes)

    def conclude_match(self, match: Match, winner_id: int) -> dict[int, Player]:
        match: Match = match

        match.outcome = winner_id

        player_1: Player = match.player_one
        player_2: Player = match.player_two

        player_1_new_rating: int = glicko.calculate_new_rating(player_1, player_2, match)
        player_2_new_rating: int = glicko.calculate_new_rating(player_2, player_2, match)

        player_1_new_rating_deviation: int = glicko.calculate_rd_prime(player_1.deviation, player_2.g_of_rd,
                                                                       match.expected_outcome[match.player_one.user_id])
        player_2_new_rating_deviation: int = glicko.calculate_rd_prime(player_2.deviation, player_1.g_of_rd,
                                                                       match.expected_outcome[match.player_two.user_id])

        player_1_new_g_of_rd: float = glicko.calculate_g_of_rd(player_1_new_rating)
        player_2_new_g_of_rd: float = glicko.calculate_g_of_rd(player_2_new_rating)

        player_1_new = Player("pool", player_1_new_rating, player_1_new_rating_deviation, player_1_new_g_of_rd,
                              player_1.user_id, player_1.name, player_1.email)
        player_2_new = Player("pool", player_2_new_rating, player_2_new_rating_deviation, player_2_new_g_of_rd,
                              player_2.user_id, player_2.name, player_2.email)

        self._match_repository.delete(match.match_id)

        return {
            player_1.user_id: player_1_new,
            player_2.user_id: player_2_new
        }
