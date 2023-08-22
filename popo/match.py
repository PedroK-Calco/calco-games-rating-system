from utilities.validation import *


class Match:
    def __init__(self, match_id: int, player_one_id: int, player_two_id: int, game: str, timebox: str,
                 expected_outcome: dict[int, float]):
        self._match_id: int = match_id
        self._player_one_id: int = player_one_id
        self._player_two_id: int = player_two_id
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
    def player_one(self) -> int:
        return self._player_one_id

    @player_one.setter
    @int_validator
    def player_one(self, player_one_id: int):
        self._player_one_id = player_one_id

    @property
    def player_two(self) -> int:
        return self._player_two_id

    @player_two.setter
    @int_validator
    def player_two(self, player_two_id: int):
        self._player_two_id = player_two_id

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
            case self._player_one_id:
                self._outcome = {
                    self._player_one_id: 1,
                    self._player_two_id: 0
                }
            case self._player_two_id:
                self._outcome = {
                    self._player_one_id: 0,
                    self._player_two_id: 1
                }
