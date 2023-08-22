from popo import Player
from popo import Match

from data import PlayerRepository
from data import MatchRepository

from service import glicko


class MatchMaker:
    def __init__(self):
        self._player_repository: PlayerRepository = PlayerRepository()
        self._match_repository: MatchRepository = MatchRepository()

        self._player_repository.load()

    def get_player(self, user_id: int) -> Player:
        return self._player_repository.retrieve(user_id)

    def update_player(self, user_id: int, player: Player):
        self._player_repository.update(user_id, player)

    def find_match_opponent(self, player_1: Player):
        pass

    def create_match(self, player_1: Player, player_2: Player):
        expected_outcomes: dict[int, float] = {
            player_1.user_id: glicko.calculate_expected_outcome(player_1.rating, player_2.rating, player_2.g_of_rd),
            player_2.user_id: glicko.calculate_expected_outcome(player_2.rating, player_1.rating, player_1.g_of_rd)
        }

        self._match_repository.create(player_1.user_id, player_2.user_id, expected_outcomes)

    def conclude_match(self, match: Match, result: dict[int, int]):
        match.outcome = result

        player_1: Player = self._player_repository.retrieve(match.player_one)
        player_2: Player = self._player_repository.retrieve(match.player_two)

        player_1_new_rating: int = glicko.calculate_new_rating(player_1, player_2, match)
        player_2_new_rating: int = glicko.calculate_new_rating(player_2, player_2, match)

        player_1_new_rating_deviation: int = glicko.calculate_rd_prime(player_1.rating, player_2.g_of_rd,
                                                                       match.expected_outcome[match.player_one])
        player_2_new_rating_deviation: int = glicko.calculate_rd_prime(player_2.rating, player_1.g_of_rd,
                                                                       match.expected_outcome[match.player_two])

        player_1_new_g_of_rd: float = glicko.calculate_g_of_rd(player_1_new_rating)
        player_2_new_g_of_rd: float = glicko.calculate_g_of_rd(player_2_new_rating)

        player_1_new = Player("pool", player_1_new_rating, player_1_new_rating_deviation, player_1_new_g_of_rd,
                              match.player_one, "1", "1")
        player_2_new = Player("pool", player_2_new_rating, player_2_new_rating_deviation, player_2_new_g_of_rd,
                              match.player_two, "1", "1")

        self.update_player(match.player_one, player_1_new)
        self.update_player(match.player_two, player_2_new)
