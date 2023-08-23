from popo import Player
from data import PlayerRepository


class PlayerService:
    def __init__(self):
        self._repository: PlayerRepository = PlayerRepository()

        self._repository.load()

    def get_player(self, user_id: int) -> Player:
        return self._repository.retrieve(user_id)

    def update_player(self, user_id: int, player: Player):
        self._repository.update(user_id, player)
