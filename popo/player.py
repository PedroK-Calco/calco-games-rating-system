from utilities.validation import *
from popo import User


class Player(User):
    def __init__(self, game: str, rating: int, deviation: int, g_of_rd: float, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self._game: str = game
        self._rating: int = rating
        self._deviation: int = deviation
        self._g_of_rd: float = g_of_rd

    @classmethod
    def new(cls, game: str, new_player_defaults: dict, user_id: int, name: str, email: str):
        return cls(game=game, rating=new_player_defaults["rating"], deviation=new_player_defaults["deviation"],
                   g_of_rd=new_player_defaults["g_of_rd"], user_id=user_id, name=name, email=email)

    @property
    def clone(self):
        return Player(self._game, self._rating, self._deviation, self._g_of_rd, self.user_id, self.name, self.email)

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

    @property
    def g_of_rd(self):
        return self._g_of_rd

    @g_of_rd.setter
    @int_validator
    def g_of_rd(self, g_of_rd: float):
        self._g_of_rd = g_of_rd

    @property
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "rating": self._rating,
            "rd": self._deviation,
            "g(rd)": self._g_of_rd
        }
