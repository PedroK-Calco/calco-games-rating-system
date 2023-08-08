from validation import validator


class Player:
    def __init__(self, game: str, rating: int, deviation: int):
        self._game: str = game
        self._rating: int = rating
        self._deviation: int = deviation

    @property
    def game(self) -> str:
        return self._game

    @game.setter
    @validator(lambda s: [s == "", s is None], ValueError("Game can't be blank or None"))
    def game(self, game: str):
        self._game = game

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    @validator(lambda n: n < 0, ValueError("Rating can't be less than 0"))
    def rating(self, rating: int):
        self._rating = rating

    @property
    def deviation(self) -> int:
        return self._deviation

    @deviation.setter
    @validator(lambda n: n < 0, ValueError("Deviation can't be less than 0"))
    def deviation(self, deviation: int):
        self._deviation = deviation
        