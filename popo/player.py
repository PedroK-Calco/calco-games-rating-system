from validation import *


class Player:
    def __init__(self, game: str, rating: int, deviation: int):
        self._game: str = game
        self._rating: int = rating
        self._deviation: int = deviation

    @property
    def game(self) -> str:
        return self._game

    @game.setter
    @str_validator
    def game(self, game: str):
        self._game = game

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    @int_validator
    def rating(self, rating: int):
        self._rating = rating

    @property
    def deviation(self) -> int:
        return self._deviation

    @deviation.setter
    @int_validator
    def deviation(self, deviation: int):
        self._deviation = deviation
        