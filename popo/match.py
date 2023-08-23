from utilities.validation import *
from popo import Player


class Match:
    def __init__(self, match_id: int, player_1: Player, player_2: Player, game: str, timebox: str,
                 expected_outcome: dict[int, float]):
        self._match_id: int = match_id
        self._player_1: Player = player_1.clone
        self._player_2: Player = player_2.clone
        self._game: str = game
        self._timebox: str = timebox

        # Data for both players based on database ID
        self._expected_outcome: dict[int, float] = expected_outcome
        self._outcome: dict[int, int] | None = None

    @property
    def match_id(self) -> int:
        return self._match_id

    @match_id.setter
    @int_validator
    def match_id(self, match_id: int):
        self._match_id = match_id

    @property
    def player_one(self) -> Player:
        return self._player_1

    @player_one.setter
    def player_one(self, player_1: Player):
        self._player_1 = player_1.clone

    @property
    def player_two(self) -> Player:
        return self._player_2

    @player_two.setter
    def player_two(self, player_2: Player):
        self._player_2 = player_2.clone

    @property
    def game(self) -> str:
        return self._game

    @game.setter
    @str_validator
    def game(self, game: str):
        self._game = game

    @property
    def timebox(self) -> str:
        return self._timebox

    @timebox.setter
    def timebox(self, timebox: str):
        self._timebox = timebox

    @property
    def expected_outcome(self) -> dict[int, float]:
        return self._expected_outcome

    @property
    def outcome(self) -> dict[int, int]:
        if self._outcome is None:
            raise ValueError(
                "Outcome shouldn't return None, match hasn't been completed and the call was made too early.")

        return self._outcome

    @outcome.setter
    def outcome(self, winner_id: int):
        match winner_id:
            case self._player_1:
                self._outcome = {
                    self._player_1: 1,
                    self._player_2: 0
                }
            case self._player_2:
                self._outcome = {
                    self._player_1: 0,
                    self._player_2: 1
                }

    @property
    def to_dict(self) -> dict:
        return {
            "match_id": self._match_id,
            "player_1": self._player_1.user_id,
            "player_2": self._player_2.user_id,
            "game": self._game,
            "timebox": self._timebox,
            "expected_outcome_p1": self._expected_outcome[self._player_1.user_id],
            "expected_outcome_p2": self._expected_outcome[self._player_2.user_id]
        }