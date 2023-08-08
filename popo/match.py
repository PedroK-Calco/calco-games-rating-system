from datetime import datetime
from validation import *


class Match:
    def __init__(self, match_id: int, player_one_id: int, player_two_id: int, game: str, timebox: datetime):
        self._match_id: int = match_id
        self._player_one_id: int = player_one_id
        self._player_two_id: int = player_two_id
        self._game: str = game
        self._timebox: datetime = timebox

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
    def timebox(self) -> datetime:
        return self._timebox

    @timebox.setter
    def timebox(self, timebox: datetime):
        self._timebox = timebox
