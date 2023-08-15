from popo import User
from popo import Player


class PlayerRepository:
    def __init__(self, user: User):
        self._user: User = user
        self.context: Player
        self.data: dict[int, Player]

    def create(self):
        pass

    def retrieve(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
